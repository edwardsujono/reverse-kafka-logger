import click
from logger import grep_manager


@click.command()
@click.option('--topic', default='', help='topic name')
@click.option('--brokers', default='', help='localhost:9092,localhost:9093')
@click.option('--regex', default='', help='in case you are not familiar with regex, you can use free text like usual')
def run_pfb_patcher(topic, brokers, regex):
	"""
	:param str topic:
	:param str brokers:
	:param str regex:
	:return:
	"""
	grep_manager.search_messages_in_parallel(
		topic=topic,
		brokers=brokers,
		regex=regex,
	)
