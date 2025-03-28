from selenium import webdriver
import os
from urllib.parse import urlparse

BASE_URL = 'https://backupns.bd.org.tw'
OUTPUT_DIR = './static_site'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_page_with_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.quit()

    page_name = urlparse(url).path.strip('/').replace('/', '_') or 'index'
    with open(os.path.join(OUTPUT_DIR, f"{page_name}.html"), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved dynamic page: {url}")

save_page_with_selenium(BASE_URL)
