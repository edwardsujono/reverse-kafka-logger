import pytest

from logger import grep_manager


class MockValue(object):
	def __init__(self, value):
		self.value = value


class MockKafkaConsumer(object):
	def __init__(self):
		self.count = -1

	def assign(self, mock_topic_partition):
		# MOCK
		return

	def seek(self, partition, offset):
		# MOCK
		return

	def next(self):
		return self.__next__()

	def __next__(self):
		while True:
			self.count += 1
			return MockValue('message_{}'.format(self.count))


class TestGrepManager(object):
	@pytest.mark.parametrize('test_case', [
		# batch size exactly matches the number of messages
		{
			'start_offset': 0,
			'end_offset': 10,
			'batch_size': 5,
			'expected_matched_messages': ['message_{}'.format(i) for i in range(10)]
		},
		# batch size "NOT" exactly matches the number of messages
		{
			'start_offset': 0,
			'end_offset': 9,
			'batch_size': 5,
			'expected_matched_messages': ['message_{}'.format(i) for i in range(9)]
		}
	])
	def test_grep_manager(self, mocker, test_case):
		# GIVEN
		# WHEN
		self._given_batch_size_is_mocked(mocker, test_case['batch_size'])
		self._given_kafka_consumer_is_mocked(mocker)
		# THEN
		assert grep_manager._reverse_search_log_per_partition(
			brokers=[],
			topic='topic-test',
			partition=1,
			partition_id_to_start_end_offset={
				1: {
					'start_offset': test_case['start_offset'],
					'end_offset': test_case['end_offset'],
				}
			},
			regex='',
		) == test_case['expected_matched_messages']

	@staticmethod
	def _given_kafka_consumer_is_mocked(mocker):
		mocker.patch(
			'logger.grep_manager.kafka_factory.generate_kafka_consumer',
			return_value=MockKafkaConsumer()
		)

	@staticmethod
	def _given_batch_size_is_mocked(mocker, batch_size):
		from logger import grep_manager
		grep_manager.BATCH_SIZE = batch_size
