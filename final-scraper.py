# import cloudscraper
# import json
# from bs4 import BeautifulSoup

# url = 'https://www.kaina24.lt/p/google-pixel-8-pro/'

# scraper = cloudscraper.create_scraper()

# response = scraper.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     title = soup.find('h1')
#     print('Scraped data:')
#     scraped_data = []
#     unique_products = set()

#     for row in soup.find_all('tr'):
#         cols = row.find_all('td')
#         cols = [ele.text.strip() for ele in cols if ele.text.strip()]

#         if len(cols) == 3:
#             product_name = cols[0]
#             price = cols[1]
#             shop_anchor = row.find('a', href=True)
#             shop_url = shop_anchor['href'] if shop_anchor else "N/A"
#             product_tuple = (product_name, price, shop_url)

#             if product_tuple not in unique_products:
#                 unique_products.add(product_tuple)
#                 scraped_data.append({
#                     "product_name": product_name,
#                     "price": price,
#                     "shop_url": shop_url
#                 })
#                 scraped_data.sort(key=lambda x: float(x['price'].split()[0]))
#             unique_data = []
#             for item in scraped_data:
#                 if item not in unique_data:
#                     unique_data.append(item)
#             scraped_data = unique_data

#     json_output = json.dumps(scraped_data, ensure_ascii=False, indent=4)
#     print(json_output)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")


import cloudscraper
import json
from bs4 import BeautifulSoup

url = 'https://www.kaina24.lt/p/google-pixel-8-pro/'

scraper = cloudscraper.create_scraper()

response = scraper.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1')
    scraped_data = []
    unique_products = set()

    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele.text.strip()]

        if len(cols) == 3:
            product_name = cols[0]
            price = cols[1]
            shop_anchor = row.find('a', href=True)
            shop_url = shop_anchor['href'] if shop_anchor else "N/A"
            product_tuple = (product_name, price, shop_url)

            price_value = float(price.split()[0])
            if price_value <= 650:
                if product_tuple not in unique_products:
                    unique_products.add(product_tuple)
                    scraped_data.append({
                        "product_name": product_name,
                        "price": price,
                        "shop_url": shop_url
                    })
                    scraped_data.sort(key=lambda x: float(x['price'].split()[0]))
            unique_data = []
            for item in scraped_data:
                if item not in unique_data:
                    unique_data.append(item)
            scraped_data = unique_data

    json_output = json.dumps(scraped_data, ensure_ascii=False, indent=4)
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")