# NATS Service Project

A Python-based event-driven microservice application that demonstrates a **3-layered architecture (API, Service, Data)** using **NATS messaging** for communication and **PostgreSQL** for persistence.

---

## 📖 Overview

This application listens to messages published to a **NATS server** and saves them into a **PostgreSQL** database.

It is designed as a **lightweight demonstration of microservices architecture** with message-driven communication.

### The project consists of:

* **Publisher (`publisher.py`)** – a simple client that publishes test messages to a NATS subject.
* **API Layer** – subscribes to NATS subjects and receives messages.
* **Service Layer** – business logic for validating and processing messages.
* **Data Layer** – handles database operations to persist messages.
* **Main (`main.py`)** – the entry point that initializes the app and services.

---

## 🛠 Tech Stack

* **Language:** Python 3.10+
* **Messaging:** [NATS](https://nats.io/)
* **Database:** PostgreSQL
* **DevOps:** Docker + Docker Compose
* **Testing:** Pytest

---

## 📂 Project Structure

```
nats_service_project/
├── api/                   # API layer: subscribes to NATS
│   └── subscriber.py
├── service/               # Service layer: business logic
│   └── processor.py
├── data/                  # Data layer: PostgreSQL interactions
│   └── repository.py
├── tests/                 # Unit tests (pytest)
│   └── test_service.py
├── publisher.py           # Publisher client (sends test messages)
├── main.py                # Entry script (starts the app)
├── docker-compose.yml     # Docker services (NATS, PostgreSQL, app)
├── Dockerfile             # App container build
├── requirements.txt       # Python dependencies
├── LICENSE
└── README.md
```

---

## 📋 Prerequisites

Before running the project, ensure you have installed:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/)
* Python 3.10+ (only required if running outside Docker)
* PostgreSQL client (optional, for DB inspection)

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/syuzannaharutyunyan777/nats_service_project.git
cd nats_service_project
```

### 2. Run with Docker

```bash
docker-compose up --build
```

This will start:

* **NATS server** (default port: `4222`)
* **PostgreSQL database** (port: `5432`)
* **NATS service application**

---

## ▶️ Usage

1. Start the app with Docker as above.
2. In a new terminal, publish a test message with:

   ```bash
   python publisher.py
   ```
3. The message will flow through:

   * **Publisher → NATS → API Layer → Service Layer → Data Layer → PostgreSQL**

---

## 🧪 Running Tests

To verify the service layer logic:

```bash
pytest
```

---

## 📊 Example Flow

* Publisher sends a message:

  ```
  {"id": 1, "message": "Hello from Publisher!"}
  ```
* API Layer receives it from NATS.
* Service Layer processes and validates the message.
* Data Layer inserts the message into PostgreSQL.

---

## 📡 API & Messaging

| Component     | Function                         |
| ------------- | -------------------------------- |
| Publisher     | Sends messages to `subject.test` |
| API Layer     | Subscribes to `subject.test`     |
| Service Layer | Validates & processes messages   |
| Data Layer    | Persists messages in PostgreSQL  |

---

## 🚀 Features

* Event-driven architecture with **NATS**
* Clean **3-layer separation** (API, Service, Data)
* Persistent storage with **PostgreSQL**
* Simple publisher client for testing
* Containerized with **Docker Compose**
* Unit testing with **pytest**

---

## 📜 License

This project is licensed under the MIT License.

---

👩‍💻 **Author:** Syuzanna Harutyunyan

---


