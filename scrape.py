'''This program was used to scrape the tomato data from the website, 
convert the data to a dictionary format,
and save to a json file (tomato_data.json)'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.by import By
import json

# open web scraping driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://en.wikipedia.org/wiki/List_of_tomato_cultivars') 

# get tomato table header 
thead = driver.find_element(By.TAG_NAME, 'thead')
header = thead.text.split()

# get tomato data
td_tags = driver.find_elements(By.TAG_NAME, 'td')
tomato_list = []
for td in td_tags:
    tomato_list.append(td.text)

# create a list of dict, insert dict values (tomato variables) for each tomato
json_list = []
i = 1
while i < len(tomato_list):
    tomato_dict = {}
    tomato_dict['Name'] = tomato_list[i]
    tomato_dict['Color'] = tomato_list[i+1]
    tomato_dict['Maturity'] = tomato_list[i+2]
    tomato_dict['Size'] = tomato_list[i+4]
    tomato_dict['Shape'] = tomato_list[i+5]
    tomato_dict['MoreInfo'] = tomato_list[i+10]
    json_list.append(tomato_dict)
    i += 13

# save data to json
with open('tomato_data.json', 'w') as json_file:
  json.dump(json_list, json_file)

# close web scraping driver
driver.quit()

