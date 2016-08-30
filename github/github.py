from bs4 import BeautifulSoup
import requests

import sys

from colors import suc, err, war, info
from file_utils import cache, is_cache_obsolete, from_cache


build_url = lambda uname : 'https://github.com/{}?tab=repositories'.format(uname)
repo2url  = lambda repo : 'https://github.com{}'.format(repo)

def get_soup(url):
    return BeautifulSoup( requests.get(url).content, 'lxml' )

def extract_repos(url):
    # get soup
    soup = get_soup(url)
    # find all header tags
    header_tags = soup.findAll('h3', {'class' : 'repo-list-name'})
    # iterate through it and fetch url and headers
    return [ { 'text' : htag.text.strip(), 'url' : htag.find('a').get('href') } for htag in header_tags ]


if __name__ == '__main__':
    # get username from cmdline args
    if len(sys.argv) > 1:
        uname = sys.argv[1]
        # check if cache is obsolete
        if is_cache_obsolete(uname):
            # construct url
            my_url = build_url(uname)
            print('>> {0} Pulling from [{1}]'.format(info,my_url))
            # extract repositories
            repos = extract_repos(url=my_url)
            # cache it
            cache(repos, uname)
        else: # get it from cache
            print('>> {0} Pulling from local cache'.format(info))
            repos = from_cache(uname)
        # pretty print 
        for i,repo in enumerate(repos):
            print(suc + '[{0}] {1} : {2}'.format(i,repo['text'], repo['url']))
    else:
        # wrong usage
        print(war + 'usage : python3 github.py <username>')
