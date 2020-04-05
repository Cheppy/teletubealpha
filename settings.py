import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot_commands = {
    'start': 'it`s a start',
    'help': 'Gives you information about the available commands',
    "download +<code>youtube link</code>": "Download video via youtube link",
    'image + <code>youtube link</code> ': 'get youtube video thumbnail via link',
    "search + <code>text + page(optional)</code>": 'results via github repo search'
}
warnings = {'video_size=big': f""" Video size is too big to be downloaded via telegram\n
    Video saved at:\n"""}

audio_source_opts = [{
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(etx)s',
    'quiet': False
}, 'mp3']

video_source_opts =[{'merge_output_format': ''}, 'mp4']
