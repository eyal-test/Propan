from typing import Optional, Union

from propan.brokers.rabbit.schemas import RabbitExchange, RabbitQueue


def validate_exchange(
    exchange: Union[str, RabbitExchange, None] = None,
) -> Optional[RabbitExchange]:
    if exchange is not None:  # pragma: no branch
        if isinstance(exchange, str):
            exchange = RabbitExchange(name=exchange)
        elif not isinstance(exchange, RabbitExchange):
            raise ValueError(
                f"Exchange '{exchange}' should be 'str' | 'RabbitExchange' instance"
            )
    return exchange


def validate_queue(
    queue: Union[str, RabbitQueue, None] = None
) -> Optional[RabbitQueue]:
    if queue is not None:  # pragma: no branch
        if isinstance(queue, str):
            queue = RabbitQueue(name=queue)
        elif not isinstance(queue, RabbitQueue):
            raise ValueError(
                f"Queue '{queue}' should be 'str' | 'RabbitQueue' instance"
            )
    return queue
