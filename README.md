# Kafka Logger
<a href="https://travis-ci.com/edwardsujono/reverse-kafka-logger.svg?branch=master"><img src="https://travis-ci.com/edwardsujono/reverse-kafka-logger.svg?branch=master" alt="Build Status"></a>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

pip library that is used to read inversely the kafka message.
The best part is each partition of topic will be run in parallel.

# Background

A need to grep the message from kafka reversely because often we want to grep something from the most recent offset.

# Problem
All the available debugging tools of kafka never introduced a feature to easily grep the message from the latest offset to
the beginning of the offset. Thus, I created this open source project.

# usage
`pip install rervese-kafka-logger`

`reverse-kafka-logger --topic='topic' --brokers='localhost:9092,localhost:9093' --regex='search this' `

# Install
setup package: `python setup.py dist`

install package: `pip install --no-index ./dist/{NEW_PACKAGE_NAME}`
