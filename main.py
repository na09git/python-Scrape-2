from bs4 import BeautifulSoup
import requests
import time 


print('Enter your unfamiliar skill')
unfamiliar_skill=input('>')
print(f'Unfamiliar Skill: {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
        # print(job)
    for index,job in enumerate(jobs):
        Published_Date=job.find('span',class_='sim-posted').span.text
        if 'few' in Published_Date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills_tag=job.find('span',class_='srp-skills')
            more_info=job.header.h2.a['href']
          
            # Check if skills_tag is not None
            if skills_tag:
                skills = skills_tag.text.strip()
            else:
                skills = "Not listed"
                
            
            print('---------')

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Commpany Name: {company_name.strip()} \n')
                    f.write(f'Skills: {skills} \n')
                    f.write(f'Published Date: {Published_Date} \n')
                    f.write(f'More Information: {more_info}')
                
                print(f'File {index}.txt has been created')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting for {time_wait} minutes ...')
        time.sleep(time_wait * 60)