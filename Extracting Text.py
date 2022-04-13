"""Coded by Gaurav Kumar Mishra
    Email: gauravmishra892001@gmail.com"""

# Importing required libraries

import csv


from selenium import webdriver
import pandas as pd
import time
import numpy as np



# Reading the given input excel data using pandas
data=pd.read_csv('Amazon Scraping - Sheet1.csv')
id=data['id']
Asin=data['Asin']
country=data['country']


mydict=[]
for i in range(0,130):
    try:
        url="https://www.amazon."+str(country[i])+"/dp/"+str(Asin[i])

        # list.append(url)




        # # Initializing selenium webdriver
        driver = webdriver.Chrome(executable_path='C:/Users/acer/Documents/chromedriver/chromedriver.exe')

        # url='https://www.amazon.de/dp/1060694'

        driver.get(url)

        title=driver.find_element_by_id('h').text
        image=driver.find_element_by_id('d')
        src = image.get_attribute('src')
        product_dic=driver.find_element_by_id('j').text

        # l1.append(title)
        # l2.append(src)
        # l3.append(produc_dic)

        my = [title, src, product_dic]

        fields = ['TITLE','IMAGE URL','PRODUCT_DIC']

        myd = {}
        for _ in range(len(fields)):
            myd.update({fields[_]: my[_]})
        mydict.append(myd)

        # with open(filename, 'w') as csvfile:
        #     writer = csv.DictWriter(csvfile, fieldnames=fields)
        #
        #     # writing headers (field names)
        #     writer.writeheader()
        #
        #     # writing data rows
        #     writer.writerows(mydict)
        #     # Output
        #     # list=[workingFile,pos,neg,polarityScore,subjectiveScore,percentCompWords,fogIndex,
        #     #       avgSentLength,lenComplex,wordCount,syllabel,AverageWordLength,pronounInText]

        driver.close()


    except:
        print("error")

df=pd.DataFrame(mydict)

df.to_csv('gaurav.csv')





