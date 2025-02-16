from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os
import csv
import time

#preapare the web driver in order to acsess
path = r"C:\msedgedriver.exe"
service = Service(path)
driver = webdriver.Edge(service=service)

#open the needed page to scape and wait to load
driver.get("https://961souq.com/collections/laptops")
driver.maximize_window()
driver.implicitly_wait(10)
count_page = 1

#opening a new file and checking if it exists
file_exists = os.path.isfile("store_laptop_info.csv")
with open('store_laptop_info.csv', mode='a', newline='', encoding='utf-8') as file:
    
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(['name', 'discount_price', 'price', 'description', 'discount %'])
    
    #using a infinte loop to check each page
    while True:   
        count_row = 1
        
        # using another infinte loop to check each row and extract the wanted data  
        while True:
            #put the code in a try except block to understand errors
            try:
 
                lap_name = driver.find_element("xpath", f'//*[@id="main-collection-product-grid"]/li[{count_row}]/div/div/div[2]/div[1]/a/span').text          
                lap_dis_price = driver.find_element("xpath", f'//*[@id="main-collection-product-grid"]/li[{count_row}]/div/div/div[2]/div[1]/div[2]/div/dl/div[2]/dd[2]/span').text    
                lap_price = driver.find_element("xpath", f'//*[@id="main-collection-product-grid"]/li[{count_row}]/div/div/div[2]/div[1]/div[2]/div/dl/div[2]/dd[1]/s').text
                description = driver.find_element("xpath", f'//*[@id="main-collection-product-grid"]/li[{count_row}]/div/div/div[2]/div[1]/div[1]').text
                discount = driver.find_element("xpath", f'//*[@id="main-collection-product-grid"]/li[{count_row}]/div/div/div[1]/div/div/span').text
                
                #writing to file and use counter to get to the next row
                writer.writerow([lap_name, lap_dis_price, lap_price, description, discount])
                print(count_row)
                count_row +=1                  
                time.sleep(0.25)
                
                #breaks and go to next page
            except Exception as e:
                print(f'Exception: {e}')
                break
        
        #finds the next button to get to next page and use counter plus waiting to lad the data of the page to load
        try:
            
            link2 = driver.find_element("class name", "pagination__item--next")
            link2.click()
            driver.maximize_window()            
            count_page += 1
            print(f'Page: {count_page}')
            driver.implicitly_wait(10)
            time.sleep(5)
        
        #brak when pages end
        except Exception as e:
            print("no more pages")
            print(f'Exception: {e}')
            break
    
driver.close()
print("Done! :)")