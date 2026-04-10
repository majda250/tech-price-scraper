#libraries importation

import requests
from bs4 import beautifulsoup 
from datetime import datetime
from config import URL_TEMPLATE,MODELES,SELECTORS,HEADERS

#importing page's html 

def build_urls():
	PRODUCT_URL=[]
	for x in MODELES:
		PRODUCT_URL.append(URL_TEMPLATE.format(model=x))
	return PRODUCT_URL


def fetch_page():
	response=requests.get(PRODUCT_URL

