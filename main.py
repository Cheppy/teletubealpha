import os
from aiogram import Bot, Dispatcher, executor, types
import utils
import settings
import logging


bot = Bot(token=settings.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


def video_to_big_warning(video_path, key):
    abs_path = os.path.abspath(video_path)
    return f""" {settings.warnings[key]}:\n
    {abs_path}"""


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    help_text = "The following commands are available: \n"
    for key in settings.bot_commands:
        help_text += "/" + key + "     "
        help_text += settings.bot_commands[key] + "\n"
    await message.reply(help_text)


@dp.message_handler(commands=['image'])
async def get_yt_image(message: types.Message):
    txt_args = message.get_args()
    with open(utils.show_pic(txt_args), 'rb') as pic:
        await bot.send_photo(message.chat.id, pic)


@dp.message_handler(commands=['download'])
async def download_video(message: types.Message):
    txt_args = message.get_args()
    video_path = utils.get_vid(txt_args)
    print("DEBUG SIZE: " + str(utils.is_size_ok(video_path)))
    print('os.path.getsize(path= )', os.path.getsize(video_path))
    if utils.is_size_ok(video_path):
        with open(video_path, 'rb') as video_file:
            await bot.send_video(message.chat.id, video_file)
            os.remove(video_path)
    else:
        await bot.send_message(message.chat.id, video_to_big_warning(video_path, "video_size=big"))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)