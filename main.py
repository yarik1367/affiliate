from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

bot = Bot(token="6411528429:AAEeCr4bYfV3GAK-zXV0O3w90CzOCFcqDnU")
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

# Здесь список зарегистрированных ID (в идеале хранить в БД)
registered_traders = set()

@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    link = "https://po.cash/register/?utm_source=telegram_bot&a=T2ye3EBrPxd4Se&ac=postbacks-test&click_id={click_id}&site_id=telegram"
    await message.answer(f"Привет! Зарегистрируйся по ссылке:\n{link}\n\nПосле регистрации отправь мне свой ID (trader_id).")

@dp.message_handler()
async def handle_trader_id(message: Message):
    trader_id = message.text.strip()
    if trader_id in registered_traders:
        await message.answer("✅ Ты успешно зарегистрирован!")
    else:
        await message.answer("⛔️ Я пока не получил информацию о твоей регистрации. Попробуй позже.")

# Эндпоинт для симуляции получения postback (вместо отдельного сервера)
@dp.message_handler(commands=["mock_postback"])
async def mock_postback(message: Message):
    trader_id = message.get_args()
    registered_traders.add(trader_id)
    await message.answer(f"🛰 Trader ID {trader_id} зарегистрирован (тестово добавлен).")

if __name__ == "__main__":
    asyncio.run(main())

