from aiogram import Bot, Dispatcher, types, executor
import config 

bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start', 'go'])
async def start(message: types.Message):
   await message.answer(f"Здраствуйте {message.from_user.full_name}")
   await message.answer("Введите /help для получения информации о боте")
   await message.answer_location(40.71267135502846, -74.00593316109249)
   await message.answer_photo("https://bigpicture.ru/wp-content/uploads/2015/11/nophotoshop29-800x532.jpg")
   await message.answer_contact("+996707646202", first_name = "Zhumabek")
   await message.answer_audio("https://cdn.pixabay.com/download/audio/2022/11/24/audio_002bd052b6.mp3?filename=passion-127011.mp3")




@dp.message_handler(commands = ['help'])
async def help(message: types.Message):
    await message.reply("Вот мои команды:") 
 
@dp.message_handler(text = ['Привет', 'привет'])
async def hello(message: types.Message):
    await message.answer("Привет, как дела?")


''
@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)

