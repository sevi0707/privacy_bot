import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Logging sozlamalari
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Bot tokeni
TOKEN = "9104802084:AAFYmrV6PKZLFBGbCZ29Ijbg4wuxzKGGdbE"

# Matnni raqamlarga (ASCII kodga) o'zgartiruvchi funksiya
async def encrypt_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_text = update.message.text

  # Har bir harfni uning raqamli kodiga o'zgartiramiz va bo'sh joy bilan ajratamiz
  encrypted_numbers = " ".join(str(ord(char)) for char in user_text)

  await update.message.reply_text(
      f"🔒 Maxfiy raqamlar:\n`{encrypted_numbers}`", parse_mode="Markdown"
  )


def main():
  application = ApplicationBuilder().token(TOKEN).build()

  # Matnli xabarlarni ushlab qolish
  handler = MessageHandler(filters.TEXT & (~filters.COMMAND), encrypt_text)
  application.add_handler(handler)

  print("Bot ishga tushdi...")
  application.run_polling()



