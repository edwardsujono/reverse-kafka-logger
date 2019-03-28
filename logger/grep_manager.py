import re

from kafka import TopicPartition

from logger import kafka_factory
from logger.constant import BATCH_SIZE


def search_messages_in_parallel(topic, brokers):
	n_partition = _get_n_partition(brokers, topic)
	kafka_consumer = kafka_factory.generate_kafka_consumer(brokers)
	partition_id_to_start_end_offset = _get_partition_info(kafka_consumer, n_partition)
	for partition in xrange(n_partition):
		_reverse_search_log_per_partition(kafka_consumer, topic, partition)


def _get_partition_info(kafka_consumer, n_partition):
	partitions = [partition for partition in n_partition]
	beginning_offsets = kafka_consumer.beginning_offsets(partitions)
	end_offsets = kafka_consumer.end_offsets(partitions)
	return {
		i: {
			'start_offset': beginning_offsets[i],
			'end_offset': end_offsets[i],
		} for i in xrange(n_partition),
	}


def _reverse_search_log_per_partition(
	kafka_consumer,
	topic,
	partition,
	partition_id_to_start_end_offset,
):
	"""
	This works by using a sliding window mechanism
	---------------------------
	1 2 3 4 5 6 7 8 9 10 11 12
							^
	Normal reading kafka starts from the beginning offset to the end
	we can seek the offset one by one, but there is an overhead of network
	to call the kafka broker, so the idea is to batch get the messages
	:param KafkaConsumer kafka_consumer:
	:param str topic:
	:param int partition:
	:return:
	"""
	start_offset = partition_id_to_start_end_offset[partition]['start_offset']
	end_offset = partition_id_to_start_end_offset[partition]['end_offset']
	offset = start_offset
	kafka_consumer.assign([TopicPartition(topic, partition)])

	for offset in range(end_offset, start_offset - 1, -BATCH_SIZE):
		start_read_offset = offset - BATCH_SIZE
		end_read_offset = offset
		if start_read_offset - BATCH_SIZE < start_offset:
			start_read_offset = start_offset

		kafka_consumer.seek(
			partition=partition,
			offset=offset
		)

	if offset < start_offset:


def grep_messages_in_batch(kafka_consumer, regex, batch_size=BATCH_SIZE):
	"""
	KafkaConsumer poll --> works by using intern
	:param KafkaConsumer kafka_consumer:
	:param str regex:
	:param int batch_size:
	:return:
	"""
	counter = 0
	while counter < BATCH_SIZE:
		message = kafka_consumer.poll(0.0001)
		counter += 1


def _get_n_partition(brokers, topic):
	"""
	:param brokers:
	:param topic:
	:return:
	"""
	kafka_consumer = kafka_factory.generate_kafka_consumer(brokers, is_singleton=False)
	kafka_consumer.subscribe(topics=[topic])
	return len(kafka_consumer.partitions_for_topic(unicode(topic)))
