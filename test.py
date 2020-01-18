##-*- coding:utf-8 -*-
import sys
import imp
imp.reload(sys)
#sys.setdefaultencoding("gbk")
import codecs
import os

from re import findall
import requests
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup 


def modifyip(tfile,sstr,rstr):

    try:

        lines=open(tfile,'r',encoding="utf8").readlines()

        flen=len(lines)-1

        for i in range(flen):

            if sstr in lines[i]:

                lines[i]=lines[i].replace(sstr,rstr)

        open(tfile,'w', encoding="utf8").writelines(lines)

        

    except Exception as e:

        print(e)

try:
    os.remove('p1.htm') 
    os.remove('p2.htm') 
except:
    pass


url = r'''
https://mp.weixin.qq.com/s?__biz=MzUwOTg1OTU5MA==&mid=2247490944&idx=1&sn=2eca8e5867dde60f7923fe68600a9092&exportkey=Af7%2BqejU8j%2F%2F5Y313OSp2QQ%3D&pass_ticket=b44rzo%2Fa8JvBjtn26phN%2BF8dMxqAdwftx8kdtrPktBFvPXVMsIN6s7f5Bpfjdh9F
'''
content = urlopen(url).read()


dirPath = r"C:\Users\lilli\Desktop\baobao_python"
fileList = os.listdir(dirPath)
for fileName in fileList:
    if (fileName == 'test.py') or (fileName[0] == '.') or ('~' in fileName) or fileName[-2:] == 'py':
        continue
    os.remove(dirPath+"/"+fileName)


with open('p.html', 'w') as file1:
    pass
f1 = open('p.htm','wb')
f1.write(content)
f1.close() 
#f2=file('pic.txt','wb')

import os 
import math       
altxt = open('p.htm', 'r', encoding="utf8").read()
pattern = '<script(.+?)</script>'
#out = re.sub(pattern,' ', altxt)
listpp=re.split(r'<script|</script>|<style>|</style>',altxt)
f1 = open('p1.htm','a+', encoding = 'utf8')
soup = BeautifulSoup(content, "lxml")
def if_script_not_needed(ele):
    if 'aliceblue' in ele.contents and 'yellowgreen' in ele.contents:
        return False
    return True
[x.extract() for x in soup.findAll(['script']) if if_script_not_needed(x)]
f1.write(str(soup))
     
f1.close()

altxt = open('p1.htm','r', encoding='utf8', errors = 'ignore').read()
pattern = '<script(.+?)</script>'
#out = re.sub(pattern,' ', altxt)
listpp=re.split(r'<|>',altxt)
f1 = open('p2.htm','a+', encoding = 'utf8', errors = 'ignore')
for i in listpp:
   print(listpp.index(i))
   if (listpp.index(i)+2)%2  == 0:
     print(i)

     f1.write(i+chr(10))
     
f1.close()

#f4=open('p2.htm','r+')
#altxt = f4.read()
#altxt =  altxt.replace('head','')
#print altxt
#f4.write(altxt)
#f4.close()

for i in range(10):

 with open('p2.htm','r+', errors = 'ignore') as f:
    t = f.read()
    t = t.replace('/head', '')
    t = t.replace('head', '')
    t = t.replace('/body', '')
    t = t.replace('body', '')
    t = t.replace('/html', '')
    t = t.replace('html', '')
    #t = t.replace('&nbsp;', '')

   #读写偏移位置移到最开始处 
    f.seek(0, 0)    
    f.write(t)



def delblankline(infile,outfile):
    infopen = open(infile,'r')
    outfopen = open(outfile,'w')
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()
    
delblankline("p2.htm","p3.txt")

pattern = ' data-src="(.+?)"'
pattern1 = ' data-src="(.+?)"'

content = open('p.htm', 'r', encoding = "utf8").read()
result = findall(pattern, content)
#print result


#content = open('p.htm').read()
#pattern1 = ' data-src="(.+?)"'
#result1 = findall(pattern1, content)
#for index, item in enumerate(result):

for index, item in enumerate(result):
    
    
    if not str(item).find('png')==-1:
         data = urlopen(str(item)).read()
         #f2.write(str(item)+'"  />'+'<img src="'+str(index)+'.png"  />')
         modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.png" ')
        
         f = open(str(index)+'.png',"wb")
         f.write(data)
         f.close() 

    if not str(item).find('jpeg')==-1:
         data = urlopen(str(item)).read()
         
         modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.jpg" ')
         
         f = open(str(index)+'.jpg',"wb")
         f.write(data)
         f.close() 

    if not str(item).find('gif')==-1:
         data = urlopen(str(item)).read()
         
         modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.gif" ')
         
         f = open(str(index)+'.gif',"wb")
         f.write(data)
         f.close()  


#with open('p1.htm', 'r', encoding="utf8", errors='ignore') as p2_file:
#    text = p2_file.read()
#text.replace(r'<head>', r'<head> <meta http-equiv="Content-Type" content="text/html; charset=gb2312">') 

#with open('p1.htm', 'w', encoding="utf8") as p2_file:
#    p2_file.write(text)



#os.remove('p1.htm') 
#os.remove('p2.htm') 




with open('p1.htm', 'r', encoding='utf8') as file1:
    text = file1.read()

#print(text)
#text = re.sub(r'<title>[\S\s]*?\/title>', "", text)
text = re.sub(r'<h2 class="rich_media_title" id="activity-name">[\S\s]*?<\/h2>', "", text)

text = text.replace(r'<p><img ', '<p style="text-align:center;"><img ')

text = text.replace(r'data-src=', 'src=')


with open('p1.htm', 'w', encoding='utf8') as file1:
    file1.write(text)

import clipboard

with open('p1.htm', 'r', encoding='utf8') as file1:
    text = file1.read()
clipboard.copy(text)
