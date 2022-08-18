#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[49]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[50]:


# Visit the mars nasa news site
url= 'https://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[51]:


html= browser.html
news_soup= soup(html, 'html.parser')
slide_elem= news_soup.select_one('div.list_text')


# In[52]:


slide_elem.find('div', class_='content_title')


# In[53]:


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[54]:


# Use the parent element to find the paragraph text
news_p= slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[55]:


# Visit URL
url= 'https://spaceimages-mars.com/'
browser.visit(url)


# In[56]:


# Find and click the full image button
full_image_elem= browser.find_by_tag('button')[1]
full_image_elem.click()


# In[57]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[58]:


# Find the relative image url
img_url_rel= img_soup.find('img', class_= 'fancybox-image').get('src')
img_url_rel


# In[59]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[60]:


df=pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns= ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[61]:


df.to_html()


# In[62]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)
# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[63]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[96]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)


# In[105]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for hemis in range(4):
    browser.links.find_by_partial_text('Hemisphere')[hemis].click()
    
    new_html = browser.html
    hemi_soup = soup(new_html,'html.parser')
    
    new_title = hemi_soup.find('h2', class_='title').text
    image_url = hemi_soup.find('li').a.get('href')
    
    hemispheres = {}
    hemispheres['img_url'] = f'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars{img_url}'
    hemispheres['title'] = new_title
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# In[106]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[46]:


# 5. Quit the browser
browser.quit()


# In[ ]:




