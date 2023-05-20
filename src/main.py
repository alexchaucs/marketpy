import requests
import argparse
import json
from lib.exchange_data import retrieveData
from lib.model import *
from typing import Optional


def parse_args():
    parser = argparse.ArgumentParser(description='Crypto comparison script.')
    parser.add_argument('--coin1', type=str, required=True, help='The first coin.')
    parser.add_argument('--coin2', type=str, required=True, help='The second coin.')
    parser.add_argument('--exchange1', type=str, required=True, help='The first percentage.')
    parser.add_argument('--exchange2', type=str, required=True, help='The second percentage.')

    parser.add_argument('--before1', type=int, required=False, help='The first timeframe.')
    parser.add_argument('--before2', type=int, required=False, help='The first timeframe.')
    parser.add_argument('--after1', type=int, required=False, help='The first timeframe.')
    parser.add_argument('--after2', type=int, required=False, help='The first timeframe.')
    parser.add_argument('--candleSize1', type=str, required=False, help='The first timeframe.')
    parser.add_argument('--candleSize2', type=str, required=False, help='The second timeframe.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    # coin1 = retrieveData(inst_id = args.coin1, exchange = args.exchange1, after = args.after1, before = args.before1, candleSize = args.candleSize1)
    coin2 = retrieveData(inst_id = args.coin2, exchange = args.exchange2, after = args.after2, before = args.before2, candleSize = args.candleSize1)

if __name__ == "__main__":
    main()



