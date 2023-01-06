#!/usr/bin/env python3

from argparse import ArgumentParser
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

def fetch_results(domain):
    results = DNSDumpsterAPI().search(domain)
    return results

def main():
    parser = ArgumentParser()
    parser.add_argument("-d",help="enter domain name", dest="domain")

    args = parser.parse_args()
    print(fetch_results(args.domain))


if __name__ == '__main__':
    main()
