import re

# # http://stackoverflow.com/a/13752628/6762004
# RE_EMOJI = re.compile('[\U0001F6A9]', flags=re.UNICODE)

# def strip_emoji(text):
#     return RE_EMOJI.sub(r'', text)

# print(strip_emoji('🙄ff🚩ffff🤔'))

# # 🚩
# # 0001F6A9




b = 'kfmd🚩kmfkm'

if re.search('[\U0001F6A9]', b):
    print('fuck pong')
    
else:
    print('sad')