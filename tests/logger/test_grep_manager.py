import pytest


class MockKafkaConsumer(object):
	def __init__(self):
		self.count = 0

	def assign(self):
		# MOCK
		return

	def seek(self):
		# MOCK
		return

	def __iter__(self):
		while True:
			yield 'message_{}'.format(self.count)
			self.count += 1


class TestGrepManager(object):
	@pytest.mark.parametrize('test_case', [
		# batch size exactly matches the number of messages
		{
			'start_offset': 0,
			'end_offset': 10,
			'batch_size': 5,
			'expected_matched_messages': ['message_{}'.format(i) for i in range(10)]
		}
		# batch size "NOT" exactly matches the number of messages
	])
	def test_grep_manager(self, mocker, test_case):
		assert True

	@staticmethod
	def _given_kafka_consumer_is_mocked(mocker):
		mocker.patch(
			'logger.grep_manager.kafka_factory.generate_kafka_consumer',
			return_value=MockKafkaConsumer()
		)

	@staticmethokd
	def _given_batch_size_is_mocked(mocker, batch_size):
		mocker.patch('logger.grep_manager.BATCH_SIZE', return_value=batch_size)
