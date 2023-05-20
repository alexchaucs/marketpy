import requests
from typing import List, Optional
from lib.model import CandleResponseOKX, OHLCVDataOKX
from pydantic import ValidationError
import pandas as pd

def retrieveData(inst_id: str, exchange:str, after: Optional[int] = None, before: Optional[int] = None, candleSize: Optional[str] = None):
    '''
    Retrieve data from give exchange, coin, bar size, after and before date
    '''
    if exchange == 'OKX':
        # Build Params
        params = {
            "instId": inst_id,
            "after": after,
            "before": before,
            "bar": candleSize
        }
        # Remove any missing params
        params = {k: v for k, v in params.items() if v is not None}

        # Base URL
        base_url = "https://www.okx.com/api/v5/market/history-candles"


        # Initial get request
        try:
            response = requests.get(base_url, params = params)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        
        # Validate Candle resposne
        try:
            candle_response = CandleResponseOKX.parse_obj(response.json()) 
        except ValidationError as e:
            print(f"Validation error: {e}")
            # print(response.json)
            return None
        
        # Parse Candle Data
        try:
            candle_data = [OHLCVDataOKX.parse_list(d) for d in candle_response.data]
            print(candle_data)
        except ValidationError as e:
            print(f"Validation error: {e}")

        # Convert to dataframe
        print(pd.DataFrame(candle_data))

    elif exchange == 'BINANCE': 
        # Build Params
        params = {
            "symbol": inst_id,
            "startTime": after,
            "endTime": before,
            "interval": candleSize
        }
        # Remove any missing params
        params = {k: v for k, v in params.items() if v is not None}

        # Base URL
        base_url = "https://api.binance.com/api/v3/klines"

        # Initial get request
        try:
            response = requests.get(base_url, params = params)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        
        # Parsing cnadle resposne
        try:
            candle_response = CandleResponse.parse_obj(response.json())
        except ValidationError as e:
            print(f"Validation error: {e}")
            return None

        # Return Parse Response
        return candle_response
    return

