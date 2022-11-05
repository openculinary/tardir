from argparse import ArgumentParser, FileType
import json
import sys

from recipe_scrapers import SCRAPERS
import surt


def _recipe_hosts():
    yield from SCRAPERS.keys()


def urls():
    parser = ArgumentParser(description="Yield potential recipe URLs from a CDX index")
    parser.add_argument("--filename", nargs=1, default=sys.stdin, type=FileType("r"))
    args = parser.parse_args()

    surted_domains = set(surt.surt(f"http://{host}")[:-2] for host in _recipe_hosts())
    while line := args.filename.readline():
        domain = line[: line.index(")")]
        if domain not in surted_domains:
            continue
        _, _, crawl_info_json = line.split(" ", 2)

        crawl_info = json.loads(crawl_info_json)
        if not "text/html" == crawl_info["mime"] == crawl_info["mime-detected"]:
            continue

        print(crawl_info["url"])
