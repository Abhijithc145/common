import pika, json
import logging
from activity_service.config import config as cfg

def publish_event(message, queue_name):
    
    print("in event")
    
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
    conn = pika.BlockingConnection(parameters)
    channel = conn.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange="", routing_key=queue_name, body=json.dumps(message))
    print(message,"26", "26")
    conn.close()


