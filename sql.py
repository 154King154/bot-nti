import asyncio
import asyncpg
import logging
from token_telegram import PG_USER, PG_PASS, host, database, port


async def create_db():
    create_db_command = open("create_db.sql", "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(user=PG_USER,
                                                     password=PG_PASS,
                                                     database=database,)
                                                     #host=host,
                                                     #port=port)
    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table users created")


async def create_pool():
    return await asyncpg.create_pool(user=PG_USER,
                                     password=PG_PASS,
                                     database=database,)
                                     #host=host,
                                     #port=port)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())