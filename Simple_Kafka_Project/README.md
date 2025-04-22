# Kafka Real-Time Messaging with Python

This project demonstrates a simple real-time messaging pipeline using **Apache Kafka** and **Python** on a local machine (MacBook). It's a great starter project for understanding how producers and consumers communicate using Kafka.

## Project Structure

A producer.py to produce messages and consumer.py to consume the messages.


## Prerequisites

- macOS with Homebrew installed
- Java (JDK 11 or higher)
- Apache Kafka (with Zookeeper)
- Python 3
- `kafka-python` package

## Setup Instructions

### 1. Install Kafka and Java

```bash
brew install openjdk@11
brew install kafka
```

Update your shell config:

```
echo 'export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
```

### 2. Start Kafka and Zookeeper

In Terminal Tab 1 (Zookeeper):

```bash
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

In Terminal Tab 2 (Kafka Broker):

```bash
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

### 3. Create a Kafka topic

```
kafka-topics --create --topic test-topic \
--bootstrap-server localhost:9092 \
--partitions 1 --replication-factor 1
```

## Running the python scripts

```
pip3 install kafka-python
python3 consumer.py
python3 producer.py
```

## Process

- producer.py sends a JSON message to the Kafka topic test-topic

- consumer.py listens on the same topic and prints any new messages

- Kafka handles the real-time transfer of the message between the two


