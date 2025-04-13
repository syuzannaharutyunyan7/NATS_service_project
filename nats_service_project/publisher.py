import asyncio
import nats

async def run():
    nc = await nats.connect("nats://localhost:4222")

    while True:
        msg = input("Enter message to send (or type 'exit' to quit): ")
        if msg.lower() == "exit":
            break
        await nc.publish("messages", msg.encode())
        await nc.flush()
        print("Message sent!")

    await nc.close()

if __name__ == "__main__":
    asyncio.run(run())
