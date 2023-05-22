from loader import dp, bot
from handlers.utils.db_api import quick_commands as commands

import asyncio
import aioschedule

async def notice():
    users = await commands.select_all_users()
    for user in users:
        text = f'{user.first_name}, давно не виделись)'
        await bot.send_message(chat_id=user.user_id, text=text)

async def scheduler():
    aioschedule.every().day.at("13:00").do(notice)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
