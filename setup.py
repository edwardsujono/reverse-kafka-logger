from distutils.core import setup

setup(
	name='kafka-logger',
	version='0.1dev',
	packages=['logger'],
	long_description=open('README.txt').read(),
	entry_points={
		'console_scripts': ['grep=logger.grep_manager:run_grep_command'],
	},
)
