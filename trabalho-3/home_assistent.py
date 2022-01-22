import pika, sys, os
import smart_obj_pb2 as SmartObject

# Instânciando um 
sensor = SmartObject.SmartObject()

# Variável teste para status da lampada
status_lamp = 'OFF'

def main():
    connection_temp = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel_temp = connection_temp.channel()
    channel_temp.exchange_declare(exchange='temp_log', exchange_type='fanout')
    result_temp = channel_temp.queue_declare(queue='', exclusive=True)
    queue_name_temp = result_temp.method.queue
    channel_temp.queue_bind(exchange='temp_log', queue=queue_name_temp)

    connection_luz = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel_luz = connection_luz.channel()
    channel_luz.exchange_declare(exchange='luz_log', exchange_type='fanout')
    result_luz = channel_luz.queue_declare(queue='', exclusive=True)
    queue_name_luz = result_luz.method.queue
    channel_luz.queue_bind(exchange='luz_log', queue=queue_name_luz)


    # --- Rotina da fila
    def callback_temp(ch, method, properties, body):
        sensor.ParseFromString(body)
        print(sensor.data)

    def callback_luz(ch, method, properties, body):
        sensor.ParseFromString(body)
        print(sensor.data)


    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel_temp.basic_consume(
        queue=queue_name_temp, on_message_callback=callback_temp, auto_ack=True)

    channel_temp.start_consuming()
    print('teste')
    channel_luz.basic_consume(
        queue=queue_name_luz, on_message_callback=callback_luz, auto_ack=True)

    channel_luz.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

#protoc -I=. --python_out=. ./todolist.proto