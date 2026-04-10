#!/usr/bin/env python3

# Template de l'URL (le {modele} sera remplacé automatiquement)

URL_TEMPLATE = "https://uno.ma/{modele}-maroc"

# Liste des modèles à scraper

MODELES = [

    "iphone-17-pro",

    "iphone-17-pro-max",

    "iphone-air",

    "iphone-17",

    "iphone-16e",

    "iphone-15",

    "ipad-pro-m5-2025-13-pouces",

    "ipad-pro-m5-2025-11-pouces",

    "ipad-a16-2025-11-pouces",

    "ipad-air-m3-2025-13-inch",

    "ipad-air-m3-2025",

    "ipad-mini-7-maroc",

    "apple-watch-ultra-3-gps-cellular-49-mm",

    "apple-watch-series-11-gps-aluminium",

    "apple-watch-se-3-gps-aluminium",

    "airpods-pro-3-avec-boitier-de-charge-magsafe-usb-c",

    "airpods4"

]

# Sélecteurs CSS (identiques pour tous)

SELECTORS = {

    "product_name": "span.base",  

    "price": "span.price",  

    "guarantee": "icare-text h4",

    "storage_capacity": "span.swatch-attribute-selected-option",

}


HEADERS = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}
