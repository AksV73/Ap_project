import feedparser
import requests
import re
from bs4 import BeautifulSoup

dis = requests.get(" https://www.thehindu.com/")
dis_soup = BeautifulSoup(dis.content, 'html5lib')
dis_headings = dis_soup.find_all('div',{'class':'story-card'})
news_title = []
news_images = []
news_url = []
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
    #print(len(title1))
    link = str(link)
    print(link[2:-3])
    image = str(image)
    print(image[2:-2])
    #title = title.split()
    if len(title1) != 1:
        news_title.append(title1[2])
    news_images.append(image)
    news_url.append(link)
    #print(main)
    #print(link)


print("The titles are:")
#print(news_title)
print("The urls are:")
#print(news_url)
print("The images are:")
#print(news_images)
        
