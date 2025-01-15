from argparse import ArgumentParser, FileType
import json
import sys

from recipe_scrapers import SCRAPERS
import surt


def _recipe_hosts():
    yield from SCRAPERS.keys()


def urls():
    parser = ArgumentParser(description="Yield potential recipe URLs from a CDX index")
    parser.add_argument("--filename", default=sys.stdin, type=FileType("r"), required=True)
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

        yield crawl_info


def _may_be_usage_terms_and_conditions(url):
    if "terms" in url.lower():
        return True
    if "policy" in url.lower():
        return True
    if "guideline" in url.lower():
        return True
    if url.lower().count("usage") - url.lower().count("sausage") > 0:
        return True
    return False


def possible_usage_terms_and_conditions():
    for crawl_info in urls():
        url = crawl_info["url"]
        if _may_be_usage_terms_and_conditions(url):
            print(url)


possible_usage_terms_and_conditions()
