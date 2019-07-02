import setuptools

long_description = ''

setuptools.setup(
	name='reverse-kafka-logger',
	version='0.1-dev-2',
	packages=setuptools.find_packages(),
	long_description=open('README.md').read(),
	entry_points={
		'console_scripts': ['reverse-kafka-logger=logger.grep_interface:run_grep_command'],
	},
	install_requires=[
		'click',
	],
	author="Edward Sujono",
	description="pip install reverse-kafka-logger; kafka-logger --topic='gg' --brokers='localhost9092;localhost:2928' --regex='wow'",
	long_description_content_type="text/markdown",
	url="https://github.com/edwardsujono/kafka-logger",
	classifiers=[
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
