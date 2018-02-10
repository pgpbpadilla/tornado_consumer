from invoke import task


@task
def down(ctx):
    ctx.run('docker-compose down', echo=True)


@task
def up(ctx):
    ctx.run('docker-compose up -d', echo=True)


@task
def publish(ctx):
    ctx.run('python publisher/rmq_publisher.py')


@task
def consume(ctx):
    ctx.run('python consumer.py')
