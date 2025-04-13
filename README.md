NATS Service Project

This project demonstrates a simple event-driven microservice architecture using a 3-layered structure (API, Service, and Data layers) connected through NATS messaging and backed by a PostgreSQL database. Additionally, I have implemented two supporting files, publisher.py and main.py. The first one acts like a test client sending messages, on the other hand main.py starts the app, it is the entry script. 

Project Description:

The application listens to messages published to a NATS server and saves them into a PostgreSQL database. It consists of the following key components:

Publisher: Sends messages to a NATS subject.
API Layer: Subscribes to the NATS subject and receives messages.
Service Layer: Handles the business logic of processing incoming messages.
Data Layer: Interacts with the PostgreSQL database to persist messages.

Docker: 

This project uses Docker and Docker Compose to easily manage the services needed for the application. 

Testing: 
I have added a basic test to check that the service layer processes messages correctly. Use pytest to run it.