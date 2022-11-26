import asyncio


async def do_gather(*coroutines, cancel_exc):
    pending = list(map(asyncio.ensure_future, coroutines))
    try:
        await asyncio.gather(*pending)
    except cancel_exc:
        for t in pending:
            t.cancel()
