import re
import networkx
import pandas as pd
# ===
from gensim.models import word2vec;print("FAST_VERSION", word2vec.FAST_VERSION)
import gensim; print("gensim", gensim.__version__)

rtn_final =[]
stopword =''
kw = ''
rtn_keyword=''
append_words = []
weight_list = []
keywords_dict = {}

main_words = []
sub_words = []
tmp = []
rtn_appendwords = []

class RawSentence:
    def __init__(self, textIter):
        if type(textIter) == str:
            self.textIter = textIter.split('\n')
        else:
            self.textIter = textIter
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in self.textIter:
            ch = self.rgxSplitter.split(line)
        if len(ch) == 1:
            ch.append(".")
        for s in map(lambda a, b: a + b, ch[0::2], ch[1::2]):
        # print(s)
            if not s: continue
            yield (self.tagger.pos(s))

class RawSentenceReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in open(self.filepath, encoding='utf-8'):
            ch = self.rgxSplitter.split(line)
            for s in map(lambda a, b: a + b, ch[::2], ch[1::2]):
                if not s: continue
                yield s


class RawTagger:
    def __init__(self, textIter, tagger=None):
        if tagger:
            self.tagger = tagger
        else:
            from konlpy.tag import Komoran
            self.tagger = Komoran()
        if type(textIter) == str:
            self.textIter = textIter.split('\n')
        else:
            self.textIter = textIter
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        # print(self.textIter)
        for line in self.textIter:
            ch = self.rgxSplitter.split(line)
            if len(ch) == 1:
                ch.append(".")
            for s in map(lambda a, b: a + b, ch[::2], ch[1::2]):
                if not s: continue
                yield (self.tagger.pos(s))

class RawTaggerReader:
    def __init__(self, filepath, tagger=None):
        if tagger:
            self.tagger = tagger
        else:
            from konlpy.tag import Komoran
            self.tagger = Komoran()
        self.filepath = filepath
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in open(self.filepath, encoding='utf-8'):
            ch = self.rgxSplitter.split(line)
            for s in map(lambda a, b: a + b, ch[::2], ch[1::2]):
                if not s: continue
                yield self.tagger.pos(s)
                # print(self.tagger.pos(s))


class TextRank:
    global rtn_final

    def __init__(self, **kargs):
        self.graph = None
        self.window = kargs.get('window', 5)
        self.coef = kargs.get('coef', 1.0)
        self.threshold = kargs.get('threshold', 0.003)
        self.dictCount = {}
        self.dictBiCount = {}
        self.dictNear = {}
        self.nTotal = 0

    def load(self, sentenceIter, wordFilter=None):
        def insertPair(a, b):
            if a > b:
                a, b = b, a
            elif a == b:
                return
            self.dictBiCount[a, b] = self.dictBiCount.get((a, b), 0) + 1

        def insertNearPair(a, b):
            self.dictNear[a, b] = self.dictNear.get((a, b), 0) + 1

        for sent in sentenceIter:
            for i, word in enumerate(sent):
                if wordFilter and not wordFilter(word): continue
                self.dictCount[word] = self.dictCount.get(word, 0) + 1
                self.nTotal += 1
                if i - 1 >= 0 and (not wordFilter or wordFilter(sent[i - 1])): insertNearPair(sent[i - 1], word)
                if i + 1 < len(sent) and (not wordFilter or wordFilter(sent[i + 1])): insertNearPair(word, sent[i + 1])
                for j in range(i + 1, min(i + self.window + 1, len(sent))):
                    if wordFilter and not wordFilter(sent[j]): continue
                    if sent[j] != word: insertPair(word, sent[j])

    def loadSents(self, sentenceIter, tokenizer=None):
        import math
        def similarity(a, b):
            n = len(a.intersection(b))
            return n / float(len(a) + len(b) - n) / (math.log(len(a) + 1) * math.log(len(b) + 1))

        if not tokenizer: rgxSplitter = re.compile('[\\s.,:;-?!()"\']+')
        sentSet = []
        for sent in filter(None, sentenceIter):
            if type(sent) == str:
                if tokenizer:
                    s = set(filter(None, tokenizer(sent)))
                else:
                    s = set(filter(None, rgxSplitter.split(sent)))
            else:
                s = set(sent)
            if len(s) < 2: continue
            self.dictCount[len(self.dictCount)] = sent
            sentSet.append(s)

        for i in range(len(self.dictCount)):
            for j in range(i + 1, len(self.dictCount)):
                s = similarity(sentSet[i], sentSet[j])
                if s < self.threshold: continue
                self.dictBiCount[i, j] = s

    def getPMI(self, a, b):
        import math
        co = self.dictNear.get((a, b), 0)
        if not co: return None
        return math.log(float(co) * self.nTotal / self.dictCount[a] / self.dictCount[b])

    def getI(self, a):
        import math
        if a not in self.dictCount: return None
        return math.log(self.nTotal / self.dictCount[a])

    def build(self):
        self.graph = networkx.Graph()
        self.graph.add_nodes_from(self.dictCount.keys())
        for (a, b), n in self.dictBiCount.items():
            self.graph.add_edge(a, b, weight=n * self.coef + (1 - self.coef))

    def rank(self):
        return networkx.pagerank(self.graph, weight='weight')

    def extract(self, ratio=0.1):
        global append_words

        ranks = self.rank()
        cand = sorted(ranks, key=ranks.get, reverse=True)[:int(len(ranks) * ratio)]
        pairness = {}
        startOf = {}
        tuples = {}
        for k in cand:
            tuples[(k,)] = self.getI(k) * ranks[k]
            for l in cand:
                if k == l: continue
                pmi = self.getPMI(k, l)
                if pmi: pairness[k, l] = pmi


        for (k, l) in sorted(pairness, key=pairness.get, reverse=True):
            # print(k[0], l[0], pairness[k, l])
            str = k[0], l[0], pairness[k, l]
            append_words.append(str)
            rtn_final.append(k[0]+l[0])

            if k not in startOf: startOf[k] = (k, l)

        for (k, l), v in pairness.items():
            pmis = v
            rs = ranks[k] * ranks[l]
            path = (k, l)
            tuples[path] = pmis / (len(path) - 1) * rs ** (1 / len(path)) * len(path)
            last = l
            while last in startOf and len(path) < 7:
                if last in path: break
                pmis += pairness[startOf[last]]
                last = startOf[last][1]
                rs *= ranks[last]
                path += (last,)
                tuples[path] = pmis / (len(path) - 1) * rs ** (1 / len(path)) * len(path)

        used = set()
        both = {}
        for k in sorted(tuples, key=tuples.get, reverse=True):
            if used.intersection(set(k)): continue
            both[k] = tuples[k]
            for w in k: used.add(w)

        return rtn_final

    def summarize(self, ratio=0.333):
        r = self.rank()
        ks = sorted(r, key=r.get, reverse=True)[:int(len(r) * ratio)]
        return ' '.join(map(lambda k: self.dictCount[k], sorted(ks)))

def f(t, d):
    # d is document == tokens
    return d.count(t)


def init(text):
    global kw
    global rtn_keyword
    global main_words
    global sub_words
    global tmp
    global keywords_dict
    global rtn_appendwords

    tr = TextRank(window=5, coef=0)
    sent = text

    stopword = set([('있'), ('하'), ('되'), ('넣'), ('가'), ('아'), ('안'), ('쓰'), ('때'), ('록'), ('좋') ])
    tr.load(RawTagger(sent), lambda w: w not in stopword and (w[1] in ('NNG', 'NNP')))

    tr.build()
    # 가중치 제외 append word 출력
    kw = tr.extract(1)

    # #  가중치+ 단어 저장
    # for i in range(0, len(append_words)):
    #     str = append_words[i][0] + append_words[i][1]
    #     weight = append_words[i][2]
    #     dict = {str : weight}
    #     # 리스트에 가중치, 단어 저장
    #     weight_list.append(dict)
    #
    # # 가중치값이 가장 높은 단어
    # top_word =''.join(tuple(weight_list[0].keys()))
    # second_word = ''.join(tuple(weight_list[int(len(weight_list)/2)].keys()))


    for j in range(0, len(kw)):
        if j%5 ==0 or j==0:
            main_words.append(kw[j])
        else:
            tmp.append(kw[j])

    i =0
    count =1
    last_idx = 0

    num = int(len(tmp)/ len(main_words))

    # main : sub
    for k in range(0, len(main_words)):
        arr = []
        for l in range(last_idx+i, num*count):
            arr.append(tmp[l])
        sub_words.append(arr)

        last_idx = num*count
        count +=1
        i+=1


    # [{'mainword' :['sub1','sub2'...]}, {'mainword2':['sub1','sub2'...]}
    for i in range(0, len(main_words)):
        keywords_dict = {main_words[i] : sub_words[i]}
        rtn_appendwords.append(keywords_dict)

    print("tmp : ", tmp)
    print("sub words : ", len(sub_words),sub_words, )
    print("main words : ", len(main_words), main_words)
    print("sub+main_dict :",len(rtn_appendwords), rtn_appendwords)
    # {main tag : (sub word, subword...)}


    # rtn_messages to csv
    # df = []
    # df.append(text)

    # dataframe = pd.DataFrame(df)
    # dataframe.to_csv("/Users/seyoung/Conference-Assistant/Conference-Assistant/flask/sentences/text_sentences.csv",
    #                  header=False, index=False)


    rtn_keyword = kw
    print("rtn_keyword:", rtn_keyword, "type:", type(rtn_keyword))

    # 모델 호출
    # word2vec.create_model(top_word)

    kw=''

# if __name__ == '__main__':
#     tr = TextRank()
#     tr.build()

