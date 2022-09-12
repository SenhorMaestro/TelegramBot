import os
import logging
import time

from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig(filename = 'logfile.log', level=logging.INFO)

TOKEN = os.getenv('TOKEN')

#t = time.localtime()
#time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#admin_id = ... мой ID

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    t = time.localtime()
    text = f'Привет, {user_name}. Я телеграм-бот, преобразующий кириллицу в латиницу. Давай начнём : введи текст на кириллице.'
    logging.info(f"{user_name=} {user_id=} sent message: {message.text} at {time.asctime(t)}")
    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    t = time.localtime()
    d = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch', 'ь':'', 'ы':'y','ъ':'ie','э':'e','ю':'iu','я':'ia','А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E','Ж':'Zh','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'Kh','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Shch','Ь':'', 'Ы':'Y','Ъ':'Ie','Э':'E','Ю':'Iu','Я':'Ia'}
    logging.info(f"{user_name=} {user_id=} sent message: {message.text} at {time.asctime(t)}")
    await bot.send_message(user_id, text.translate(text.maketrans(d)))
    #await bot.send_message(admin_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)