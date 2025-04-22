# producer.py
from kafka import KafkaProducer
import json

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample data to send
data = {"user_id": 101, "action": "click", "product": "Shoes"}

# Send to Kafka topic
producer.send('test-topic', value=data)

# Ensure it's sent
producer.flush()

print("Message sent to Kafka!")

