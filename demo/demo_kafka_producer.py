from kafka import KafkaProducer

from demo.config import KAFKA_CONFIG


def produce_messages(n_messages):
	kafka_producer = KafkaProducer(
		bootstrap_servers=KAFKA_CONFIG['brokers'],
	)
	for i in range(n_messages):
		future = kafka_producer.send(KAFKA_CONFIG['topic'], b'raw_bytes')
		try:
			future.get(timeout=10)
		except Exception as e:
			print e
		kafka_producer.flush()


if __name__ == '__main__':
	produce_messages(1000)
