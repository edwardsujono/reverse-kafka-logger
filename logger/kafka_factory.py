import uuid

from kafka import KafkaConsumer

kafka_consumer = None


def get_singleton_kafka_consumer(topic, broker_clusters):
	"""
	:param str topic: 'debug_topic'
	:param str broker_clusters: '129.0.0.1:2003,203.22.22.22:300'
	:return:
	"""
	global kafka_consumer
	if kafka_consumer is None:
		group_id = 'debug-{}'.format(str(uuid.uuid1()))
		kafka_consumer = KafkaConsumer(
			topic=topic,
			group_id=group_id,
			bootstrap_servers=[broker.strip(' ') for broker in broker_clusters.split(',')],
		)
	return kafka_consumer
