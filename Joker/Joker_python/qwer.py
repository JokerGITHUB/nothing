import urllib.request
import urllib.parse as parse  
import string  
print(""" 
+++++++++++++++++++++++ 
  学校：超神学院 
  专业：德玛班 
  姓名：德玛之力 
  version: python3.4 
+++++++++++++++++=++++ 
     """)  
def baidu_tieba(url, begin_page, end_page):  
    for i in range(begin_page, end_page + 1):  
        sName = 'e:/test/'+str(i).zfill(5)+'.html'  
        print('正在下载第'+str(i)+'个页面, 并保存为'+sName)
        print(url+str(i))
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }        
        request=urllib.request.Request(url+str(i),headers=headers)
        response=urllib.request.urlopen(request)        
        m = response.read() 
        with open(sName,'wb') as file:  
            file.write(m)  
        file.close()  
url = "http://www.qiushibaike.com/hot/page/"  
begin_page = 1  
end_page = 3  
baidu_tieba(url, begin_page, end_page) 
