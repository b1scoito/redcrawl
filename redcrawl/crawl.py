from redcrawl.api.redapi import get_top10_torrents


def init_crawl():
    # Get top10 torrents list
    top10_torrents = get_top10_torrents()
    if top10_torrents != None:
        print(top10_torrents)
