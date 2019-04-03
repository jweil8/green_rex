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
    for i in list:
        if i in docs.find_one({'url':url}):
            None
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
        
def parse_docs(dict):
    """Parse the HTML docs that we have stored in a dictionary, return as a list. """
    strain_text= []
    for key, values in dict.items():
        soup = BeautifulSoup(values, 'html.parser')
        strain_text.append(soup.select("p.strain-review__text"))
            #stars = soup.select("div.star_rating")
    return strain_text


def get_stars_list(d):
    """grabs the star ratings for eac review"""
    stars = []
    for key, values in d.items():
        soup = BeautifulSoup(values, 'html.parser')
        tags = soup.select("div.div.stars")
        for t in tags:
            stars.append(t.attrs['style'])
    return stars

def star_int_conv(l):
    """get star width str, strip and turn into an integer value 1-5 to represent the number of stars"""
    flat_stars= []
    star_num = []
    for s in l:
        star = int((s[6:].split(';')[0]).strip('px'))
        star_num.append((star/22))
        for star in star_num:
            for item in sublist:
                flat_stars.append(item)
    return flat_stars

def list_o_strains(i):
    # Works on the main explore page, but doesnt when i use filter...
    #need to figure out how to get the filters to work and still scrapy.
    LOS = []
    r = requests.get(i)
    soup2 = BeautifulSoup(r.content, 'html.parser')
    strains = soup2.find_all('a', class_="ga_Explore_Strain_Tile")
    for s in strains:
        LOS.append(s.attrs['href'])
    return LOS

def grab_users(i):
"""Gets all of the users that reviews the strain"""
    LU = []
    r = requests.get(i)
    soupu = BeautifulSoup(r.content, 'html.parser')
    users = soupu.find_all('div', {'class': 'strain-review__title'})
    for u in users:
        temp = u.find('h2')
        LU.append(temp.text)
    return LU


def grab_users_from_list(l):
"""Pass in a list of URLS to scrape and it returns all the userswhove reviewd the strain"""
    LU = []
    htmls = []
    for i in l:
        r = requests.get(i)
        html = (r.content)
        htmls.append(html)
        soupu = BeautifulSoup(r.content, 'html.parser')
        users = soupu.find_all('div', {'class': 'strain-review__title'})
        for u in users:
            temp = u.find('h2')
        LU.append(temp.text)
    return LU