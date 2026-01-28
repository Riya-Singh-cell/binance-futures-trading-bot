Binance Futures Trading Bot (Testnet)

A Python command-line application to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).
The project focuses on clean API integration, CLI-based interaction, structured logging, and robust error handling.

--------------------------------------------------

Features

- Command Line Interface (CLI) using argparse
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- Clean separation between API client, order handling, and CLI
- Structured logging to file and console
- Secure API key management using environment variables
- Robust error handling

--------------------------------------------------

Setup Instructions

1. Clone the repository

git clone <repository-url>
cd binance-futures-trading-bot

2. Create and activate virtual environment

python -m venv venv

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

--------------------------------------------------

Environment Configuration

Create a .env file in the project root and add:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret

Note: The .env file is excluded from version control via .gitignore.

--------------------------------------------------

Binance Futures Testnet Setup

- Register at https://testnet.binancefuture.com
- Generate API Key and Secret
- Enable Futures permission
- Add test USDT funds from the dashboard

--------------------------------------------------

Usage

Place a MARKET Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Place a LIMIT Order:

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

--------------------------------------------------

Sample Output

ORDER PLACED SUCCESSFULLY
Order ID: N/A
Status: N/A
Executed Qty: N/A
Avg Price: N/A

Note: Binance Futures Testnet may return empty ACK responses ({}) even when orders are successfully placed.
All API requests and responses are logged for verification.

--------------------------------------------------

Logging

Application logs are written to:

logs/trading_bot.log

Logs include:
- Order request details
- API responses
- Error messages and exceptions

--------------------------------------------------

Notes on Testnet Behavior

- Binance Futures Testnet may return empty responses for order placement
- Orders are still accepted successfully
- This behavior is handled gracefully and documented via logs
- On mainnet, full execution details are typically returned

--------------------------------------------------

Assumptions

- This project uses Binance Futures Testnet (USDT-M) only
- No real funds are involved
- CLI-based interface is preferred for simplicity and backend focus

--------------------------------------------------

Submission

This project was developed as part of a Python Developer – Trading Bot assignment,
demonstrating safe API usage, clean architecture, and production-style coding practices.
