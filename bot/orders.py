import logging
from binance.client import Client

logger = logging.getLogger(__name__)

def place_market_order(client: Client, symbol: str, side: str, quantity: float):
    try:
        logger.info(
            f"Placing MARKET order | Symbol={symbol}, Side={side}, Quantity={quantity}"
        )

        client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        # Fetch recent trades to confirm execution
        trades = client.futures_account_trades(symbol=symbol)

        if trades:
            last_trade = trades[-1]
            logger.info(f"Fetched trade confirmation: {last_trade}")
            return last_trade

        logger.warning("Order placed but no trade data returned yet")
        return {}

    except Exception as e:
        logger.error(f"Failed to place MARKET order: {e}")
        raise
def place_limit_order(
    client: Client,
    symbol: str,
    side: str,
    quantity: float,
    price: float
):
    try:
        logger.info(
            f"Placing LIMIT order | Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
            newOrderRespType="RESULT"
        )

        logger.info(f"Order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Failed to place LIMIT order: {e}")
        raise
