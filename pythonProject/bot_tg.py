from aiogram import types, executor, Dispatcher, Bot
from aiogram.utils.markdown import hbold, hlink
from config import token
from parss import result_json
import json


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.message):
    await bot.send_message(message.chat.id, "Привет, я покажу тебе меню")

@dp.message_handler(commands=["сеты"])
async def send_menu(message: types.message):
    await message.answer("please wating...")
    result_json()
    with open("result_data.json") as file:
        sety = json.load(file)
    for item in sety:
        card = f'{hlink(item.get("картинка"), item.get("имя"))}\n' \
        f'{hbold(item.get("цена"))}\n' \
        f'{hbold(item.get("состав"))}\n' \
        f'{hbold(item.get("описание"))}'
        print(card)
        await message.answer(card)

def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()