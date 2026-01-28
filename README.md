Binance Futures Trading Bot (Testnet)

A Python command-line application to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M) with clean architecture, logging, and error handling.

This project demonstrates safe integration with an external trading API, structured code design, and production-style practices such as environment-based configuration and logging.

🚀 Features

Place MARKET and LIMIT orders on Binance Futures Testnet

Supports BUY and SELL orders

Command-line interface (CLI) using argparse

Clean separation of concerns:

API client layer

Order logic

CLI layer

Structured logging to file and console

Robust error handling

Secure API key management using environment variables

🧱 Project Structure
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures Testnet client
│   ├── orders.py          # Order placement logic
│   ├── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── .gitignore
└── logs/
    └── trading_bot.log

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone <your-repo-url>
cd binance-futures-trading-bot

2️⃣ Create and activate virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create .env file (IMPORTANT)

Create a .env file in the project root and add:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret

Note: The .env file is excluded from version control via .gitignore.

--------------------------------------------------

5️⃣ Binance Futures Testnet Setup

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

📄 Output Example
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


Includes:

Order request details

API responses

Errors and exceptions

Sample log entry:

INFO | Placing MARKET order | Symbol=BTCUSDT, Side=BUY, Quantity=0.001
INFO | Order response: {}

⚠️ Testnet Behavior Note

Binance Futures Testnet sometimes returns empty responses ({}) for both MARKET and LIMIT orders, even when the order is successfully placed.

This behavior is handled safely in the application and is documented in logs.
In production (mainnet), full order details are typically returned.

✅ Requirements Coverage

 Python 3.x

 MARKET orders

 LIMIT orders

 BUY / SELL support

 CLI input validation

 Logging to file

 Error handling

 Clean, reusable code structure

📌 Assumptions

This project uses Binance Futures Testnet (USDT-M) only

No real funds are involved

CLI is preferred over UI for simplicity and focus on backend logic