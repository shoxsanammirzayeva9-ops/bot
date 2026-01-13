import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# BU YERNI DIQQAT BILAN KO'RING: 
# os.getenv ichida token emas, nomi bo'lishi kerak!
TOKEN = os.getenv(""8551813992:AAEfrfMFkYENIH-90-4vvg6n3QMbZNkjMZ")

if not TOKEN:
    exit("Xatolik: BOT_TOKEN topilmadi! GitHub Secrets'ni tekshiring.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom! Menga misol yuboring (masalan: 25 * 4), men uni hisoblab beraman.")

@dp.message()
async def calculate_handler(message: types.Message):
    try:
        # Faqat matematik amallar ekanligini tekshirish xavfsizlik uchun yaxshi
        result = eval(message.text)
        await message.reply(f"Natija: {result}")
    except Exception:
        await message.reply("Xatolik! Faqat matematik amallarni yuboring (masalan: 10 + 5 / 2).")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
