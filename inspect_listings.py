from bs4 import BeautifulSoup

with open('sample_listings.html', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.price'):
    print(tag.text)

for tag in soup.select('.item'):
    print(tag.text)

for tag in soup.select('.badge'):
    print(tag.text)

for tag in soup.select('.free-shipping'):
    print(tag.text)

for tag in soup.select('.sponsored'):
    print(tag.text)

for tag in soup.select('.results > li'):
    print(tag.text)

for tag in soup.select('.item + .item'):
    print(tag.text)

for tag in soup.select('.li.item > a'):
    print(tag.text)


#Predictions
#.item 5
#.badge 4
#.free-shipping 3
#.sponsored 1
#results > li 5
#.item + .item 4
#li.item > a 5

from bs4 import BeautifulSoup
from lab_selectors import extract_listings

# Load local sample_listings.html file
with open('sample_listings.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')


from bs4 import BeautifulSoup
from lab_selectors import extract_listings

# Load local sample_listings.html file
with open('sample_listings.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

print("--- ALL PRICES ---")
for tag in soup.select('.price'):
    print(tag.get_text().strip())

print("\n--- SELECTOR MATCH COUNTS ---")
selectors = [
    '.item',
    '.badge',
    '.free-shipping',
    '.sponsored',
    '#results > li',
    '.item + .item',
    'li.item > a',
]

for sel in selectors:
    matches = soup.select(sel)
    print(f"len(soup.select('{sel}')) = {len(matches)}")

print("\n--- EXTRACT LISTINGS TEST ---")
listings = extract_listings(html_content)
print(f"Total items extracted: {len(listings)}\n")

print(listings)

listings = extract_listings(html_content)

