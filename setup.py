import setuptools

long_description = ''

setuptools.setup(
	name='kafka-logger',
	version='0.1dev',
	packages=['logger'],
	long_description=open('README.txt').read(),
	entry_points={
		'console_scripts': ['grep=logger.grep_interface:run_grep_command'],
	},
	install_requires=[
		'click',
	],
	author="Shopee Checkout Dev",
	description="Collection of script that help you to execute many things",
	long_description_content_type="text/markdown",
	url="https://git.garena.com/candinegarae/git_mr",
	classifiers=[
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
