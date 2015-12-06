from kafka import KafkaConsumer
 
if __name__ == "__main__":
    consumer = KafkaConsumer(b"foobar", group_id=b"my_group_id",
                             metadata_broker_list=["192.168.33.10:9092"])
    for message in consumer:
        # This will wait and print messages as they become available
        print(message)
