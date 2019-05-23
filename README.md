# Fakestream

A program that fakes various kinds of data, and injects a stream of such fake events into Kafka.

This is used for testing various streaming scenarios.

## Setup

1. `pipenv install`
2. Install [librdfkafka prerequisites](https://github.com/confluentinc/confluent-kafka-python#prerequisites), according to your OS.


## Running

```
export CONFLUENT_API_KEY=(your key)
export CONFLUENT_API_SECRET=(your secret)
export KAFKA_BOOTSTRAP_SERVERS=(your server)

# Get usage information
pipenv run python3 fake.py  -h

# Send 100 messages of type "account" to topic "test"
pipenv run python3 fake.py --topic test -n 100 --type account
```