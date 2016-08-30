import os
import time
import csv

usr2cache = lambda usr  : '.{}.cache'.format(usr)

def is_cache_obsolete(username):
    # figure out if cache needs to be updated
    try:
        (_, _, _, _, _, _, _, _, mtime, _) = os.stat(usr2cache(username))
    except OSError:
        return True

    current_time = lambda: int(round(time.time()))
    return (current_time() - mtime) > 3600

def cache(repos, username):
    with open(usr2cache(username),'w') as f:
        for repo in repos:
            f.write('{0},{1}\n'.format(repo['text'], repo['url']))

def from_cache(username):
    with open(usr2cache(username)) as f:
        content = list(csv.reader(f))
    return [ { 'text' : row[0], 'url' : row[1] } for row in content ]

