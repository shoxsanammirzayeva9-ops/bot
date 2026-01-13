
import asyncio
import os  # Tizim o'zgaruvchilari bilan ishlash uchun
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Tokenni GitHub Secrets'dan oladi
# Mahalliy kompyuterda ishlatmoqchi bo'lsangiz, o'rniga "TOKENINGIZNI_YOZING" qo'ying
TOKEN = os.getenv("8551813992:AAEfrfMFkYENIH-90-4vvg6n3QMbZNkjMZY")

# Agar token topilmasa, bot ishlamaydi (xavfsizlik uchun)
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
        # Xavfsizlik uchun faqat raqamlar va belgilarni tekshirish (ixtiyoriy)
        # eval() oddiy misollar uchun
        result = eval(message.text)
        await message.reply(f"Natija: {result}")
    except Exception:
        await message.reply("Xatolik! Faqat matematik amallarni yuboring (masalan: 10 + 5 / 2).")

async def main():
    print("Bot ishga tushdi...")
    # Botni ishga tushirish (polling)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
