from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib2to3.pgen2 import driver
from time import sleep
from selenium.webdriver.common.by import By
import json
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions


DRIVER_PATH = 'C:\chromedriver.exe'
current_page = 0
turn_it = True
all_journals = list()





while (turn_it):
    dico_journal = {}
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    web_site = "https://dl.acm.org/action/doSearch?AllField=Blockchain&expand=all&ConceptID=118230&startPage=" + \
        str(current_page)+"&pageSize=50"
    driver.get(web_site)
    sleep(4)
    # journals = driver.find_elements(By.CSS_SELECTOR, "div.issue-item.issue-item--search.clearfix")
    journals = driver.find_elements(By.CLASS_NAME,'issue-item__title')
    # Title = journals.find_elements(By.CSS_SELECTOR,'span.hlFld-Title')

    if journals == []:
        turn_it = False

    # print(journals)
    enf_of_recherche = False

    # for journal in journals:
    for index, val in enumerate (journals):
        journals = driver.find_elements(By.CLASS_NAME,'issue-item__title')
        Title = journals[index].find_element(By.CSS_SELECTOR,'span.hlFld-Title')
        url = Title.find_element(By.XPATH, './a[1]').get_attribute('href')
        

        
        dico_journal = url
        
        #this list contains all our data
        all_journals.append(dico_journal)

    print(current_page)
        
    driver.close
    # if(current_page == 0):
    #     turn_it = False
    current_page += 1
    
    if(dico_journal == {}):
        turn_it = False


with open("urls.json", "w") as write_file:
    # convert the list into a json file
    json.dump(all_journals, write_file, indent=4)

driver.close()