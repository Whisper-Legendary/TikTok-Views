import requests,random
from getuseragent import UserAgent
ua = UserAgent("ios").Random()
user=input('[+] TikTok UserName : ')
link=input('[+] Video Link : ')
res=requests.post('https://api.likesjet.com/freeboost/3',json={"link":link,"tiktok_username":user,"email":f"whisper{random.randint(100000,999999)}@gmail.com"},headers={"Host": "api.likesjet.com","content-length": "137","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","user-agent":ua,"sec-ch-ua-platform": "\"Android\"","origin": "https://likesjet.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://likesjet.com/","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"}).json()
print(res)
