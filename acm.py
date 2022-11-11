from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib2to3.pgen2 import driver
from time import sleep
from selenium.webdriver.common.by import By
import json
from selenium.webdriver import ActionChains

DRIVER_PATH = 'C:\chromedriver.exe'
current_page = 0
turn_it = True
all_journals = list()



while (turn_it):
    dico_journal = {}
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    web_site = "https://dl.acm.org/action/doSearch?AllField=Cybersecurity&expand=all&ConceptID=118230&startPage=" + \
        str(current_page)+"&pageSize=20"
    driver.get(web_site)
    sleep(4)
    journals = driver.find_elements(By.CSS_SELECTOR, "div.issue-item.issue-item--search.clearfix")

    if journals == []:
        turn_it = False

    # print(journals)
    enf_of_recherche = False

    for journal in journals:

        def hasxpath(xpath):
            try:
                journal.find_element(By.XPATH, xpath)
                return True
            except:
                return False

        title = journal.find_element(By.CSS_SELECTOR,'span.hlFld-Title').text

        journal_info = journal.find_element(By.CSS_SELECTOR, "div.issue-item__detail")

        source = journal_info.find_element(By.XPATH, "./a[1]/span[1]").text

        date = journal_info.find_element(By.XPATH, "./span[1]/span[1]").text

        type = journal.find_element(By.XPATH, "./div[1]/div[1]").text

        access_type = journal.find_element(By.XPATH, "./div[1]/div[2]").text

        if hasxpath('./div[2]/div[1]/ul[1]') == True:
            authors = journal.find_element(By.XPATH, "./div[2]/div[1]/ul[1]").text
        else:
            authors=''
        


        
        dico_journal = {"Title":title, "Source":source, "Date":date, "Type": type, "Access_type": access_type, "Authors":authors}

        #this list contains all our data
        all_journals.append(dico_journal)

    print(current_page)
        
    driver.close
    # if(current_page == 0):
    #     turn_it = False
    current_page += 1
    
    if(dico_journal == {}):
        turn_it = False


with open("data.json", "w") as write_file:
    # convert the list into a json file
    json.dump(all_journals, write_file, indent=4)

driver.close()