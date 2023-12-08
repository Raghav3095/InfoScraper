import re
import requests
import pandas as pd  
from urllib.request import urlopen
from requests_html import HTMLSession

'''
url of the page to scrape
'''
url = "http://math.iisc.ac.in/faculty.html"
# page = urlopen(url)
# html_code = page.read().decode("utf-8")

'''
regex for email findall(pattern, source) if the method with response.html.find() does not work
'''
# links = re.findall("mailto:.*?.in", html_code)
# links_list = [s.replace('mailto:', '') for s in links]
# print(link_replace)

try:
    session = HTMLSession()
    response = session.get(url)
except requests.exceptions.RequestException as e:
    print(e)

'''
.class or #id selector to access specific sections followd by the tag to access (h4/p/small etc.)
'''

name = response.html.find('.table .col-md-10 a')
# lname = response.html.find('#cn-team-container-7fba6628 .family-name')
# desig = response.html.find('#cn-team-container-7fba6628 .title.notranslate')
# qual = response.html.find('.card_item_wrp.section-spacing.section-spacing-paddb-65 small')
email = response.html.find('.table .col-md-10 div:nth-child(4) > div:nth-child(3)')

name_list, lname_list, desig_list, email_list = [], [], [], []

for i in range(len(name)):
    name_list.append(name[i].text)
    # lname_list.append(lname[i].text)
    # desig_list.append(desig[i].text)
    email_list.append(email[i].text)

'''
Checking data recieved
'''
# print(name_list)
# print(len(name_list), len(lname_list), len(desig_list), len(email_list))

'''
Cleaning data according to requirements
'''
email_list = [s.replace('UserID : ', '') for s in email_list]
email_list = [s + '@iisc.ac.in' for s in email_list]
# print(name_list[:5], email_list[:5])
# links_list.append('')

'''
Writing to csv file
'''
dict = {
    'FName': name_list,
    # 'LName': lname_list,
    # 'Designation': desig_list,
    'Email': email_list}  
       
df = pd.DataFrame(dict) 
    
'''
saving the dataframe
''' 
df.to_csv('Ashoka.csv')