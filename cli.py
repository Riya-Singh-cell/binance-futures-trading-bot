import argparse
import logging

from bot.client import get_binance_client
from bot.logging_config import setup_logging
from bot.orders import place_market_order, place_limit_order


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")
    parser.add_argument("--symbol", required=True, help="Trading symbol e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        client = get_binance_client()

        if args.type == "MARKET":
            order = place_market_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )

        elif args.type == "LIMIT":
            if args.price is None:
                raise ValueError("Price is required for LIMIT orders")

            order = place_limit_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print(f"Order ID: {order.get('orderId', 'N/A')}")
        print(f"Status: {order.get('status', 'N/A')}")
        print(f"Executed Qty: {order.get('executedQty', 'N/A')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        logger.error(f"Execution failed: {e}")
        print("\n❌ Order failed. Check logs for details.")
        print(e)


if __name__ == "__main__":
    main()
