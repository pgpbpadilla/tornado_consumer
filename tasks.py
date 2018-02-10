from invoke import task


@task
def up(ctx):
    ctx.run('docker-compose up -d', echo=True)


@task
def publish(ctx):
    ctx.run('python publisher/rmq_publisher.py')


@task
def consume(_):
    import pika
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    exchange = 'test-exchange'
    channel.exchange_declare(
        exchange=exchange,
        exchange_type='fanout',
        auto_delete=True
    )
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=exchange, queue=queue_name)
    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % body)

    channel.basic_consume(
        callback,
        queue=queue_name,
        no_ack=True
    )
    channel.start_consuming()
