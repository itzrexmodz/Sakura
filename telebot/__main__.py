import glob
from telethon import TelegramClient, events
from telebot.telebotConfig import Var
from telebot.utils import load_module, start_mybot, load_pmbot
from pathlib import Path
import telethon.utils

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

async def add_bot(bot, bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done(bot):
    try:
        await bot.send_message(TELE, f"**TeleBot has been deployed.\nSend** `{CMD_HNDLR}alive` **to see if the bot is working.\n\nAdd** @{BOTNAME} **to this group and make it admin for enabling all the features of TeleBot**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

async def main():
    bot = TelegramClient("TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH)
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        await add_bot(bot, Var.TG_BOT_USER_NAME_BF_HER)
        print("Startup Completed")
    else:
        await bot.start()

    path = 'telebot/plugins/*.py'
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))

    print("TeleBot has been deployed! ")

    print("Setting up TGBot")
    path = "telebot/plugins/mybot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_mybot(shortname.replace(".py", ""))

    if LOAD_MYBOT == "True":
        path = "telebot/plugins/mybot/pmbot/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                load_pmbot(shortname.replace(".py", ""))
        print("TGBot set up completely!")

    print("TGBot set up - Level - Basic")
    print("TeleBot has been fully deployed! Do Visit @TeleBotSupport")
    await startup_log_all_done(bot)

    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
