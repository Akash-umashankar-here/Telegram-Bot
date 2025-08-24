import os
from telegram import Update
import asyncio
from datetime import datetime
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes
from telegram.error import TimedOut
now=datetime.now()
Token = os.getenv("Token")
async def start (update:Update,context:ContextTypes.DEFAULT_TYPE):
  await  update.message.reply_text("Hello")
async def help(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This bot will say whether the staff is in class or not")
def make_check_handler(greeting_message: str):
    async def check (update:Update,content:ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(greeting_message+"\n"+str(now.strftime("%I:%M:%S")))
    return check
def main(message):
    while True:
        try:
            application = ApplicationBuilder().token(f"{Token}").build()
            application.add_handler(CommandHandler("start", start))
            application.add_handler(CommandHandler("help", help))
            check_handler=make_check_handler(message)
            application.add_handler(CommandHandler("check", check_handler))
            application.run_polling()
            break
        except TimedOut:
            print("Timed out, retrying in 5 seconds...")
            asyncio.sleep(5)

if __name__ == '__main__':
  message = "hi"
  asyncio.run(main(message))



