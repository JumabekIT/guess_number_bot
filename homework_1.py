'''1) Напишите телеграмм бот который загадывает случайное число с помощью
библиотеки random и вы должны угадать его.
Бот:
Я загадал число от 1 до 3 угадайте
Пользователь:
Вводит число 2, если число правильное то выводит “Правильно вы отгадали”
ДОП ЗАДАНИЕ:
2) Загрузить файлы в GitHub'''



from aiogram import Bot, Dispatcher, types, executor
import config 
import random 

bot = Bot(token = config.token)
dp = Dispatcher(bot)


number = random.randint(1, 3)

@dp.message_handler(commands = ['start', 'go'])
async def start(message: types.Message):
   await message.answer(f"Я загадал число от 1 до 3 угадайте {message.from_user.full_name}")
   await message.answer("Введите /help для получения информации о боте")

@dp.message_handler(commands = ['help'])
async def help(message: types.Message):
    await message.reply("Вот мои команды:") 
 
@dp.message_handler(lambda message: message.text.isdigit())
async def check_number(message: types.Message):
    global number
    user_guess = int(message.text)
    if user_guess == number:
        await message.answer("Правильно вы отгадали")
        number = random.randint(1, 3)
    else:
        await message.answer("Неправильно, попробуйте еще раз.")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял, введите /help")


executor.start_polling(dp)