from api_layer import nats_subscribe
import asyncio

if __name__ == "__main__":
    asyncio.run(nats_subscribe())