import setuptools

long_description = ''

setuptools.setup(
	name='reverse-kafka-logger',
	version='0.1.2',
	packages=setuptools.find_packages(),
	long_description=open('README.md').read(),
	entry_points={
		'console_scripts': ['reverse-kafka-logger=logger.grep_interface:run_grep_command'],
	},
	install_requires=[
		'click',
	],
	author="Edward Sujono",
	description="grep kafka message reversely from the end offset to start offset",
	long_description_content_type="text/markdown",
	url="https://github.com/edwardsujono/kafka-logger",
	classifiers=[
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
