import os
import requests

base_url = "https://redacted.ch/"

session = requests.session()
session.headers = {
    "Authorization": os.getenv("REDACTED_API_KEY")}


def get_top10_torrents() -> str | None:
    res = session.get(f"{base_url}ajax.php?action=top10")
    print(res.status_code)
    json = res.json()
    if json["status"] != "success":
        return None

    return session.get(f"{base_url}ajax.php?action=top10").text
