from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    # print(job)
for job in jobs:
    Published_Date=job.find('span',class_='sim-posted').span.text
    if 'few' in Published_Date:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_='srp-skills')
        more_info=job.header.h2.a
        print('---------')


        print(f'Commpany Name: {company_name.strip()}')
        print(f'Skills: {skills}')
        print(f'Published Date: {Published_Date}')
        print(f'Published Date: {more_info}')