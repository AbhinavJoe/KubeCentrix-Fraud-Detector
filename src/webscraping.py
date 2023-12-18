from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import re
from webdriver_manager.chrome import ChromeDriverManager

# Obtain the version of ChromeDriver compatible with the browser being used.
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Which website to scrape
val = input("Enter a url:")

wait = WebDriverWait(driver, 10)

driver.get(val)


get_url = driver.current_url
wait.until(EC.url_to_be(val))


if get_url == val:
    page_source = driver.page_source

# Use BeautifulSoup to parse the HTML scraped from the webpage.
soup = BeautifulSoup(page_source,features="html.parser")

# Parse the soup for User Input Keywords.
multiple=input("Would you like to enter multiple keywords?(Y/N)")

if multiple == "Y":
    keywords=[]
    matches=[]
    len_match=[]
    num_keyword=input("How many keywords would you like to enter?")
    count=int(num_keyword)
while count != 0:
    keyword=input("Enter a keyword to find instances of in the article:")
    keywords.append(keyword)
    match=soup.body.find_all(string=re.compile(keyword))
    matches.append(match)
    len_match.append(len(match))
    count -= 1
    df=pd.DataFrame({"Keyword":pd.Series(keywords),"Number of Matches": pd.Series(len_match),"Matches":pd.Series(matches)})
elif multiple == "N":
    keyword=input("Enter a keyword to find instances of in the article:")
    matches = soup.body.find_all(string=re.compile(keyword))
    len_match = len(matches)
    df=pd.DataFrame({"Keyword":pd.Series(keyword),"Number of Matches": pd.Series(len_match), "Matches":pd.Series(matches)})
else:
    print("Error, invalid character entered.")

# Store the data collected into an excel file.
df.to_excel("Keywords.xlsx", index=False)

driver.quit()