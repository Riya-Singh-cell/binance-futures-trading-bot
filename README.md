# Binance Futures Trading Bot (Testnet)

A Python command-line application to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).
The project focuses on clean backend design, safe API integration, logging, and error handling.

This application demonstrates how to interact with an external trading API in a structured and production-style manner, including environment-based configuration and defensive coding practices.

## Features

- Place MARKET and LIMIT orders on Binance Futures Testnet
- Supports both BUY and SELL orders
- Command-line interface (CLI) built using argparse
- Clean separation between API interaction, order execution logic, and CLI handling
- Structured logging to file and console
- Robust error handling and input validation
- Secure API key management using environment variables

## Setup Instructions

1. Clone the repository  
git clone <your-repo-url>  
cd binance-futures-trading-bot  

2. Create and activate a virtual environment  
python -m venv venv  

Windows:  
venv\Scripts\activate  

Mac / Linux:  
source venv/bin/activate  

3. Install dependencies  
pip install -r requirements.txt  

4. Create a .env file (Important)

Create a .env file in the project root directory with the following content:

BINANCE_API_KEY=your_testnet_api_key  
BINANCE_API_SECRET=your_testnet_api_secret  

Do not commit the .env file to GitHub.  
It is already excluded via .gitignore.

## Binance Futures Testnet Setup

1. Register at https://testnet.binancefuture.com  
2. Generate API Key and Secret  
3. Enable Futures permissions  
4. Add test USDT funds from the testnet dashboard  

## How to Run

MARKET Order Example:  
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001  

LIMIT Order Example:  
python cli.py --symbol BTCUSDT --side BUY --order_type LIMIT --quantity 0.001 --price 50000  

## Sample Output

ORDER PLACED SUCCESSFULLY  
Order ID: N/A  
Status: N/A  
Executed Quantity: N/A  
Average Price: N/A  

Note: Binance Futures Testnet may return empty acknowledgment responses ({}) for order placement.
Orders are still successfully accepted and logged.

## Logging

Logs are written to:  
logs/trading_bot.log  

Logs include:
- Order request details
- API responses
- Errors and exceptions

Sample log entry:  
INFO | Placing MARKET order | Symbol=BTCUSDT, Side=BUY, Quantity=0.001  
INFO | Order response received: {}  

## Testnet Behavior Note

Binance Futures Testnet may return empty responses ({}) for both MARKET and LIMIT orders,
even when the order is successfully placed.

This behavior is handled safely in the application and documented through logs.
On the Binance Futures mainnet, full order details are typically returned.

## Requirements Coverage

- Python 3.x
- MARKET order support
- LIMIT order support
- BUY / SELL support
- CLI input validation
- Logging to file and console
- Error handling
- Clean and reusable code structure

## Assumptions

- This project uses Binance Futures Testnet (USDT-M) only
- No real funds are involved
- A CLI-based interface is used to keep the focus on backend execution logic
