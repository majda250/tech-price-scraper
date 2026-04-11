#libraries importation

import requests
from bs4 import beautifulsoup 
from datetime import datetime
from config import URL_TEMPLATE,MODELES,SELECTORS,HEADERS

#genrates all products URLs from the template and models list 
def build_urls():
	PRODUCT_URL=[]
	for x in MODELES:
		url = URL_TEMPLATE.format(model=x)
		PRODUCT_URL.append(url)
	return PRODUCT_URL


#Download HTML content from given URL. Returns (html,error)
def fetch_page(url):
	try:
		response=requests.get(url, headers= HEADERS , timeout=10)
		if response.status_code == 200 :
			html=response.text
			return html , NONE
		else :
			return NONE , f"HTTP {response.status_code}"

	except requests.exceptions.RequestException as e :
		return NONE , str(e)



#Extracts product data (name,price,guarantee,storage) from HTML using CSS selectors
def parse_product(html,model):
	soup=BeautifulSoup(html,'html.parser') #BeautifulSoup take the content to parse + the parser

	product_name=soup.selct_one(SELECTORS["product_name"])
	price=soup.selcet_one(SELECTORS["price"])
	guarantee=soup.select_one(SELECTORS["guarantee"])
	storage=soup.select_one(SELECTORS["storage_capacity"])


	return {"product_name":product_name,"product_price":price, "product_guarantee":guarantee, "product_storage":storage}











#Loops through all models,fetches and parses each page collects results with timestamps





















#save scrapped data to CSV file (appends if exists,cretes header if empty








#Orchestrates the Whole pipeline: scrape -> save -> print summary








