import time
 
from kafka import SimpleProducer, KafkaClient
from kafka.common import LeaderNotAvailableError
 
if __name__ == "__main__":
    kafka = KafkaClient("192.168.33.10:9092")
    producer = SimpleProducer(kafka)
 
    topic = b'foobar'
    msg = b'Hello World'
 
    try:
        print str(producer.send_messages(topic, msg))
    except LeaderNotAvailableError:
        time.sleep(1)
        print str(producer.send_messages(topic, msg))
 
    kafka.close()
