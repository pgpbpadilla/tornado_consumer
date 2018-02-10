from invoke import task


@task
def down(ctx):
    """Shutdown all containers"""
    ctx.run('docker-compose down', echo=True)


@task
def up(ctx):
    """Start RabbitMQ, MongoDB and Tornado consumer."""
    ctx.run('docker-compose build')
    ctx.run('docker-compose up -d', echo=True)


@task(pre=[up])
def publish(ctx):
    """Boot up all containers and start publishing messages to RabbitMQ."""
    print('Waiting for containers to be ready')
    ctx.run('sleep 30', echo=True);
    ctx.run('python publisher/rmq_publisher.py', echo=True)

