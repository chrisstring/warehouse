#first script of the firsts7test in python. it works!! can you commit this? maybe
#!/usr/bin/env python3
import requests,time

url = "https://s7sps1apissl.scene7.com/scene7/services/IpsApiService"

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns=\"http://www.scene7.com/IpsApi/xsd/2014-04-03\">\r\n   <soapenv:Header>\r\n      <ns:authHeader>\r\n         <!--Optional:-->\r\n         <ns:user>chris.string@turn5.com</ns:user>\r\n         <!--Optional:-->\r\n         <ns:password>Password2#</ns:password>\r\n         <ns:locale>EN</ns:locale>\r\n         <ns:appName>bertzSerch</ns:appName>\r\n         <ns:appVersion>69</ns:appVersion>\r\n      </ns:authHeader>\r\n   </soapenv:Header>\r\n   <soapenv:Body>\r\n      <ns:searchAssetsParam>\r\n         <ns:companyHandle>c|8676</ns:companyHandle>\r\n         <ns:includeSubfolders>1</ns:includeSubfolders>\r\n         <ns:keywordArray>\r\n            <!--Zero or more repetitions:-->\r\n            <ns:items>J100103</ns:items>\r\n         </ns:keywordArray>\r\n      </ns:searchAssetsParam>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>"
headers = {
    'soapaction': "searchAssets",
    'cache-control': "no-cache"
    }
print("sending searchAssets request...")
t0 = time.clock()
response = requests.request("POST", url, data=payload, headers=headers)
t1 = time.clock()
print(response.text)

print("\n\n\tCompleted: {}s".format(t1-t0))
