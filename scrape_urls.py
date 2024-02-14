import requests
import sys
from bs4 import BeautifulSoup

def url_scraping(url):
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
    # Append the paragraph to list if we reach condition
            paragraph_list.append(p.text)

    # Join paragraphs with newlines
    article = '\n\n'.join(paragraph_list)

    # Returning title and article text
    return title + '\n' + article

def write_article_to_file(article, url, i):
    # Write the scraped text from the article to a text file
    with open(f'article_{i+1}.txt', 'w', encoding='utf-8') as f:
        f.write(article)
    print(f"\nThe article from {url} was written to article_{i+1}.txt\n")


def main():
    # User file input
    # Take in commandline arguments
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        article_urls = file.readlines()

    # Handle reading and writing URLs from given text file input, then check for exceptions.
    for i, url in enumerate(article_urls):
        url = url.strip()
        try:
            article = url_scraping(url)
            write_article_to_file(article, url, i)
        except Exception as e:
            print(f"Failure scraping! {url}: {e}")

if __name__ == "__main__":
    main()