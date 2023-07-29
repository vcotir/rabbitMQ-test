import pika # pure-python implementation of AMQP protocol

def test_rabbitmq_url(url):
    try:
        params = pika.URLParameters(url)
        conn = pika.BlockingConnection(params)
        conn.close();
        print("connection successful")
    except pika.exceptions.AMQPError as e:
        print("connection fialed", e)

test_rabbitmq_url("amqp://testuser:testpassword@localhost:5672/Example")