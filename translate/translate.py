import urllib.request
import json

text=str(input("Please input the contents you want to translate\n"))

url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data={}
data['i']=text
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='15479533612685'
data['sign']='77a353b2f2311126d114b9774695aeae'
data['ts']='1547953361268'
data['bv']='1de9313c44872e4c200c577f99d4c09e'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'

data=urllib.parse.urlencode(data).encode('utf-8')

response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')

result=json.loads(html)

# print(result['translateResult'][0][0]['src'])
print(result['translateResult'][0][0]['tgt'])