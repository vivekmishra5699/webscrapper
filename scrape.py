''''from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_amazon_price(product_url):
    options = Options()
    options.headless = True

    service = Service('geckodriver.exe')  # Replace 'path/to/geckodriver' with the path to your geckodriver executable
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get(product_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole')))  # Wait for the price element to be present
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        price_element = soup.find("span", attrs={'class': 'a-price-whole'})
        if price_element:
            price = price_element.text.strip()
        else:
            price = "Could not find the price."
            print(soup.prettify())  # Print the page content for further inspection
    except Exception as e:
        print(f"An error occurred: {e}")
        price = "Error retrieving price."
    finally:
        driver.quit()  # Make sure to close the WebDriver after use

    return price

product_url = 'https://www.amazon.com/dp/B07FZ8S74R/'  # Replace with your product URL
print(get_amazon_price(product_url))'''