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

