import asyncio

from sqlalchemy import Column, Table, MetaData, select, String, URL, Engine
from sqlalchemy.ext.asyncio import create_async_engine

url = URL.create(
    drivername="postgresql+asyncpg",
    username="postgres",
    host="192.168.0.8",
    port="5432",
    password="1234",
    database="tests"
)
meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


async def async_main() -> None:
    engine = create_async_engine(
        url,
        echo=True,
    )
    print(engine)

    # async with engine.begin() as conn:
    # await conn.run_sync(meta.create_all)

    # await conn.execute(
    # t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
    # )

    """
    ME : engine.begin() خودش کامیت رو انجام میده گویا اگر با engine.connect() بریم خواهیم داشت : 
    async with engine.connect() as conn:
        await conn.run_sync(meta.create_all)

        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )

        await conn.commit()
    """
    async with engine.connect() as conn:
        # select a Result, which will be delivered with buffered
        # results
        result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))

        for r in result:
            print(r)

    async with engine.connect() as conn:
        async_result = await conn.stream(select(t1))

        async for row in async_result:
            print("row: %s" % (row,))

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())
