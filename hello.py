import feedparser
import requests
import re
from bs4 import BeautifulSoup

dis = requests.get(" https://www.thehindu.com/")
dis_soup = BeautifulSoup(dis.content, 'html5lib')
dis_headings = dis_soup.find_all('div',{'class':'story-card'})

#print(dis_headings)
for article in dis_headings:
    main = article.find_all('a')[0]    
    main = str(main)
    link = re.findall(r'href=\"(.*?)\"', main)
    imagelink = article.find_all('img')[0]
    imagelink = str(imagelink)
    image = re.findall(r'data-src-template=\"(.*?)\"', main)
    
    title = article.find_all('h2')
    
    title = str(title)

    title1 = title.split("\n")
    #news_title =  dis_soup.findAll("h2")[0].renderContents()
    #print(title)
    ntitle = re.findall(r'IST>(.*?)</"a',title)
    #title = title.split()
    print(title1[-3])
    #print(main)
    #print(link)

      
