import logging
from binance.client import Client

# Logger for order-related operations
order_logger = logging.getLogger(__name__)


def place_market_order(
    trading_client: Client,
    trading_symbol: str,
    order_side: str,
    order_quantity: float
):
    """
    Places a MARKET order on Binance Futures Testnet.
    """
    try:
        order_logger.info(
            f"Placing MARKET order | Symbol={trading_symbol}, "
            f"Side={order_side}, Quantity={order_quantity}"
        )

        # Place market order
        trading_client.futures_create_order(
            symbol=trading_symbol,
            side=order_side,
            type="MARKET",
            quantity=order_quantity
        )

        # Fetch recent trades to confirm execution
        recent_trades = trading_client.futures_account_trades(
            symbol=trading_symbol
        )

        if recent_trades:
            latest_trade = recent_trades[-1]
            order_logger.info(
                f"Trade execution confirmed: {latest_trade}"
            )
            return latest_trade

        order_logger.warning(
            "Market order placed but trade details not available yet"
        )
        return {}

    except Exception as error:
        order_logger.error(
            f"Market order placement failed: {error}"
        )
        raise


def place_limit_order(
    trading_client: Client,
    trading_symbol: str,
    order_side: str,
    order_quantity: float,
    limit_price: float
):
    """
    Places a LIMIT order on Binance Futures Testnet.
    """
    try:
        order_logger.info(
            f"Placing LIMIT order | Symbol={trading_symbol}, "
            f"Side={order_side}, Quantity={order_quantity}, Price={limit_price}"
        )

        order_response = trading_client.futures_create_order(
            symbol=trading_symbol,
            side=order_side,
            type="LIMIT",
            quantity=order_quantity,
            price=limit_price,
            timeInForce="GTC",
            newOrderRespType="RESULT"
        )

        order_logger.info(
            f"Limit order response received: {order_response}"
        )
        return order_response

    except Exception as error:
        order_logger.error(
            f"Limit order placement failed: {error}"
        )
        raise
