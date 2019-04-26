#the docstring having all the tags of HTML
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister"
id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister"
id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister"
id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#imporitng the beautifulsoup
from bs4 import BeautifulSoup
#using BS4 and passing the docstring and requires output is in the form of full html document
soup = BeautifulSoup(html_doc, 'html.parser')
#print the html format
print(soup.prettify())
