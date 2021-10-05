import json
import logging
import logging.config
import os
import urllib.parse
import warnings

import requests

# グローバル設定
FEEDLY_HEADERS = {
    "Authorization": f"Bearer {os.environ['FEEDLY_API_TOKEN']}",
}
FEEDLY_BOARD_ID = urllib.parse.quote(os.environ["FEEDLY_BOARD_ID"], safe="")

LINKACE_HEADERS = {
    "Authorization": f"Bearer {os.environ['LINKACE_API_TOKEN']}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}
LINKACE_LISTS = [int(s) for s in os.environ["LINKACE_LISTS"].split(",")]
LINKACE_TAGS = [int(s) for s in os.environ["LINKACE_TAGS"].split(",")]


# ログ設定
logging.config.dictConfig({
    "version": 1,

    "formatters": {
        "feedly_to_linkace.logging.format": {
            "format": "%(asctime)s - %(levelname)-5s [%(name)s] %(message)s",
        },
    },

    "handlers": {
        "feedly_to_linkace.logging.handler": {
            "class": "logging.StreamHandler",
            "formatter": "feedly_to_linkace.logging.format",
            "level": logging.DEBUG,
        },
    },

    "loggers": {
        "feedly_to_linkace": {
            "handlers": ["feedly_to_linkace.logging.handler"],
            "level": logging.DEBUG,
            "propagate": 0,
        },
    },
})

L = logging.getLogger("feedly_to_linkace")

warnings.simplefilter("ignore")


# Feedlyのタグリストを取得する
def get_feedly_tags():
    L.info("get_feedly_tags: start")

    res = requests.get(
        "https://cloud.feedly.com/v3/boards",
        headers=FEEDLY_HEADERS,
    )
    L.debug(json.dumps(res.json(), indent=4))


# FeedlyのReadLater記事リストを取得する
def get_feedly_readlater():
    L.info("get_feedly_readlater: start")

    res = requests.get(
        f"https://cloud.feedly.com/v3/streams/{FEEDLY_BOARD_ID}/contents",
        headers=FEEDLY_HEADERS
    )
    # L.debug(json.dumps(res.json(), indent=4))

    if res.status_code != 200:
        L.error(f"{res.status_code}: {res.text}")
        raise RuntimeError(f"{res.status_code}: {res.text}")

    items = []

    for item in res.json()["items"]:
        i = {
            "id": item["id"],
            "title": item["title"],
        }

        if "canonicalUrl" in item:
            i["url"] = item["canonicalUrl"]
        else:
            i["url"] = item["alternate"][0]["href"]

        L.debug(i)
        items.append(i)

    return items


# LinkAceにブックマーク登録する
def create_bookmark(item):
    L.info(f"create_bookmark: start: {item}")

    req = {
        "url": item["url"],
        "lists": LINKACE_LISTS,
        "tags": LINKACE_TAGS,
        "is_private": True,
    }

    res = requests.post(
        "https://bookmark.u6k.me/api/v1/links",
        data=json.dumps(req),
        headers=LINKACE_HEADERS,
    )

    if res.status_code == 200:
        L.debug("Bookmark created")
        result = res.json()["id"]
    else:
        L.warning(f"Bookmark create fail: {res.status_code}: {res.text}")
        result = None

    return result


# FeedlyのReadLaterを外す
def remove_feedly_tag(item):
    L.info(f"remove_feedly_tag: start: {item}")

    id = urllib.parse.quote(item["id"], safe="")
    res = requests.delete(
        f"https://cloud.feedly.com/v3/tags/{FEEDLY_BOARD_ID}/{id}",
        headers=FEEDLY_HEADERS,
    )

    if res.status_code != 200:
        L.error(f"{res.status_code}: {res.text}")
        raise RuntimeError(f"{res.status_code}: {res.text}")


# メイン処理
if __name__ == "__main__":
    # get_feedly_tags()
    # raise RuntimeError()

    items = get_feedly_readlater()

    for item in items:
        result = create_bookmark(item)

        if result:
            remove_feedly_tag(item)
