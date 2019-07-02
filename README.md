# Kafka Logger
<a href="https://travis-ci.com/edwardsujono/reverse-kafka-logger.svg?branch=master"><img src="https://travis-ci.com/edwardsujono/reverse-kafka-logger.svg?branch=master" alt="Build Status"></a>

```text
pip library that is used to read inversely the kafka message.
The best part is each partition of topic will be run in parallel.
```

# Background

A need to grep the message from kafka reversely because often we want to grep something from the most recent offset.

# Problem
All the available debugging tools of kafka never introduced such feature.

# usage
`pip install rervese-kafka-logger`

# Install
setup package: `python setup.py dist`

install package: `pip install --no-index ./dist/{NEW_PACKAGE_NAME}`
