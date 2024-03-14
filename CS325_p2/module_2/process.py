# process.py

# The ArticleProcessor class follows (SRP) or 'Single Responsibility Principle'
# Principle states that a class should have one sole reason to change.
# The class has one sole single responsibility being to process the scraped article data and write it to a file.

class ArticleProcessor:
    @staticmethod
    # *process method takes the article, URL, and index as input
    # Writes article to file in the Data/processed dir. and prints message
    def process(article, url, i):
        # Write the scraped text from the article to a text file
        with open(f'Data/processed/article_{i+1}.txt', 'w', encoding='utf-8') as f:
            f.write(article)
        print(f"\nThe article from {url} was written to Data/processed/article_{i+1}.txt\n")