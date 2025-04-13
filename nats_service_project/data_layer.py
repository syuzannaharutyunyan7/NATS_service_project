import psycopg2
from psycopg2 import sql, OperationalError, errors
import asyncio

def create_table_if_not_exists(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            print("Table 'messages' checked/created.")
    except Exception as e:
        print(f"Error creating table: {e}")

async def save_message(content):
    try:
        conn = psycopg2.connect(
            dbname="nats_service_db",
            user="postgres",
            password="syuzanna.",
            host="localhost"
        )

        create_table_if_not_exists(conn)

        with conn.cursor() as cur:
            cur.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
            conn.commit()
            print(f"Message saved: {content}")

    except OperationalError as e:
        print(f"Database connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
