# module_1/scraper.py
import requests
from bs4 import BeautifulSoup

# The CollectArticleInfo class follows (SRP) or 'Single Responsibility Principle'
# Principle states that a class should have one sole reason to change.
# The class has one sole single responsibility being to scrape article data from URL.

class CollectArticleInfo:
    @staticmethod
    # *scrape_url method takes in URL as the input
    # Returns the scraped article as output
    def scrape_url(url): # Fetches the webpage content, parses it to find the article text
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Find title
        title = soup.find('title').text

        # Find main
        main = soup.find('main', {'class': 'Page-main'})

        # Removing all the elements in <div class="CarouselSlide-info-content">
        for div in main.find_all('div', {'class': 'CarouselSlide-info-content'}):
            div.decompose()
        # Removing all the elements in <span class="LinkEnhancement">
        for span in main.find_all('span', {'class': 'LinkEnhancement'}):
            span.decompose()

        # Find all paragraphs
        paragraphs = main.find_all('p')

        # Array list to hold paragraphs
        paragraph_list = []

        # Iterating over all of the paragraphs except last
        for p in paragraphs[:-1]:

            if p.text.strip() and not p.text.startswith(('http', 'www')):
        # Appending the paragraph to list if we reach the condition
                paragraph_list.append(p.text)

        # Joining the paragraphs with newlines
        article = '\n\n'.join(paragraph_list)

        # Returning title and article text
        return title + '\n' + article