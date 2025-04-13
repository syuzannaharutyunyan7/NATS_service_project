import asyncio
import nats
from service_layer import process_message

async def nats_subscribe():
    try:
        nc = await nats.connect("nats://localhost:4222")
        print("Subscriber is running and waiting for messages on 'messages' subject...")

        async def message_handler(msg):
            print(f"Received message: {msg.data.decode()}")
            await process_message(msg.data.decode())

        await nc.subscribe("messages", cb=message_handler)
        await asyncio.Future()

    except Exception as e:
        print(f"Error while connecting to NATS: {e}")
    finally:
        if 'nc' in locals() and nc.is_connected:
            await nc.close()
            print("NATS connection closed.")

if __name__ == "__main__":
    asyncio.run(nats_subscribe())