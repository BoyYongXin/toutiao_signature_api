# 使用说明

1.npm需安装express

`npm install express #推荐使用局部安装  `

2.将3个文件放于同一文件夹，cd到该目录，命令行运行

```javascript
node server.js
```

3.测试接口是否开启成功，如下命令：

```
http://XX.XX.XX.XX:3002
```



4.运行api_test.py开始测试使用

```
{'error_code': -1, 'msg': 'https://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as=A1A53E0E9392C5D&cp=5EE3729CA58D3E1&max_behot_time=1591940030&_signature=q0yg5AAgEBBUs18btVJzAqtMIfAAPW-'}
```

以上结果为正常使用


### 由于pyexecjs运行会报以下错误，因此这里使用接口调用。如有解决办法，请联系告知，谢谢！
```python
TypeError: Cannot read property 'init' of undefined
```
### 实际为无法读取window.byted_acrawler对象，但node运行正常

