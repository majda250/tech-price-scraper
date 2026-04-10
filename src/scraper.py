#libraries importation

import requests
from bs4 import beautifulsoup 
from datetime import datetime
from config import URL_TEMPLATE,MODELES,SELECTORS,HEADERS

#importing page's html 

def build_urls():
	PRODUCT_URL=[]
	for x in MODELES:
		url = URL_TEMPLATE.format(model=x)
		PRODUCT_URL.append(url)
	return PRODUCT_URL


def fetch_page(url):
	try:
		response=requests.get(url, headers= HEADERS , timeout=10)
	except:
		print("ERROR")	
