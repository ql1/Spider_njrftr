import requests
import re
import time
from bs4 import BeautifulSoup
import urllib.request 

# import io  
# import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')  

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'Hm_lvt_87000df3ff8fbd36b40dd3cb90ea084c=1523060582,1523080345,1523162660,1523259663; yeuaulastsearchtime=1523260052; fikker-ZsME-l1vU=xL4oBSXsLWNK4CbmnQ4AT1Zk8EKEDOt9; yeuauecookieinforecord=%2C1287-23753%2C1287-23775%2C1287-23761%2C1287-23782%2C938-20548%2C914-17308%2C900-16976%2C813-16529%2C868-16210%2C822-14061%2C808-13902%2C760-12224%2C760-12223%2C760-12222%2C751-11822%2C745-11683%2C745-20839%2C745-11687%2C600-8108%2C830-19853%2C918-17331%2C918-17325%2C591-7844%2C1313-25927%2C1320-25940%2C; Hm_lpvt_87000df3ff8fbd36b40dd3cb90ea084c=1523270427; yeuauecookieclassrecord=%2C1287%2C822%2C808%2C760%2C751%2C745%2C600%2C40%2C25%2C1438%2C29%2C154%2C1434%2C',
'Host': 'nanrenvip.org',
'If-Modified-Since': 'Mon, 09 Apr 2018 08:52:41 GMT',
'If-None-Match': 'W/"5acb29d9-5284"',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

def log(*args,is_file = 1,**kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    # print(args,kwargs,dt)
    if is_file == 1:
        with open('log.gua.txt', 'a', encoding='utf-8') as f:
            print(dt, *args, file=f, **kwargs)
    elif is_file == 2:
        with open('file_av.txt', 'a', encoding='utf-8') as f:
            print(dt, *args, file=f, **kwargs)

def get_girls_inf(url):
	response = requests.get(url,headers=headers,timeout=2)
	# log('**debug_utf-8',response)
	# log(type(response))
	response.encoding = 'utf-8'
	# log(isinstance(response,unicode))
	# response = response.encode('utf-8')
	html = response.text
	soup=BeautifulSoup(html,'html.parser')
	# print(type(result))
	# result = result.encode()
	# log('girlinf***',result)
	# print (result)
	# reg = r'<a href="/mrhql/2018/SSNI-192.html" target="_blank"><img data-original="//nanrenvip.org/uploads/2018/04/ssni192pl-small.jpg" src="//nanrenvip.org/uploads/2018/04/ssni192pl-small.jpg" style="display: inline;"></a>'
	# reg = r'<a href="(.*?)" target="_blank"><img data-original=".*?'
	# matched = re.findall(reg,result)
	results = []
	reg = r'<a href="(.*?)">下一页</a>' 
	index = re.findall(reg,html)
	result = soup.find(attrs = {'class' :'list_img'})
	if result:
		result = result.encode().decode('utf-8')
		reg = r'<a href="(.*?)" target="_blank"><img data-original=".*?'
		result = re.findall(reg,result)
	
	while index:
		get_girls_inf(index)
	results.append(result)	
		# <a href="/mrhql/2018/SSNI-192.html" target="_blank"><img data-original="//nanrenvip.org/uploads/2018/04/ssni192pl-small.jpg" src="//nanrenvip.org/uploads/2018/04/ssni192pl-small.jpg" style="display: inline;"></a>
	return (results)


def get_av_inf(url):
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    soup=BeautifulSoup(html,'html.parser')
    result = soup.find_all('p')
    return result
# # soup = soup.decode('utf-8')
#     result1 = soup.find_all(attrs = {'class' :'artCon'})
#     # result2 = soup.find_all(attrs = {'class' :'artCon'})
#     reg = r'<p>(.*?)</p>'
#     result2 = re.findall(reg, html)
#     return result1,result2
    # response = requests.get(url,headers=headers)
    # response.encoding = 'utf-8'
    # result = response.text
    # # print (result)
    # # log(result)
    
    # reg1 = r'<strong>(.*?)</p>'
    # reg2 = r'<p>(.*?)</p>'

    # <div class="artCon"><p>日本AV女优桥本有菜参演的作品番号SNIS-854，该片（
    #             <strong>チ●ポ大好き超即尺おしゃぶりメイド 橋本ありな</strong>）时长120分钟，本番号作品分类定义于：口交,美少女,女佣，正式发片日期是2017-02-19</p>
    #           <div class="con"><img data-original="//nanrenvip.org/uploads/2017/04/snis854pl.jpg" alt="チ●ポ大好き超即尺おしゃぶりメイド 橋本ありな"/></div></div>

    # <li><a href="youyueanxia/"><img data-original="//nanrenvip.org/d/file/2017/04/099a55bb4d54b38ece221b1416d7d509.jpg" /><br />悠月安夏</a></li>
    # # pattern = re.compile(reg1)
    # matched1 = re.findall(reg1,result)
    # matched2 = re.findall(reg2,result)
    # return (matched1,matched2)



def get_main():
    response = requests.get('http://nanrenvip.org/find.html')
    response.encoding = 'utf-8'
    result = response.text
    # print (result)
    reg = r'<li><a href="(.*?)"><img data-original="//nanrenvip.org/d/(.*?)" /><br />(.*?)</a></li>'
    # <li><a href="youyueanxia/"><img data-original="//nanrenvip.org/d/file/2017/04/099a55bb4d54b38ece221b1416d7d509.jpg" /><br />悠月安夏</a></li>
    matched = re.findall(reg,result)
    return (matched)


def compile_url(name):
	new_url = 'http://nanrenvip.org/' + name
	return new_url

def compile_url_fu(name):
	new_url = 'http://nanrenvip.org' + name
	return new_url	

# print (get_main())
match = get_main()
# log('match',match)
for i in match:
	girl_list = compile_url(i[0])
	# log(girl_list)
	# log('girl',girl_list)
	girls_inf = get_girls_inf(girl_list)
	# log(girls_inf)
	if girls_inf:
		for j in girls_inf:
			name = j
			log(name)
			av_list = compile_url(name)
			av_inf = get_av_inf(av_list)
			if av_inf:
				# log(av_inf)
		# log(av_list)
		# log(name,is_file = 2)
		# av_inf = get_av_inf(av_list)
		# if av_inf:
		# 	log(av_inf,is_file = 2)
print('-----------------爬虫已结束')




