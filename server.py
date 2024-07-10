from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode

def get_price(product_name):
    proxy_url = "http://localhost:5000/proxy?url="  # Proxy server URL
    amazon_url_base = "https://www.amazon.in/s?"
    flipkart_url_base = "https://www.flipkart.com/search?"
    croma_url_base = "https://www.croma.com/search/?text="

    # Convert the product name to a URL
    query = urlencode({"q": product_name})
    query1 = urlencode({"k": product_name})
    amazon_url = f"{amazon_url_base}{query1}"
    flipkart_url = f"{flipkart_url_base}{query}"
    croma_url = f"{croma_url_base}{query}"

    # Define the price variables
    amazon_price = None
    flipkart_price = None
    croma_price = None

    # Scrape the prices from the web pages
    for url in [amazon_url, flipkart_url, croma_url]:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"Scraping: {url}")
        if "amazon" in url:
            # Find the parent container for each product listing
            product_containers = soup.find_all("div", class_="s-result-item")
            for container in product_containers:
                price_elem = container.find("span", class_="a-price-whole")
                if price_elem:
                    amazon_price = price_elem.text.strip()
                    break  # Stop searching once the price is found
            if not amazon_price:
                amazon_price = "Price not found"
            print(f"Amazon Price: {amazon_price}")
        elif "flipkart" in url:
            flipkart_price_elem = soup.find("div", {"class": "Nx9bqj _4b5DiR"})
            flipkart_price = flipkart_price_elem.text.strip() if flipkart_price_elem else "Price not found"
            print(f"Flipkart Price: {flipkart_price}")
        elif "croma" in url:
            croma_price_elem = soup.find("div", {"class": "product_price"})
            croma_price = croma_price_elem.text.strip() if croma_price_elem else "Price not found"
            print(f"Croma Price: {croma_price}")

    # Return the prices
    return amazon_price, flipkart_price, croma_price 

product_name = "Your Product Name"
amazon_price, flipkart_price, croma_price = get_price(product_name)
print("Amazon Price:", amazon_price)
print("Flipkart Price:", flipkart_price)
print("Croma Price:", croma_price)
