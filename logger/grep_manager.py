import re
from collections import defaultdict
from multiprocessing import Process

from kafka import TopicPartition

from logger import kafka_factory
from logger.constant import BATCH_SIZE


def search_messages_in_parallel(topic, brokers, regex):
	"""
	Messages will be searched in parallel by spawning process per partition.
	:param topic:
	:param brokers:
	:param regex:
	:return:
	"""
	n_partition = _get_n_partition(brokers, topic)
	kafka_consumer = kafka_factory.generate_kafka_consumer(brokers)
	partition_id_to_start_end_offset = _get_partition_info(kafka_consumer, topic, n_partition)
	for partition in xrange(n_partition):
		p = Process(
			target=_reverse_search_log_per_partition,
			args=(brokers, topic, partition, partition_id_to_start_end_offset, regex),
		)
		p.start()
		p.join()


def _get_partition_info(kafka_consumer, topic, n_partition):
	partition_to_offset_info = defaultdict(dict)
	partitions = [TopicPartition(topic, partition) for partition in xrange(n_partition)]
	beginning_offsets = kafka_consumer.beginning_offsets(partitions)
	for topic_partition, offset in beginning_offsets.items():
		partition_to_offset_info[topic_partition.partition].update({'start_offset': offset})

	end_offsets = kafka_consumer.end_offsets(partitions)
	for topic_partition, offset in end_offsets.items():
		partition_to_offset_info[topic_partition.partition].update({'end_offset': offset})

	return partition_to_offset_info


def _reverse_search_log_per_partition(
	brokers,
	topic,
	partition,
	partition_id_to_start_end_offset,
	regex,
):
	"""
	This works by using a sliding window mechanism
	---------------------------
	1 2 3 4 5 6 7 8 9 10 11 12
							^
	Normal reading kafka starts from the beginning offset to the end
	we can seek the offset one by one, but there is an overhead of network
	to call the kafka broker, so the idea is to batch get the messages
	:param list[str] brokers:
	:param str topic:
	:param int partition:
	:param str regex:
	:return:
	"""
	"""
		Kafka consumer can only be instantiated when the sub-process is spawned otherwise the socket is closed
	"""
	kafka_consumer = kafka_factory.generate_kafka_consumer(brokers, is_singleton=False)
	start_offset = partition_id_to_start_end_offset[partition]['start_offset']
	end_offset = partition_id_to_start_end_offset[partition]['end_offset']
	print 'start_offset: {}, end_offset: {}'.format(start_offset, end_offset)
	kafka_consumer.assign([TopicPartition(topic, partition)])
	for offset in range(end_offset, start_offset - 1, -BATCH_SIZE):
		start_read_offset, end_read_offset = _get_start_end_offset(offset, start_offset)
		# assign partition and offset to the kafka consumer
		print 'start_read_offset: {}, end_read_offset: {}, assigned_offset: {}'.format(start_read_offset, end_read_offset, offset)
		kafka_consumer.seek(
			partition=TopicPartition(topic, partition),
			offset=start_read_offset,
		)
		grep_messages_in_batch(kafka_consumer, regex, start_read_offset, end_read_offset)


def _get_start_end_offset(offset, start_offset):
	"""
	start offset might be less than the offset that can be read. Depending with
	the configuration, messages are saved only in particular time period.
	:param offset:
	:param start_offset:
	:return:
	"""
	start_read_offset = offset - BATCH_SIZE
	end_read_offset = offset
	if start_read_offset < start_offset:
		start_read_offset = start_offset
	return start_read_offset, end_read_offset


def grep_messages_in_batch(kafka_consumer, regex, start_offset, end_offset):
	"""
	KafkaConsumer poll --> works by using intern
	:param KafkaConsumer kafka_consumer:
	:param str regex:
	:param int start_offset:
	:param int end_offset:
	:return:
	"""
	for _ in range(start_offset, end_offset):
		message = next(kafka_consumer)
		if re.match(regex, message.value):
			print 'message: {}'.format(message)


def _get_n_partition(brokers, topic):
	"""
	:param brokers:
	:param topic:
	:return:
	"""
	kafka_consumer = kafka_factory.generate_kafka_consumer(brokers, is_singleton=False)
	kafka_consumer.subscribe(topics=[topic])
	kafka_consumer.topics()
	return len(kafka_consumer.partitions_for_topic(unicode(topic)))
