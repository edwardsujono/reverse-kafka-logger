import uuid

from kafka import KafkaConsumer

kafka_consumer = None


def generate_kafka_consumer(brokers, is_singleton=True):
	"""
	:param str brokers: '129.0.0.1:2003,203.22.22.22:300'
	:param is_singleton: create only single reference when the flag is on
	:return:
	"""
	global kafka_consumer
	if not is_singleton:
		return _init_kafka_consumer(brokers)
	if kafka_consumer is None:
		kafka_consumer = _init_kafka_consumer(brokers)
	return kafka_consumer


def _init_kafka_consumer(brokers):
	group_id = 'debug-{}'.format(str(uuid.uuid1()))
	return KafkaConsumer(
		group_id=group_id,
		bootstrap_servers=[broker.strip(' ') for broker in brokers.split(',')],
		enable_auto_commit=False,
	)


def clear_kafka_consumer():
	"""
	Clear the singleton object
	:return:
	"""
	global kafka_consumer
	kafka_consumer = None
