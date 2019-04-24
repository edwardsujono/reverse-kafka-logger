import click

from logger import command_validator
from logger import grep_manager


@click.command()
@click.option('--topic', default=None, help='topic name')
@click.option('--brokers', default=None, help='broker cluster, separate with comma for each broker')
@click.option('--regex', default='', help='regex to be matched with the message')
def run_grep_command(topic, brokers, regex):
	try:
		command_validator.validate_grep_input(**locals())
		grep_manager.search_messages_in_parallel(topic, brokers, regex)
	except ValueError as e:
		print e

