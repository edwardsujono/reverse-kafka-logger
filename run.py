"""
Entry point to test the script in the module
This file is for the sake of testing
"""
from logger import grep_manager


if __name__ == '__main__':
	# the demo script contains
	grep_manager.search_messages_in_parallel(
		topic='test_demo',
		brokers='localhost:9092',
		regex='raw_gg',
	)
