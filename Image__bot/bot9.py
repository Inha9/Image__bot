import logging

from aiogram import Bot, Dispatcher, executor, types

from btn9 import main_menu_keyboard, drinks_menu_keyboard, dessert_menu_keyboard

API_TOKEN = '6082663790:AAEqFqwLSIl3kqEZ12d0SFMCqEuIZBoDBs4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=main_menu_keyboard)

@dp.message_handler(text=['Ichimlikar'])
async def send(message: types.Message):
    await message.reply("Ichimlikar", reply_markup=drinks_menu_keyboard)

@dp.message_handler(text=['Shirinliklar'])
async def send(message: types.Message):
    await message.reply("Shirinliklar", reply_markup=dessert_menu_keyboard)

@dp.message_handler(text=['Orqaga'])
async def send(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=main_menu_keyboard)



@dp.message_handler(text='CocaCola')
async def send(message: types.Message):
    await message.answer_photo("https://m.media-amazon.com/images/I/81AyNAm-QiL.jpg", caption="0.5 - 5500 \n 1l - 9000 \n 1.5 - 12000")

@dp.message_handler(text='Pepsi')
async def send(message: types.Message):
    await message.answer_photo("https://www.retail.ru/upload/medialibrary/f1a/shutterstock_1481415659.jpg", caption="0.5 - 7000 \n 1l - 11000 \n 1.5 - 15000")



@dp.message_handler(text='Fanta')
async def send(message: types.Message):
    await message.answer_photo("https://ru.coca-cola.uz/content/dam/one/uz/ru/section-header-mobile/fanta-header_mobile_image.jpg", caption="0.5 - 5000 \n 1l - 10000 \n 1.5 - 15000")

@dp.message_handler(text='Sprite')
async def send(message: types.Message):
    await message.answer_photo("https://www.cocacolaep.com/assets/Uploads/resources/Sprite-and-Sprite-Zero-packshots_1200x735px__FillWzEyMDAsNjMwXQ.jpg", caption="0.5 - 4000 \n 1l - 8000 \n 1.5 - 11000")



@dp.message_handler(text='Cake')
async def send(message: types.Message):
    await message.answer_photo("https://hips.hearstapps.com/hmg-prod/images/wdy050121lifeoftheparty-003-1621611282.jpg?crop=0.998xw:0.337xh;0,0.276xh&resize=1200:*", caption="kattasi - 5000 \n Kichigi - 20000 \n O'rtachasi - 25000")

@dp.message_handler(text='Pencake')
async def send(message: types.Message):
    await message.answer_photo("https://live.staticflickr.com/3751/9869659585_4c03689cfd_b.jpg", caption="Kattasi - 15000 \n Kichigi - 7000 \n O'rtachasi - 10000")



@dp.message_handler(text='sweets')
async def send(message: types.Message):
    await message.answer_photo("https://media.istockphoto.com/id/1054228718/photo/indian-sweets-in-a-plate-includes-gulab-jamun-rasgulla-kaju-katli-morichoor-bundi-laddu.jpg?s=612x612&w=0&k=20&c=hYWCXLaldKvhxdBa83M0RnUij7BCmhf-ywWdvyIXR40=", caption="1 pachka - 15000 \n 1kilosi - 10000 \n donasi - 500")

@dp.message_handler(text='donuts')
async def send(message: types.Message):
    await message.answer_photo("https://cdn.britannica.com/38/230838-050-D0173E79/doughnuts-donuts.jpg", caption="1 tasi - 5000")



@dp.message_handler(text='Lavashlar')
async def send(message: types.Message):
    await message.answer_photo("https://yukber.uz/image/cache/catalog/lavash-700x700.jpg", caption="kattasi - 30000 \n Kichigi - 10000 \n O'rtachasi - 20000")

@dp.message_handler(text='Pitsalar')
async def send(message: types.Message):
    await message.answer_photo("https://hips.hearstapps.com/hmg-prod/images/classic-cheese-pizza-recipe-2-64429a0cb408b.jpg?crop=0.6666666666666667xw:1xh;center,top&resize=1200:*", caption="Kattasi - 50000 \n Kichigi - 20000 \n O'rtachasi - 25000")



@dp.message_handler(text='Burgerlar')
async def send(message: types.Message):
    await message.answer_photo("https://www.thecookierookie.com/wp-content/uploads/2023/04/featured-stovetop-burgers-recipe.jpg", caption="Kattasi - 20000 \n Kichigi - 5000 \n O'rtachasi - 10000")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)