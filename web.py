from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_starshttps://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome("C:\Users\YASHRAJ DIXIT\OneDrive\Desktop\Flask\chromedriver")
browser.get = (START_URL)

time.sleep(12)

def scrape():
    headers = ["name","distance","mass","radius"]
    planet_data = []

    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,'html.parser')
       
        for ul_tag in soup.find_all('ul',attrs={'class','expoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp_list = []
            for index , li_tag in enumerate(li_tags):
                if index == 0:

                     temp_list.append(li_tag.find_all('a')[0].contents[0] )
                else:

                     try:
                         temp_list.append(li_tag.contents[0])
                     except:
                         temp_list.append('')

            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id='primary_coloum']/footer/div/div/div/nav/span[2]/a').click()
    with open('scrapper_2.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(planet_data)

scrape()

                        

            







        
