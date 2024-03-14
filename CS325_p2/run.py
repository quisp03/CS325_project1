# run.py
from module_1.scrape import CollectArticleInfo
from module_2.process import ArticleProcessor
import sys
import os

# Sole responsibility of main function is to coordinate the actions of the other modules (1 and 2) to achieve objective.
# Principle states that a class should have one sole reason to change.
def main():
    # User file input
    # Take in commandline arguments
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else input('Enter filename: ')
    except EOFError:
        filename = 'Data/raw/newsarticles_url.txt'
    # Check if the filename provided exists in the current directory
    if not os.path.isfile(filename):
    # If not, prepend the default directory path
        filename = os.path.join('Data/raw', filename)


    with open(filename, 'r') as file:
        article_urls = file.readlines()

    # Handle reading and writing URLs from given text file input, then check for exceptions.
    for i, url in enumerate(article_urls):
        url = url.strip()
        try:
            article = CollectArticleInfo.scrape_url(url)
            ArticleProcessor.process(article, url, i)
        except Exception as e:
            print(f"Failure scraping! {url}: {e}")

if __name__ == "__main__":
    main()