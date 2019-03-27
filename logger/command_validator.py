def validate_grep_input(**kwargs):
	if kwargs.get('topic') is None:
		raise ValueError('please input topic name')
	elif kwargs.get('brokers') is None:
		raise ValueError('please input brokers')