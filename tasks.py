from invoke import task
import consumer

@task
def up(ctx):
    ctx.run('docker-compose up -d', echo=True)


@task
def publish(ctx):
    ctx.run('python publisher/rmq_publisher.py')


@task
def consume(ctx):
    ctx.run('python consumer.py')
