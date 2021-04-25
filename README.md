# tsai-quant

tsai-quant is a python framework for quantative finance

## Installation

```
~ git clone https://github.com/tildeSlashAi/tsai-quant.git
...
~ pip install -r requirements.txt
...
```

## How to Use

### tsai_quant.data

tsai_quant can use prebuilt or custom APIs to retrieve historic price data.

```python
import tsai_quant.data as qdata

aapl_ticker = qdata.Ticker('AAPL')
aapl = qdata.DailyPrice(aapl_ticker)
```

The Data retrieval API is specified with the `qdata.SourceManager` variable. By default pandas_datareader with googlefinance is being used.
