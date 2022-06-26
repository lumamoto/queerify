from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import ssl

def create_wiki_csv():
    ssl._create_default_https_context = ssl._create_unverified_context
    wiki_urls = [
        "https://en.wikipedia.org/wiki/Category:Bisexual_musicians",
        "https://en.wikipedia.org/wiki/Category:Gay_musicians",
        "https://en.wikipedia.org/wiki/Category:Intersex_musicians",
        "https://en.wikipedia.org/wiki/Category:Lesbian_musicians",
        "https://en.wikipedia.org/wiki/Category:Pansexual_musicians",
        "https://en.wikipedia.org/wiki/Category:Queer_musicians",
        "https://en.wikipedia.org/wiki/Category:Transgender_women_musicians",
        "https://en.wikipedia.org/wiki/Category:Transgender_male_musicians",
        "https://en.wikipedia.org/wiki/Category:Non-binary_musicians"
    ]
    artists = []
    identities = []

    for url in wiki_urls:
        html = urlopen(url) 
        soup = BeautifulSoup(html, 'html.parser')

        # Grab list of artists from article
        num_artists = 0 # Keep track of number of artists in current article
        for div in soup.find_all(class_="mw-category-group"):
            for li in div.find_all('li'):
                name = li.text
                if "musicians" not in name: # Ignore "musicians" list items
                    name, *_ = name.split(' (') # Remove parentheses
                    artists.append(name)
                    num_artists += 1

        # Add their identities to list
        identity = soup.find('h1').text
        identity = identity.partition("Category:")[2].rpartition(" musicians")[0]
        if "male" in identity:
            identity = identity.replace("male", "men")
        for i in range(num_artists):
            identities.append(identity)

    df = pd.DataFrame([artists, identities]).transpose()
    df.columns = ['Artist', 'Identity']
    # print(df)

    # Export to .csv
    df.to_csv('data/wikipedia.csv', index=False)

create_wiki_csv()