from pydantic import BaseModel, root_validator
from typing import List, Union, Any, Optional

class OHLCVDataOKX(BaseModel):
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    volCcy: float
    volCcyQuote: float
    confirm: int
    # include any additional fields returned by the OKX API

    @root_validator(pre=True)
    def parse_list(cls, values: Union[List, Any]) -> Any:
        if isinstance(values, list):
            return {
                'timestamp': int(values[0]),
                'open': float(values[1]),
                'high': float(values[2]),
                'low': float(values[3]),
                'close': float(values[4]),
                'volume': float(values[5]),
                'volCcy': float(values[6]),
                'volCcyQuote': float(values[7]),
                'confirm': int(values[8])
            }
        return values
    
class CandleResponseOKX(BaseModel):
    code: int
    msg: Optional[str]
    data: List[Any]


    
class OHLCVDataBINANCE(BaseModel):
    timestampOpen: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestampClose: int
    quoteAssetVolume: float
    numberOfTrades: int
    takerBuyBaseAssetVolume: float
    takerBuyQuoteAssetVolume: float
    unused: int

    @root_validator(pre=True)
    def parse_list(cls, values: Union[List, Any]) -> Any:
        if isinstance(values, list):
            return {
                'timestampOpen': int(values[0]),
                'open': float(values[1]),
                'high': float(values[2]),
                'low': float(values[3]),
                'close': float(values[4]),
                'volume': float(values[5]),
                'timestampClose': int(values[6]),
                'quoteAssetVolume': float(values[7]),
                'numberOfTrades': int(values[8]),
                'takerBuyBaseAssetVolume': float(values[9]),
                'takerBuyQuoteAssetVolume': float(values[10]),
                'unused': int(values[11]),
            }
        return values
    



