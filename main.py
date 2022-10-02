from dotenv import load_dotenv
from redcrawl.crawl import init_crawl


def init():
    # Load .env files
    load_dotenv()

    # Start crawling
    init_crawl()


if __name__ == "__main__":
    init()
