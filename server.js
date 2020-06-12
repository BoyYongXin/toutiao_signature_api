const express = require("express");
const app = express(); // express实例化
// 监听端口，设置回调
app.listen(3001,()=>{
    console.log("server start");
});


const {getUrl} = require('./get_args');// 导入模块
const bodyParser = require("body-parser");// 插件
//app.use 使用中间件(插件)
app.use(bodyParser.urlencoded({extend:false}));
//设置一个post接口
app.post('/sign/toutiao',(req,res)=>{
    let {url} = req.body;
    if(url){
        res.send({error_code:-1,msg:getUrl(url)});
    }else{
        res.send({error_code:0,msg:getUrl(url)});
    }
    
});