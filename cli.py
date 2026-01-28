import argparse
import logging

# Importing helper functions from project modules
from bot.client import get_binance_client
from bot.logging_config import setup_logging
from bot.orders import place_market_order, place_limit_order


def main():
    # Setting up logging at the start
    setup_logging()
    app_logger = logging.getLogger(__name__)

    # Defining CLI arguments
    argument_parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot (Testnet)"
    )

    argument_parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (example: BTCUSDT)"
    )
    argument_parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )
    argument_parser.add_argument(
        "--order_type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Type of order"
    )
    argument_parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )
    argument_parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required only for LIMIT orders)"
    )

    user_inputs = argument_parser.parse_args()

    try:
        # Create Binance Futures Testnet client
        trading_client = get_binance_client()

        # Handle MARKET order
        if user_inputs.order_type == "MARKET":
            order_response = place_market_order(
                trading_client=trading_client,
                trading_symbol=user_inputs.symbol,
                order_side=user_inputs.side,
                order_quantity=user_inputs.quantity
            )

        # Handle LIMIT order
        elif user_inputs.order_type == "LIMIT":
            if user_inputs.price is None:
                raise ValueError("Price must be provided for LIMIT orders")

            order_response = place_limit_order(
                trading_client=trading_client,
                trading_symbol=user_inputs.symbol,
                order_side=user_inputs.side,
                order_quantity=user_inputs.quantity,
                limit_price=user_inputs.price
            )

        # Print order summary
        print("\nORDER PLACED SUCCESSFULLY")
        print(f"Order ID: {order_response.get('orderId', 'N/A')}")
        print(f"Status: {order_response.get('status', 'N/A')}")
        print(f"Executed Quantity: {order_response.get('executedQty', 'N/A')}")
        print(f"Average Price: {order_response.get('avgPrice', 'N/A')}")

    except Exception as error:
        app_logger.error(f"Order execution failed: {error}")
        print("\nOrder failed. Please check logs for more details.")
        print(error)


if __name__ == "__main__":
    main()
