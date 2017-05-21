### Example of using Rabbit MQ to pass work to workers in a Docker Swarm

# 1. Build the images starting with python
# 2. docker-compose up in the notebook dir
# 3. ./start_stack.sh in the slave dir
# 4. Wait for the slaves to wake up (30 secs)
# 5. Run the notebook

### Architecture

Notebook -> Rabbit MQ -> Docker Swarm 

Docker Swarm:
    Slave1
    Slave2
    Slave3
    Slave...
    Slave12

### How it works

RabbitMQ starts up.
The slave nodes in the docker swarm start up and register with RabbitMQ for messages.
The notebook sends messages to Rabbit MQ.
RabbitMQ routes these messages to workers.
The workers perform their work and send the result back to RabbitMQ.
The notebook, which is listening for the result, is served it by RabbitMQ.
The notebook prints the result

