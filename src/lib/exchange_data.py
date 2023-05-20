import requests
from typing import List, Optional
from lib.model import CandleResponseOKX, OHLCVDataOKX, OHLCVDataBINANCE
from pydantic import ValidationError
import pandas as pd
from datetime import datetime

def dateConversionToUnix(dateString: Optional[str]) -> int:
    if dateString is None:
        return int(datetime.now().timestamp())
    
    dt = datetime.strptime(dateString, '%Y%m%d')
    return int(dt.timestamp())


def retrieveData(inst_id: str, exchange:str, after: Optional[int] = None, before: Optional[int] = None, candleSize: Optional[str] = None) -> pd.DataFrame:
    '''
    Retrieve data from give exchange, coin, bar size, after and before date
    '''
    if exchange == 'OKX':
        # Build Params
        params = {
            "instId": inst_id,
            "after": dateConversionToUnix(after),
            "before": dateConversionToUnix(before),
            "bar": candleSize
        }
        # Remove any missing params
        params = {k: v for k, v in params.items() if v is not None}

        print(params)
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
        except ValidationError as e:
            print(f"Validation error: {e}")

        # Convert to dataframe
        return pd.DataFrame(candle_data)

    elif exchange == 'BINANCE': 
        # Build Params
        params = {
            "symbol": inst_id,
            "startTime": dateConversionToUnix(after),
            "endTime": dateConversionToUnix(before),
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

        # print(response.json())        
        # Parse Candle Data
        try:
            candle_data = [OHLCVDataBINANCE.parse_list(d) for d in response.json()]
        except ValidationError as e:
            print(f"Validation error: {e}")

        # Convert to dataframe
        return pd.DataFrame(candle_data)

    return

