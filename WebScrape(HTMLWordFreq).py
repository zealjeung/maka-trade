# Store url of chosen novel from gutenberg
# url = 'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm'
# url = 'https://www.imsdb.com/scripts/Les-Miserables.html'
# url = 'http://syndein.com/Genesis.html'

# import html5lib
import html5lib
# Import `requests`
import requests
# Make the request and check object type
r = requests.get(url)
# Extract HTML from Response object and print
html = r.text
# print(html.encode("utf-8"))
# Import BeautifulSoup from bs4
from bs4 import BeautifulSoup
# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html5lib")
# Get the text out of the soup and print it
text = soup.get_text()
# print(text.encode('utf-8'))
# Import regex package
import re
# Find all words in Moby Dick and print several
tokens = re.findall('\w+', text)
# Initialize new list
words = []
# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())
# Import nltk
import nltk
# nltk.download('stopwords')
# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')
# Initialize new list
words_ns = []
# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)
# Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Figures inline and set visualization style
sns.set()
# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
title = soup.title.string
plt.title(title)
freqdist1.plot(20)
