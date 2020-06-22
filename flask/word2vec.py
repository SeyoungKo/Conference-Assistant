from gensim.models import word2vec;print("FAST_VERSION", word2vec.FAST_VERSION)
import gensim; print("gensim", gensim.__version__)
import datetime

now = datetime.datetime.now()
file_name = ''
input_similar = ''

# rtn_keyword :['aaa','bbb'..] rtn_messages = 'aabbcc..'
def create_model(top_word):

    wData = word2vec.LineSentence(
        "/Users/seyoung/Conference-Assistant/Conference-Assistant/flask/sentences/text_sentences.csv")
    wModel = word2vec.Word2Vec(wData, iter=20, size=20, window=3, hs=1, min_count=2, sg=1)

    file_name = "words.unit_model"
    wModel.save("/Users/seyoung/Conference-Assistant/Conference-Assistant/flask/stored_model/" + file_name)
    print("model saved")

    most_similar(top_word)

def most_similar(top_word):
    model = word2vec.Word2Vec.load(
        "/Users/seyoung/Conference-Assistant/Conference-Assistant/flask/stored_model/" + file_name)

    rtn = []

    try:
        input_similar = top_word

        print("most_similar is called")
        rtn.append(model.most_similar(input_similar))

        print("similarity: ", rtn)
        # print("similarity :" , rtn)

    except Exception as e:
        print("Exception occurred!!!!")

    # finally:
        # rtn_keyword = kw
        # print("rtn_keyword:", rtn_keyword, "type:", type(rtn_keyword))


# def main(rtn_keyword):
#     create_model(rtn_keyword)
