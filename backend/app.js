// express 기본 모듈
var express = require('express')
    ,http  = require('http')
    ,path = require('path');

// express 미들웨어
var bodyParser = require('body-parser')
   ,cookieParser = require('cookie-parser')
   ,static = require('serve-static')
   ,errorHandler = require('errorhandler');

// 에러 핸들러 모듈
var expressErrorHandler = require('express-error-handler');

// Session 미들웨어
var expressSession = require('express-session');

var app = express();

// 서버 변수 설정 및 public 폴더 설정
app.set('port', process.env.PORT || 3000);

// body-parser로 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({extended:false}))

// body-parser로 application/json 파싱
app.use(bodyParser.json())

// public을 static으로 오픈
app.use('/public', static(path.join(__dirname,'public')))

// cookie-parser 설정
app.use(cookieParser());

// 세션 설정
app.use(expressSession({
    secret:'my key',
    resave:true,
    saveUninitialized:true
}));

// 404 에러페이지 처리
var errorHandler = expressErrorHandler({
    static:{
        '404':'./public/404.html'
    }
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

// ==== server on ====

// passport 사용
var passport= require('passport');
var flash = require('connect-flash');

app.use(passport.initialize()); // passport 초기화
app.use(passport.session());  // 세션 유지
app.use(flash());

// express 서버 시작
http.createServer(app).listen(app.get('port'),function(){
    console.log('server on! port:' + app.get('port'));
});