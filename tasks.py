from invoke import task


@task
def up(ctx):
    ctx.run('docker-compose up -d', echo=True)
