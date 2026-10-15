#!/usr/bin/python3
'''Starter functions for the Selector Golf lab.'''
from bs4 import BeautifulSoup


def count_matches(html, selector):
    '''
    Return how many tags in `html` match the CSS `selector`.

    >>> count_matches('<div><p>a</p><p>b</p><span><p>c</p></span></div>', 'p')
    3
    >>> count_matches('<div><p>a</p><p>b</p><span><p>c</p></span></div>', 'div > p')
    2
    '''
    soup = BeautifulSoup(html, 'html.parser')
    return len(soup.select(selector))


def select_texts(html, selector):
    '''
    Return the `.text` of every tag in `html` that matches `selector`.

    >>> select_texts('<span class="price">$9.99</span><span class="price">$19.99</span>', '.price')
    ['$9.99', '$19.99']
    >>> select_texts('<div><p>a</p><p>b</p></div>', 'p')
    ['a', 'b']
    '''
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.text for tag in soup.select(selector)]

def select_attr(html, selector, attr):
    '''
    Return the value of `attr` on every tag in `html` matching `selector`.

    >>> select_attr('<a href="/a">One</a><a href="/b">Two</a>', 'a', 'href')
    ['/a', '/b']
    >>> select_attr('<img src="x.png"><img src="y.png">', 'img', 'src')
    ['x.png', 'y.png']
    '''
    soup = BeautifulSoup(html, 'html.parser')
    return [tag[attr] for tag in soup.select(selector) if tag.has_attr(attr)]


def extract_titles(html):
    '''
    Return the text of every listing title (the `a.title` links).

    >>> extract_titles('<li class="item"><a class="title" href="/1">Mouse</a></li><li class="item"><a class="title" href="/2">Keyboard</a></li>')
    ['Mouse', 'Keyboard']
    '''
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.text.strip() for tag in soup.select('.title')]

def extract_prices_cents(html):
    '''
    Return every `.price` as a whole number of cents (an int, never a float).

    >>> extract_prices_cents('<span class="price">$49.99</span><span class="price">$5.00</span>')
    [4999, 500]
    >>> extract_prices_cents('<span class="price">$8.99</span>')
    [899]
    '''
    soup = BeautifulSoup(html, 'html.parser')
    prices = []
    for tag in soup.select('.price'):
        dollars = tag.text.strip().lstrip('$')
        prices.append(int(round(float(dollars) * 100)))
    return prices
    # TODO: for each '.price', strip the '$', convert dollars to an int of cents
    # Hint: int(round(float(dollars) * 100)) turns '49.99' into 4999


def count_free_shipping(html):
    '''
    Return how many listings carry a free-shipping badge (`.free-shipping`).

    >>> count_free_shipping('<li class="item"><span class="free-shipping">Free shipping</span></li><li class="item"></li>')
    1
    >>> count_free_shipping('<li class="item"></li><li class="item"></li>')
    0
    '''
    # TODO: count the '.free-shipping' tags
    soup = BeautifulSoup(html, 'html.parser')
    return len(soup.select('.free-shipping'))


def first_link(html):
    '''
    Return the `href` of the first link in `html`, or None if there are none.

    >>> first_link('<div><a href="/first">One</a><a href="/second">Two</a></div>')
    '/first'
    >>> first_link('<p>no links here</p>')  # returns None, which prints nothing
    '''
    # TODO: select 'a[href]'; return the first one's href, or None if the list is empty
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a[href]')
    if links:
        return links[0]['href']
    return None


def extract_listings(html):
    '''
    Turn a listings page into a list of dicts, one per `.item`, each with the
    item's `name`, `price_cents`, and `url`. Project 2 uses the same pattern,
    renames `price_cents` to `price`, and adds other listing fields.

    >>> html = '<li class="item"><a class="title" href="/itm/1">Mouse</a><span class="price">$9.99</span></li><li class="item"><a class="title" href="/itm/2">Keyboard</a><span class="price">$19.99</span></li>'
    >>> extract_listings(html)
    [{'name': 'Mouse', 'price_cents': 999, 'url': '/itm/1'}, {'name': 'Keyboard', 'price_cents': 1999, 'url': '/itm/2'}]
    '''
    # TODO: loop over each '.item'; inside each, find its '.title' and '.price'
    # and build a dict with keys 'name', 'price_cents', and 'url'
    soup = BeautifulSoup(html, 'html.parser')
    listings = []
    for item in soup.select('.item'):
        title_tag = item.select_one('.title')
        price_tag = item.select_one('.price')

        name = title_tag.text.strip() if title_tag else ''
        url = title_tag['href'] if title_tag and title_tag.has_attr('href') else None

        if price_tag:
            dollars = price_tag.text.strip().lstrip('$')
            price_cents = int(round(float(dollars) * 100))
        else:
            price_cents = 0

        listings.append({
            'name': name,
            'price_cents': price_cents,
            'url': url
        })
    return listings


if __name__ == '__main__':
    import doctest
    doctest.testmod()
