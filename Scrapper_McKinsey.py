from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import PyPDF2
import os
import io

html = urlopen("https://www.mckinsey.com/industries/financial-services/our-insights")
# html = urlopen( "http://www.pythonscraping.com/exercises/exercise1.html")
# html = urlopen( "https://www.investopedia.com/terms/e/equity.asp")

soup = BeautifulSoup(html.read(), features="html.parser");
# soup.originalEncoding

print("********************************************************** PRETTIFY **********************************************************")
print(soup.prettify())

#
# import lxml.html
# t = lxml.html.parse("https://www.businessinsider.com/clusterstock")
# print ('tìtulos:',t.find(".//title").text)

print("********************************************************** TITLE  **********************************************************")
print('soup title:', soup.title.string)

print("*" * 50, "CLASSS: OraLink", "*" * 50)
nameList = soup.findAll("a", {"class":"item-title-link"})
print(nameList)


count=0
for link in soup.findAll("a", {"class":"item-title-link"},href=re.compile("(/our-insights/)((?!:).)*$")):     #si se necesita lo referente a fondos e inversión, descomentar esta y comentar las otras
    if 'href' in link.attrs:
        auxi= link.attrs['href']
        print("-",auxi)
        count=count+1
        base_url = "https://www.mckinsey.com/"
        comp= base_url+auxi
       #request_href = requests.get(base_url + auxi)
       #print (request_href)
        print(comp)


print("******************************************************* NUMBER OF DOCUMENTS ********************************************************")
print('Número total documentos', count)

with open('mckinsey.txt', 'w') as f:  # Write titles to txt file
    for name in nameList:
        auxi = name.get_text()
        #print("-", name.get_text())
        f.write("-"*85)
        f.write(name.get_text())
        #f.write("\n")

        # print("\n")


