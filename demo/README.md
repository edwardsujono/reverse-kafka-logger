# Run kafka using Docker

Running kafka-cluster on your local can be quite tedious; Hence, it is good if we can spawn the
kafka cluster with its dependency in one command.

`docker-compose up -d`

Above command will run 2 services.
- Zookeeper
keep track the broker configuration, no need to expose any port to the external parties. 
Kafka can communicate with zookeeper using the internal docker bridge network.
- Kafka
kafka cluster needs to expose its port so that the outsider can publish or consume the message.