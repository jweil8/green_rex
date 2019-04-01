# Create list of URL's corresponding with strain reviews
def get_url(x,y):
    """X= number of urls to grab, y= strain name or other thing we are scraping 
    Pull in urls from a 'Load MOre' button and the like. Create identical URL's with differing numbers"""
    urls = []
    url = 1 
    while url <= x:
        urls.append("https://www.leafly.com/%s/reviews?page=%d" % (y, url))
        url += 1 
    return urls

# See if table contains URL already, if not add it in.
def table_check(url):
    """This checks to see if a url is already in my database of reviews"""
    if docs.find_one({'url':url}):
        pass
    else:
        docs.insert_one({'url': url,
                 'html': html
                 })

# Insert review into mongo db table
def get_reviews(list):
    """Pass in a list of URL's and return them in a mongo db table as a dicitonary with 
    keys{'url', 'html'} and their corresponding values"""
    htmls = []
    for i in l:
        r = requests.get(i)
        htmls.append(r.content)
        table_check(i)