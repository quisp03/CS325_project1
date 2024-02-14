# - Python News Article Scraper

This is a program made using python which visits every URL of specified news articles given in a textfile. This script utilizes the requests library to send out requests and BeautifulSoup library for parsing HTML content. It is designed to scrape text and then write out that content to a textfile. The script handles some filtering and discarding of material that is non-related information, containing only the content relevent to the article. 
## *Notes before you start
- This program takes in commandline arguments, when running in terminal be sure to follow this format: 'run scriptname.py something.txt. Also please note that this program is specifically designed to handle news agency articles. Providing URLs of non-news articles or other types of web pages may lead to unexpected output or errors.

## * Requirements

* Must have a Windows/Mac/Linux operating system
* Know a few basic command line operations, see the following for more help: [Github CommandLine Documentation](https://docs.github.com/en/github-cli/github-cli/quickstart)
* Install git for your system (important for cloning repo and conda environment) here: [Git Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Install the latest version of python (3.9 or higher) here: [Python Installation](https://www.python.org/downloads/)
* Install miniconda virtual environment (for python package management) here: [Miniconda Installation](https://docs.anaconda.com/free/miniconda/miniconda-install/)

## - Installation Process

1. Install Miniconda: Follow the instructions given on-screen.
2. Create a New Virtual Environment: Open your terminal/command-line prompt then create a new virtual environment, be sure to specify python version name ```conda create --name myenv python=3.9``` where myenv is whatever environment name of your choosing.
3. Activate the Environment: Once the environment is created, activate that environment via ```conda activate myenv```.
4. Clone the Repository: Navigate to a desired directory of your choosing to clone the repository. For example, ```cd your_dir_path/projects```. Clone your git repository via: ```git clone https://github.com/username/repo.git``` replace with actual GitHub username and repository.
5. Navigate to the Repository: Now navigate to the cloned repository, using ```cd repo``` replace “repo” with the cloned repository name.
6. Install Required Packages: Install the required packages using this command ```pip install requests beautifulsoup4```.
7. Deactivate the Environment: When no longer in need of the environment, simply type ```conda deactivate```.

## - How to use the program

1. Choose any category (politics, sports, entertainment, etc.) from any news agency website of your liking.
2. Click on any 5 links within the category and copy those URLs.
3. Paste each of these URLs in a single text file. To create a new text file, type the following in the terminal: ```notepad "something.txt"```, you will be prompted to create a new file, click yes.
4. After pasting the URLs in the file, save the file via ```ctrl + s``` or file save in the top left corner.
5. Activate your Miniconda environment using conda activate myenv.
6. In the command-line, use the following to run the script ```python script.py something.txt``` where “script.py” is replaced with the name of your actual script and “something.txt” is the name of your file.
7. After entering the command, 5 different text files should be generated, containing the output of your chosen URL articles.

## - Guidance

If you come across any issues, please refer to potential solutions below:

* Double check to make sure you have all required libraries and the latest version of python installed.
* Make sure you're located in the correct directories.
* Be sure that you've included all commandline arguments to run the program.
* Make sure the URLs you've provided are valid links.


## - Nametag

- Program by Marquis Pritchett