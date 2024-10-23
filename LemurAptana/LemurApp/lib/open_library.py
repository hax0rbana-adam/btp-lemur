from collections import namedtuple
from json import load
from logging import info, warning, error
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen


RESULTS_PER_PAGE = 10

booktuple = namedtuple('booktuple', ['title', 'author', 'isbn'])
searchresult = namedtuple('searchresult', ['pages', 'books', 'lastResultIndex'])


def search(parameters, page=0):
  response = load(urlopen("https://openlibrary.org/search.json?{}".format(urlencode(parameters))))

  results = []
  items = response.get('docs', [])
  i = page * RESULTS_PER_PAGE
  while i < len(items) and len(results) < RESULTS_PER_PAGE:
    item = items[i]
    if "isbn" in item:  # omit books without an isbn
      author = item["author_name"][0] if "author_name" in item.keys() else ""
      results.append(type("book", (object,), {"title": item["title"],
                                              "author": author,
                                              "isbn": item["isbn"][0]}))
    i += 1
  return type("SearchResults", (object,), {"pages": response["numFound"] // RESULTS_PER_PAGE,
                                           "lastResultIndex": i,
                                           "books": results})

def search_isbn(isbn):
  info("Searching for isbn of: {}".format(isbn))
  try:
    response = load(urlopen("https://openlibrary.org/isbn/{}.json".format(isbn)))
  except HTTPError as e:
    if e.getcode() != 404:
      # Something went wrong other than that the isbn wasn't found
      error("Unable to lookup ISBN. e="+e)
    return None

  title = response["title"]
  try:
    response = load(urlopen("https://openlibrary.org/{}.json".format(response["authors"][0]['key'])))
  except HTTPError as e:
    if e.getcode() != 404:
      # Something went wrong other than that the isbn wasn't found
      error("Unable to lookup ISBN. e="+e)
    return None
  author = response["personal_name"] if "personal_name" in response.keys() else ""
  return type("book", (object,), {"title": title,
                                  "author": author,
                                  "isbn": isbn})
