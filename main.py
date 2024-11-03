from bot import dp, bot
import asyncio
from handlers import router

async def main():
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())