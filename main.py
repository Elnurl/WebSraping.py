import time

from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content=html_file.read()
    #print(content)

    soup=BeautifulSoup(content,'lxml')
   # print(soup.prettify())
    tags=soup.find('h1')
   # print(tags)
    tags1=soup.find_all('li')
   # print(tags1)
   # for course in tags1:
        #print(course.text)
    course_cards=soup.find_all('div',class_='card')
    #print(course_cards)
    courese_first_li=soup.find_all('li',class_="li2")
  #  print(courese_first_li)
    for course in  course_cards:
      #  print(course.h1)
      course_name=course.h1
     # print(course_name.text)
      #print(course.h1)
#++++++++++++++++++++++++++++++++++++++++++++++++++++

import requests

html_text=requests.get('https://smartjob.az/vacancies?_token=HO7JErdqlf43lLQ3R1uTv3GZ0xxzx7ecKCjkTACd&search=python').text
#print(html_text)
soup=BeautifulSoup(html_text,'lxml')
job=soup.find('div',class_="brows-job-list")
#print(job)
name=job.find('div',class_="brows-job-position").text.replace(' ','')

#print(name)
skill= job.find('div',class_="hide-on-pc").text.replace(' ','')
#print(skill)
#print(f'''
#company Name:{
#name
#}
#Salary:{
#skill
#}
#''')

date=job.find('div',class_="created-date").text
#print(date)
import time
jobs=soup.find_all('div',class_='brows-job-list')
print('jobs finding out')
time.sleep(3)
for job in jobs:

    names = job.find('div', class_="brows-job-position").text.replace(' ', '')
    print(names)
    skills = job.find('div', class_="hide-on-pc").text.replace(' ', '')
    print(skills)
    print(f'''
       company Name:{names}Salary:{skills.strip()} ''')
    dates = job.find('div', class_="created-date").text
    print(dates.strip())


