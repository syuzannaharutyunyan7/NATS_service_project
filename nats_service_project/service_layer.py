from data_layer import save_message

async def process_message(content):
    print(f"Processing message: {content}")
    await save_message(content)