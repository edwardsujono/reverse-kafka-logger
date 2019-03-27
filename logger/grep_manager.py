import click

from logger import kafka_factory
from logger import command_validator


@click.command()
@click.option('--topic', default=None, help='topic name')
@click.option('--brokers', default=None, help='broker cluster, separate with comma for each broker')
def run_grep_command(topic, brokers):
	kafka_consumer = kafka_factory.get_singleton_kafka_consumer()
