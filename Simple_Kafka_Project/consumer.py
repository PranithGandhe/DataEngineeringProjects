# consumer.py
from kafka import KafkaConsumer
import json

# Create Kafka Consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🔁 Listening for messages...")

# Listen and print messages
for message in consumer:
    print("Received:", message.value)

