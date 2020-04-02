import os
from aiogram import Bot, Dispatcher, executor, types
import  manager
import settings
bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)


def video_to_big_warning(video_path):
    abs_path = os.path.abspath(video_path)
    return f"""
    Video size is too big to be downloaded via telegram.
    Video saved at:\n
    {abs_path}"""


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    help_text = "The following commands are available: \n"
    for key in misc.bot_commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + "     "
        help_text += misc.bot_commands[key] + "\n"
    await message.reply(help_text, parse_mode='HTML')


@dp.message_handler(commands=['yt'])
async def get_yt_image(message: types.Message):
    txt_args = message.get_args()
    with open(manager.show_pic(txt_args), 'rb') as pic:
        await bot.send_photo(message.chat.id, pic)


@dp.message_handler(commands=['download'])
async def download_video(message: types.Message):
    txt_args = message.get_args()
    video_path = manager.get_vid(txt_args)
    print("DEBUG SIZE: " + str(manager.is_size_ok(video_path)))
    if manager.is_size_ok(video_path):
        with open(video_path, 'rb') as video_file:
            await bot.send_video(message.chat.id, video_file)
            os.remove(video_path)
    else:
        await bot.send_message(message.chat.id, video_to_big_warning(video_path))


@dp.message_handler(commands=['search'])
async def github_search(message: types.Message):
    search_args = message.get_args().split()
    print(search_args)

    message_txt = github_search(*search_args)
    if message_txt == "":
        message_txt = f"{settings.error_message} {search_args}'"
    await bot.send_message(message.chat.id, settings.search_results_message + str(message_txt),
                           parse_mode="HTML",
                           disable_web_page_preview=True)


if __name__ == 'main':
    executor.start_polling(dp, skip_updates=True)