import asyncio

async def process_transaction_async(transaction):
    await asyncio.sleep(1)
    if transaction.process_transaction("Miner1"):
        print("Transaction processed!")
    else:
        print("Error processing transaction.")

async def run_load_test():
    transaction1 = Transaction("User1", "User2", 20, 2, wallet, user1_public_key, user1_private_key)
    transaction2 = Transaction("User3", "User4", 15, 1.5, wallet, user3_public_key, user3_private_key)
    await asyncio.gather(process_transaction_async(transaction1), process_transaction_async(transaction2))

asyncio.run(run_load_test())
