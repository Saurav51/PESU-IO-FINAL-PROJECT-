# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

# Set the URL you want to webscrape from
url = 'https://karki23.github.io/Weather-Data/assignment.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

# To download the whole data set, let's do a for loop through all a tags
for i in range(0,len(soup.findAll('a'))): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    #print(one_a_tag)
    link = one_a_tag['href']
    #print(link)
    download_url = 'https://karki23.github.io/Weather-Data/'+ link
    #print(download_url)
    #urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
    response=requests.get(download_url)
    info=BeautifulSoup(response.text,"html.parser")
    #print(info)
    table=info.select_one('table')
    #print(table)
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        #print(columns)
        output_row = []
        for column in columns:
            #print(column.text)
            output_row.append(column.text)
        output_rows.append(output_row)
    
    with open('dataset.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        #for i in output_rows:
        writer.writerows(output_rows)

    time.sleep(1) #pause the code for a sec
    
csvfile.close()
"""
Created on Wed Jul 17 15:13:22 2019

@author: Saurav Nayak
"""

