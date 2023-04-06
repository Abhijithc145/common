import pika, json
from activity_service.config import config as cfg
import logging
from BaseWorke.middlewares.new_relic_middleware import get_logger

logger = get_logger()


ACTIVITY_CREATED_ROUTING_KEY = "Activity.Activity.Created"
AUDIT_EXCHANGE = "AUDIT"


def publish_event(
    message, routing_key=ACTIVITY_CREATED_ROUTING_KEY, exchange=AUDIT_EXCHANGE
):
    EXCHANGE = AUDIT_EXCHANGE
    credentials = pika.PlainCredentials(
        cfg.get("rabbit_mq", "USER_NAME"), cfg.get("rabbit_mq", "PASSWORD")
    )
    parameters = pika.ConnectionParameters(
        host=cfg.get("rabbit_mq", "HOST"),
        virtual_host=cfg.get("rabbit_mq", "VIRTUAL_HOST"),
        credentials=credentials,
        frame_max=int(cfg.get("rabbit_mq", "FRAME_MAX")),
        heartbeat=int(cfg.get("rabbit_mq", "HEART_BEAT")),
        connection_attempts=int(cfg.get("rabbit_mq", "CONNECTION_ATTEMPTS")),
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, exchange_type="topic")

    channel.basic_publish(
        exchange=EXCHANGE,
        routing_key=routing_key,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,
        ),
    )

    logger = get_logger()
    logger.info(
        "EVENT SUCCESFULLY PUBLISHED TO "
        + EXCHANGE
        + "\n ROUTING KEY"
        + routing_key
        + "\n CURRENT PAYLOAD \n"
        + str(message)
    )

    connection.close()
