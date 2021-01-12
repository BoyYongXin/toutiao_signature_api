import requests

url = "http://localhost/sign/toutiao"
url = "http://XXXXXXXXXX/sign/toutiao"
data = {
    # "url": "https://www.toutiao.com/toutiao/c/user/article/?user_id=4010048375&page_type=0&max_behot_time=0&count=10&version=2&platform=pc&as=A1B59E8E83128CD&cp=5EE3E2E81C1DCE1",
    # "url": "https://www.toutiao.com/toutiao/c/user/article/?page_type=1&user_id=4377795668&max_behot_time=0&count=20"
    "url": "https://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as=A1A53E0E9392C5D&cp=5EE3729CA58D3E1&max_behot_time=1591940030"
}
res = requests.post(url, data=data).json()
print(res)

## result
# {'error_code': -1, 'msg': 'https://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as=A1A53E0E9392C5D&cp=5EE3729CA58D3E1&max_behot_time=1591940030&_signature=jmTw2gAgEBBxmw8la8v8yY5kccAANCU'}
