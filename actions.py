"""

action.py - Drew Taylor - 4.26.18

Module which stores all function logic for Pengwin's commands.abs

"""

import urllib.request
import json
import pymongo
import nba


def lookup(command):
    """ 
        Looks up and serves a website in a nice manner.
    """ 
    # TODO!!! What else can be done with this?
    try:
        website = command.split()[1]
        if 'com' in website:
            domain = website.split('.')[-1]
            # TODO!!!
        else:
            domain = website
        return 'www.{}.com'.format(domain)
    except IndexError:
        return 'Please provide a website when using the "lookup" command.'

def nba(command):
    """
        Provides the user with a nice info layout about current
        NBA games and statistics.
    """
    try:
        block = command.split()[1]
    except KeyError:
        return 'Please provide a specific block when using the "nba" command.'

    if block == 'summary':
        with urllib.request.urlopen("http://data.nba.net/10s/prod/v1/today.json") as url:
            data = json.loads(url.read().decode())
            return data
    elif block == 'teams':
        with urllib.request.urlopen("http://data.nba.net/10s/prod/2017/teams_config.json") as url:
            data = json.loads(url.read().decode())
            return data
    elif block == 'current game':
        return nba.current()


