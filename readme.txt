#######   Super Simple Stock Market  ###########

Description:

The source code that will -
- For a given stock,
    - calculate the dividend yield
    - calculate the P/E Ratio
    - record a trade, with timestamp, quantity of shares, buy or sell indicator and price
    - Calculate Stock Price based on trades recorded in past 15 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

Constraints & Notes:

1.	No database or GUI is required, all data need to be held in memory.

2.	Formulas and data provided are simplified representations for the purpose of this exercise.

Global Beverage Corporation Exchange

Stock Symbol  | Type      |  Last Dividend| Fixed Dividend| Par Value
------------- | ----      | ------------: | :------------: | --------:
TEA           | Common    | 0             |                | 100
POP           | Common    | 8             |                | 100
ALE           | Common    | 23            |                | 60
GIN           | Preferred | 8             |         2%     | 100
JOE           | Common    | 13            |                | 250




Requirements:

- Python 3.10, Python 3.7 or higher should also be okay
- pandas, openpyxl libraries of python
- Tested on Windows10

INSTALLATIONS:

To install pandas execute command:

'''
pip install pandas
or
conda install pandas
'''

To install openpyxl execute:

'''
pip install openpyxl
or
conda install pandas
'''


Run:
Please ensure:
1. StocksGBCE.xlsx file contains data as specified in current StocksGBCE.xlsx file,
    it is read using pandas and then populates in-memory database/model for further operations.
2. StocksDBFile.txt contains trade records, we operate on this while recording trade, calculating
    volume weighted stock price and GBCE all share index. If this file is not present,
    the code automatically handles it by creating one. So, NO NEED TO WORRY ABOUT IT!!

Ensure main.py is present inside SuperSimpleStockMarket folder and then run as

```
python main.py
```

Output on Console Window:

```
Select a number for corresponding operation:
                                1 for Calculating DIVIDEND yield.
                                2 for calculating P/E ratio.
                                3 for Recording Trade.
                                4 for Calculating Volume Weighted Stock Price.
                                5 for Calculating the GBCE All Share Index.
                                0 to exit, if you are done with all the operations.
                                ===============================================
                                Enter number:
```

Tests:

To test the assignment using unittest, please execute test.py file as

```
python test.py
```

Coder:
Satyam Kumar Sinha
