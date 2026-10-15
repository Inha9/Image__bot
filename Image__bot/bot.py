import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from bot__btn import*
from bot__states import*
from bot__untils import make_img_filter
from database import *
import datetime


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '6107186803:AAHBpQQV7e29bkYX_AbSrue3ZUa7-iQgO3k'
ADMINS =[1068093091]

bot =Bot(token=BOT_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

async def on_start_bot(dispatcher):
    await create_table()

@dp.message_handler(commands=['start'])
async def start_bot_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    await create_user(user_id, username, today)
    btn = await start_menu_btn()
    await message.answer("Hello, This is bot for filter pictures", reply_markup=btn)

@dp.message_handler(commands=['admin'])
async def admin_handler(message: types.Message):
   user_id = message.from_user.id
   if user_id in ADMINS:
       all_users = await select_all_users()
       today_users = await select_today_users()
       await message.answer(f"Bot azolar: {all_users} ta\nBugun kirgan azolar: {today_users} ta\nKecha kirgan azolar: 2 ta")
   else:
       await message.answer("Siz admin emasiz!")
       await UserStates.mailing.set()

@dp.message_handler(state=UserStates.mailing, content_types=['text'])
async def mailing_to_users(message: types.Message):
    text = message.text
    users = await get_all_users()

    for user in users:
        await bot.send_message(chat_id=user[0], text=text)

@dp.message_handler(commands=['send'])
async def send_msg_all_users(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in ADMINS:
        await message.answer("Xabaringizni yuboring: ")

@dp.message_handler(text="🖼 Effects")
async def show_effects_handler(message: types.Message):
    btn = await effects_btn()
    await message.answer("chose effects", reply_markup=btn)

@dp.message_handler(text="⬅️ Back")
async def back_to_menu_handler(message: types.Message):
    await start_bot_handler(message)
    # btn = await start_menu_btn()
    # await message.answer("Hello, This is bot for filter pictures", reply_markup=btn)

@dp.message_handler()
async def select_filter_handler(message: types.Message, state: FSMContext):
    text = message.text
    if text in pillow__filters:
        await state.update_data(user_filter=text)
        await message.answer("Send photo:")
        await UserStates.get_img.set()

@dp.message_handler(state=UserStates.get_img,  content_types=['photo'])
async def get_img_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    filename = f"img_{user_id}.jpg"
    await message.photo[-1].download(destination_file=filename)
    msg_id = await message.answer("⏳")
    date = await state.get_data()
    result_img = await make_img_filter(img=filename, filter_name=date['user_filter'])
    await bot.delete_message(user_id, message_id=msg_id.message_id)
    await message.answer_photo(types.InputFile(result_img), caption="✅")
    await state.finish()
    os.unlink(result_img)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_bot)
