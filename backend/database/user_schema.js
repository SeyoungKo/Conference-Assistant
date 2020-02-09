var Schema = {};

Schema.createSchema = function(mongoose){

    var UserSchema = mongoose.Schema({
        id : {type : String, 'default':''},
        hashed_password : {type : String, required:true, 'default':''},
        salt : {type : String, required : true},
        name : {type : String, index : 'hashed', 'default' : ''},
        tel : {type : String, 'default' : ''},
        email : {type : String, 'default' : ''},
        created_at : {type: Date, index : {unique : false}, 'default' : Date.now},
        updated_at : {type : Date, index : {unique : false}, 'default' : Date.now}
    });

    UserSchema.path('hashed_password').validate(function (hashed_password){
         return hashed_password.length;
    }, 'hashed_password 칼럼 값이 없음');

    // 모델 객체에서 사용하는 메소드 정의
    UserSchema.static('findById', function(id, callback){
        return this.find({id : id}, callback);
    });

    UserSchema.static('findAll', function(callback){
        return this.find({ }, callback);
    })
}