#import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

def scrape():
	#grab news title and summary with bs
	url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	response = requests.get(url)
	soup = bs(response.text, 'lxml')

	#scrape title
	news_title = soup.find('div', class_='content_title').text

	#scrape image
	news_p = soup.find('div', class_='rollover_description_inner').text

	#grab featured image and set up splinter
	executable_path = {'executable_path': 'C:\\Webdrivers\\chromedriver.exe'}

	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url)

	#click link via splinter
	browser.click_link_by_partial_text('FULL IMAGE')

	response = requests.get(url)
	soup = bs(response.text, 'lxml')

	featured_image = soup.find('div', class_='carousel_items').article
	featured_image_url = 'https://www.jpl.nasa.gov' + featured_image.a['data-fancybox-href']

	#get weather report from twitter
	url = 'https://twitter.com/marswxreport?lang=en'
	response = requests.get(url)
	soup = bs(response.text, 'lxml')

	mars_weather = soup.find('div', class_='js-tweet-text-container').p.text

	#get mars facts in an html table
	url = 'https://space-facts.com/mars/'
	response = requests.get(url)
	soup = bs(response.text, 'lxml')

	mars_table = soup.find('table', class_='tablepress tablepress-id-mars')
	#mars_table = pd.read_html(str(mars_table))

	#get images from each hemisphere using splinter 
	#cerberus
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)

	browser.click_link_by_partial_text('Cerberus')

	url = browser.url

	response = requests.get(url)
	soup = bs(response.text, 'lxml')
	cerberus = soup.find('img', class_='wide-image')

	cerberus_image = 'https://astrogeology.usgs.gov/' + cerberus['src']

	#Schiaparelli
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)

	browser.click_link_by_partial_text('Schiaparelli')

	url = browser.url

	response = requests.get(url)
	soup = bs(response.text, 'lxml')
	schiaparelli = soup.find('img', class_='wide-image')

	schiaparelli_image = 'https://astrogeology.usgs.gov/' + schiaparelli['src']

	#Syrtis
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)

	browser.click_link_by_partial_text('Syrtis')

	url = browser.url

	response = requests.get(url)
	soup = bs(response.text, 'lxml')
	syrtis = soup.find('img', class_='wide-image')

	syrtis_image = 'https://astrogeology.usgs.gov/' + syrtis['src']

	#Valles
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)

	browser.click_link_by_partial_text('Valles')

	url = browser.url

	response = requests.get(url)
	soup = bs(response.text, 'lxml')
	valles = soup.find('img', class_='wide-image')

	valles_image = 'https://astrogeology.usgs.gov/' + valles['src']

	#convert all variables to python dictionary
	mars = {'news_title': news_title, 'news_p': news_p, 'featured_image_url': featured_image_url,
               'mars_weather': mars_weather, 'cerberus_image': cerberus_image,
               'schiaparelli_image': schiaparelli_image, 'syrtis_image': syrtis_image, 'valles_image': valles_image}
	return mars               