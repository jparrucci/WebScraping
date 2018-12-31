import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    exec_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **exec_path, headless=False)


url1 = 'https://mars.nasa.gov/news/'
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
url3 = 'https://twitter.com/marswxreport?lang=en'
url4 = 'http://space-facts.com/mars/'
url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


browser = init_browser()
browser.visit(url1)
news_title = browser.find_by_css('.content_title').first.text
news_p = browser.find_by_css('.article_teaser_body').first.text
print(news_title, "\n" + news_p)

def scrape_info():
    browser = init_browser()

    #Visit https://mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    #soup = bs(html, "html.parser")

    # Get the average temps
    news_title = browser.find_by_css('.content_title').first.text
    news_p = news_p = browser.find_by_css

    print(news_title, "\n" + news_p)


    print("hello")

    # Store data in a dictionary
    #costa_data = {
        #"sloth_img": sloth_img,
       # "min_temp": min_temp,
        #"max_temp": max_temp
    #}

    # Close the browser after scraping
    #browser.quit()

    # Return results
    return costa_data
