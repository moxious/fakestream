from confluent_kafka import Producer
import uuid
import os
import json

debug = False

# Docs:
# https://docs.confluent.io/current/clients/confluent-kafka-python/

def get_or_default_env(env_var, default=''):
    try:
        return os.environ[env_var]
    except KeyError:
        return default

def acked(err, msg):
    """Delivery report callback called (from flush()) on successful or failed delivery of the message."""
    if err is not None:
        print("failed to deliver message: {}".format(err.str()))
    else:
        print("topic {} => [part:{}] @ offset:{}".format(msg.topic(), msg.partition(), msg.offset()))

confluent_cloud = 'pkc-epgnk.us-central1.gcp.confluent.cloud:9092'

try:
    bootstrap = os.environ['KAFKA_BOOTSTRAP_SERVERS']
    username = os.environ['CONFLUENT_API_KEY']
    password = os.environ['CONFLUENT_API_SECRET']
except KeyError:
    raise Exception("You must define env vars KAFKA_BOOTSTRAP_SERVERS, CONFLUENT_API_KEY, and CONFLUENT_API_SECRET")

local = False

config = {
    'bootstrap.servers': bootstrap,
    'broker.version.fallback': '0.10.0.0',
    'api.version.fallback.ms': 0,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': username,
    'sasl.password': password
}

print("Kafka config: %s" % json.dumps(config, indent=3))

p = Producer(config)

def kafka_flush():
    return p.flush()

def kafka_send(topic, entry, callback=acked):
    if not topic or not entry:
        raise Exception('Topic and entry must be good')

    r = p.produce(topic=topic, value=str(entry).encode('utf-8'), callback=callback)
    p.poll(0)
    return r