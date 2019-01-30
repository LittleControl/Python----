import urllib.request
import json


while True:	
	text=str(input('Please input the text you want to translate,input "wq"to quit\n'))
	if text =='wq':
		break;	
	url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

	data={}
	data['i']=text
	data['form']='AUTO'
	data['to']='AUTO'
	data['smartresult']='dict'
	data['client']='fanyideskweb'
	data['salt']='15488296851070'
	data['sign']='3932a4d55a222cca27da2a590792b425'
	data['ts']='1548829685107'
	data['bv']='57ddaf41eea8c605eaf49a05203af899'
	data['doctype']='json'
	data['version']='2.1'
	data['keyfrom']='fanyi.web'
	data['action']='FY_BY_REALTIME'
	data['typoResult']='false'
	data=urllib.parse.urlencode(data).encode('utf-8')
	headers={}
	headers['User-Agent']='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'
	seq=urllib.request.Request(url,data,headers)
	response=urllib.request.urlopen(seq)
	html=response.read().decode('utf-8')
	result=json.loads(html)
	print(result['translateResult'][0][0]['tgt'])
