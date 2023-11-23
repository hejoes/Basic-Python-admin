
import requests
import json
from bs4 import BeautifulSoup

base_url = 'https://scrapeme.live/shop/page/{}'

products = []

for page_number in range(1, 12):
    
    response = requests.get(base_url.format(page_number))
    soup = BeautifulSoup(response.content, 'html.parser')

    for product in soup.select('ul.products li'):
        
        name = product.select_one('h2.woocommerce-loop-product__title')
        price = product.select_one('.woocommerce-Price-amount')
        image_url = product.select_one('img')['src']
        
        products.append({
            'Title': name.text.strip(), 
            'Price': price.text.strip().replace('\u00a3', '$'),
            'Picture href': image_url,
        })

with open('products_soup.json', 'w') as f:
    json.dump(products, f)