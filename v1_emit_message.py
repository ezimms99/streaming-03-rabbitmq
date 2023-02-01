"""
    Emily Zimmerman - 1/31 - This program sends a message to the RabbitMQ server

    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# use the connection to create a communication channel
channel = connection.channel()
# use the channel to declare a queue
channel.queue_declare(queue="hello")
#Define the message you want to send
mymessage = 'Heyooo!'
# use the channel to publish a message to the queue
channel.basic_publish(exchange='', routing_key='hello', body=mymessage)
# print a message to the console for the user
print(" [x] Sent " + mymessage)
# close the connection to the server
connection.close()
