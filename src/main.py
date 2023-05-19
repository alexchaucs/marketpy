import requests
import argparse
import json
from lib.exchange_data import get_binance_data, get_okex_data


def main():
    parser = argparse.ArgumentParser(description='Crypto comparison script.')
    parser.add_argument('--coin1', type=str, required=True, help='The first coin.')
    parser.add_argument('--coin2', type=str, required=True, help='The second coin.')
    parser.add_argument('--percent1', type=float, required=True, help='The first percentage.')
    parser.add_argument('--percent2', type=float, required=True, help='The second percentage.')
    parser.add_argument('--timeframe1', type=str, required=True, help='The first timeframe.')
    parser.add_argument('--timeframe2', type=str, required=True, help='The second timeframe.')
    
    args = parser.parse_args()

    coin1_binance_data = get_binance_data(args.coin1)
    coin2_binance_data = get_binance_data(args.coin2)

    coin1_okex_data = get_okex_data(args.coin1)
    coin2_okex_data = get_okex_data(args.coin2)

    print(f"Binance {args.coin1} data: {json.dumps(coin1_binance_data, indent=4)}")
    print(f"Binance {args.coin2} data: {json.dumps(coin2_binance_data, indent=4)}")
    print(f"OKEx {args.coin1} data: {json.dumps(coin1_okex_data, indent=4)}")
    print(f"OKEx {args.coin2} data: {json.dumps(coin2_okex_data, indent=4)}")

if __name__ == "__main__":
    main()
