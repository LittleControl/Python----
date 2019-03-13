import urllib.request
import urllib.parse
import re


url=str(input("Please input the website for picures in Miyuansu:\n"))
# url="http://www.51yuansu.com/subject/18-1.html"
req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
html=urllib.request.urlopen(req)
html=html.read().decode("utf-8")
print(html)
p=r'src="(http://pic.51yuansu.com/[^"]+/unsharp/true/compress/true)"'
srclist=re.findall(p,html)
count=1
print(srclist)
for each in srclist:
	print(each)
	filename=str(count)
	count+=1
	urllib.request.urlretrieve(each,filename,None)

print('Finshed!')	
