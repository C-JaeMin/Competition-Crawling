#Make by CjaeMs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

#공모전 이름에 들어간것중 파일이름이 될수없는 문자들 변환
def change(compName):
    compName = compName.replace('/','&')
    compName = compName.replace(':','|')
    compName = compName.replace('*','')
    compName = compName.replace('?','')
    compName = compName.replace('<','[')
    compName = compName.replace('>',']')
    compName = compName.replace('|','')
    return compName

#사이트에서 자동화프로그램을 막는 보안처리한경우 이를 우회하기 위한 구문
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#background에서 실행시키기위한 구문
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('headless')

#driver세팅
driver = webdriver.Chrome(options = options)
driver.get('http://www.detizen.com/contest/?Category=19&IngYn=Y')

#try except를 이용하여 list가 비어있으면 자동으로 종료되게 처리
try:
    for i in range(1,21):
        competition = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/section[2]/div/ul/li[%d]/div[1]/h4/a[1]' %i).get_attribute('href')
        driver.get(competition)
        compName = change(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/section[2]/header/h3/span[1]').text)
        compSubject = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/section[2]/div/div/ul/li[2]/pre').text
        compTerm = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/section[2]/div/div/ul/li[3]/pre').text
        compEligibility = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/section[2]/div/div/ul/li[4]/pre').text
        imgURL = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/section[2]/div/div/div[2]/div[1]/div/a").get_attribute("href")
        
        #result/detizen 폴더에 공모전이름.txt와 공모전이름.jpg 로 저장
        urllib.request.urlretrieve(imgURL, 'D:/Crawling/result/detizen/'+compName+".jpg")
        path = 'D:/Crawling/result/detizen/'+compName+'.txt'
        result = open(path,'w')
        result.write('%s\n\n%s\n\n%s\n\n%s' %(compName,compSubject,compTerm,compEligibility))
        result.close()
        driver.back()
    
except:
    print('\n\n This Site competition list is end\n\n')

driver.get('https://www.wevity.com/?c=find&s=1&gub=1&cidx=22&sp=&sw=&gbn=list&mode=ing')
try:
    for i in range(2,17):
        competition = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[3]/div/ul/li[%d]/div[1]/a' %i).get_attribute('href')
        driver.get(competition)
        compName = change(driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div/div[1]/h6').text)
        compArticle = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[4]').text
        imgURL = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/img").get_attribute("src")
        
        #result/wevity 폴더에 공모전이름.txt와 공모전이름.jpg 로 저장
        urllib.request.urlretrieve(imgURL, 'D:/Crawling/result/wevity/'+compName+".jpg")
        path = 'D:/Crawling/result/wevity/'+compName+'.txt'
        result = open(path,'w',-1,'utf-8')
        result.write('%s\n\n%s' %(compName,compArticle))
        result.close()
        driver.back()
    driver.quit()
    print("\n\n Competition Crawling End \n\n")

except:
    print('\n\n This Site competition list is end\n\n')
    driver.quit()
    result.close()