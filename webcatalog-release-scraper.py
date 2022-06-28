#!/usr/bin/env python3

import json
from argparse import ArgumentParser, FileType
from sys import stdin, stdout
from typing import Dict, List

from bs4 import BeautifulSoup, Tag


def scrape(article: Tag) -> List[Dict]:
    releases = []
    for div in article.find_all('div'):
        if not div.find('h2'):
            continue
        span = div.find('span')
        assert isinstance(span, Tag)
        version = span.get_text()[1:]
        p = div.find('p')
        assert isinstance(p, Tag)
        changes = p.get_text()
        releases.append({
            'version': version,
            'changes': changes,
        })
    return releases


def main():
    parser = ArgumentParser()
    parser.add_argument('-i',
                        '--in-file',
                        type=FileType('r'),
                        default=stdin,
                        help='input file, default: stdin')
    parser.add_argument('-o',
                        '--out-file',
                        type=FileType('w'),
                        default=stdout,
                        help='output file, default: stdout')
    args = parser.parse_args()
    soup = BeautifulSoup(args.in_file.read(), features='html.parser')
    article = soup.find('article')
    assert isinstance(article, Tag)
    releases = scrape(article)
    print(json.dumps(releases, indent=2), file=args.out_file)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(130)
