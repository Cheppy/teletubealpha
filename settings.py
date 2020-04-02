API_TOKEN = 'INSERR_API_TOKEN_HERE'

bot_commands = {
    'start': 'it`s a start',
    'help': 'Gives you information about the available commands',
    "download +<code>youtube link</code>": "Download video via youtube link",
    'yt + <code>youtube link</code> ': 'get youtube video thumbnail via link',
    "search + <code>text + page(optional)</code>": 'results via github repo search'
}
warnings = {'video_size=big': f""" Video size is too big to be downloaded via telegram\n
    Video saved at:\n"""}
