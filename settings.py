API_TOKEN = 'INSERR_API_TOKEN_HERE'
search_results_message = """                  🐙 <em>Such repositories were found upon your request:</em> 
                                                                                                \n"""
error_message = "We couldn’t find any repositories matching"

bot_commands = {  # command description used in the "help" command
    'start': 'it`s a start',
    'help': 'Gives you information about the available commands',
    "download +<code>youtube link</code>": "Download video via youtube link",
    'yt + <code>youtube link</code> ': 'get youtube video thumbnail via link',
    "search + <code>text + page(optional)</code>": 'results via github repo search'
}