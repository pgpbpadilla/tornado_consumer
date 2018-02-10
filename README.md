# System requirements

- Python 2.7
- Docker & Docker Compose 


# Quick start

- `inv -l` - List available tasks
- `inv -h <taskname>` - Help for specific task 

# Example usage:

- `inv publish`: 
    - start up the RabbitMQ, MongoDB and Tornado consumer as specified
in `docker-compose.yml`
    - run the `rmq_publisher.py` to start publishing messages to RabbitMQ.  
