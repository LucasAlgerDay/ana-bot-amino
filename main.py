import os


from BotAmino import BotAmino
from BotAmino import *
import os
import requests
from datetime import datetime
import pytz
from pathlib import Path
from gtts import gTTS, lang
from fancy_text import fancy
from google_trans_new import google_translator
#from constant import LANGUAGES, DEFAULT_SERVICE_URLS
from json import dumps, load
from threading import Thread
from random import choice, randint
from pathlib import Path
from contextlib import suppress
from string import punctuation
from unicodedata import normalize
#wnload import google_images_download
import time
import urllib
import json
from datetime import datetime
#from pdf2image import convert_from_path
from youtube_dl import YoutubeDL
from BotAmino import *
import random
import math
from PIL import Image, ImageFont, ImageDraw
import string
import pytz
import re
import shutil
import argparse
from PIL import Image, ImageDraw, ImageFont
from easy_pil import Editor, Canvas, load_image, Font
import io
import requests
from os import path
import urllib.request
import datetime
import json 
from time import sleep
from functools import wraps
from io import BytesIO
import base64
from zipfile import ZipFile
import threading
import sys
from urllib import response

id = ["71a18c01-da11-4fd9-9d11-4491d8ebd64d"]

f = open("youtube.txt", "r+")
ytlink=(f.read())
with suppress(Exception):
    for i in (path_utilities, path_amino):
        Path(i).mkdir(exist_ok=True)

my_proxies = {
    "http": "http://mmamlolxd:MXJxcVpEdT@93.188.207.53:50100 "
}

client = BotAmino(proxies=my_proxies)
print(client.proxies)
fs = open("sids.txt", "r+")
sidd=(fs.read())

client = BotAmino(sid=sidd)
#client = BotAmino(email="Anitabotsito@gmail.com", password="URAPRO123")
client.prefix = "!"
#yokita3788@gamezalo.com

@client.command('bg')
def bg(data):
    image = data.subClient.get_chat_thread(data.chatId).backgroundImage
    if image is not None:
      filename = image.split("/")[-1]
      urllib.request.urlretrieve(image, filename)
      with open(filename, 'rb') as fp:
        data.subClient.send_message(chatId=data.chatId, file=fp, fileType="image")


@client.command(name="joinc")
def joinc(data):
    if client.check(data,'staff'):
        url = data.message
        code = client.get_from_code(url)
        community_id = code.path[1:code.path.index('/')]
        if 'extensions' in code.json and 'invitationId' in code.json['extensions']:
            invitation_id = code.json['extensions']['invitationId']
            client.join_community(community_id, invitation_id)
            data.subClient.send_message(data.chatId,"unido", replyTo=data.messageId)
        else:
            client.join_community(community_id)
        Thread(target=client.threadLaunch, args=[community_id, True]).start()
        data.subClient.send_messag

@client.command(name="uc")
def juc(data):
        url = data.message
        code = client.get_from_code(url)
        community_id = code.path[1:code.path.index('/')]
        if 'extensions' in code.json and 'invitationId' in code.json['extensions']:
            invitation_id = code.json['extensions']['invitationId']
            client.join_community(community_id, invitation_id)
            data.subClient.send_message(data.chatId,"unido", replyTo=data.messageId)
        else:
            client.join_community(community_id)
        Thread(target=client.threadLaunch, args=[community_id, True]).start()
        data.subClient.send_messag


@client.on_member_join_chat()
def say_hello(data):
    l = data.subClient.get_user_info(data.authorId).icon
    level = data.subClient.get_member_level(data.authorId)
    req = requests.get(l).content
    with open('giga.jpeg', 'wb') as file:
        file.write(req)
    with open('giga.jpeg', 'rb') as file:
        data.subClient.send_message(data.chatId, f"""
[c]𝗪𝗘𝗟𝗖𝗢𝗠𝗘 <$@{data.author}$>,
[C]
[C]
[C]╭╭╌💮 〕﹟𝗕𝗢𝗧 𝗗𝗘 𝗝𝗢𝗡  ↓↓︕ ╌╮╮
[C]╰╰▻ ❪﹟𝐔𝐧 𝐛𝐮𝐞𝐧 𝐚𝐦𝐢𝐠𝐨  ❫ 💮﹞ ︵ . ╯
[C]☆  /  /  ★  ᨓ  ¡¡  +  ♡̶  𓂃 ###  !! `
[C]︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿
[C]                𝐖3𝗟𝗖𝐎𝕸𝗘      𝖴𝖲𝖴𝖠𝖱𝖨𝖮
[C]!! ⸺ 𝗟𝗲𝗮 𝗹𝗮𝘀 𝗿𝗲𝗴𝗹𝗮𝘀 para evitar lle
[C]          varse el ban. Esperemos que
[C]          su                                             !!
[C]          𝗲𝘀𝘁𝗮𝗻𝗰𝗶𝗮 en éste chat sea de
[C]          𝗼𝗿𝗼.                            ¡Disfrute!
[C]︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿""",mentionUserIds=data.authorId ,embedImage=file, embedTitle=f'{data.author}', embedContent=f'Level: {level}, una nueva personita')

file = "old_messages.json"
filed = "deleted_messages.json"

try:
    with open(file, "r") as f:
        old_messages = json.load(f)
except Exception:
    old_messages = {}

try:
    with open(filed, "r") as f:
        deleted_messages = json.load(f)
except Exception:
    deleted_messages = {}

def print_exception(exc):
    print(repr(exc))
    
def join_community(comId: str = None, inv: str = None):
    if inv:
        try:
            client.client.join_community(comId=comId, invitationId=inv)
            return True
        except Exception as e:
            print_exception(e)





@client.command()
def unetec(data):
    data.subClient.join_all_chat()
    data.subClient.send_message(data.chatId, "Unido a todos los chats")

@client.on_all()
def anti_raid(data):
    datatype=[114,109,108,100, 107,115,116,110,111,112,113,114,117,124,125,126,128]
    types = data.info.message.type
    if types in datatype and data.message != None and data.authorId != client.userId:
        if data.subClient.is_in_staff(client.userId):
            data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
            try:
                data.subClient.strike(userId=data.authorId, time= 1, title= "Rider", reason= f"raider type {types}")
                data.subClient.ban(userId=str(data.authorId), reason=f"{data.author}: raid type: {types}")
            except:
                pass
        else:
            data.subClient.flag(reason=f"Raider type {types}", flagType=1, userId= data.authorId)




listita=["COMES", "Comes", "Tragas", "Desayunas", "Que rico", "No, mejor los pussys"]
listaS=["No tendras por pajero", "Sexo con tu mama", "Solo eso saben decir, csmr", "No, causa, no", "Ya comienzan estos virgos", "No, el sexo es sobrevalorado", "Sexo compro, sexo vendo", "¡Sexooooooooooo!"]

@client.on_all()
def pene_comes(data):
    mens=["pene", "polla", "pito", "pilin"]
    mensaje=["sexo", "Sexo", "SEXO", "segs", "sexito", "segsss"]
    type = data.message
    if type in mens and data.message != None and data.authorId != client.userId:
        data.subClient.send_message(data.chatId,message=f"""[Ic]⸻ ❝{random.choice(listita)}, {data.author}❞ ৴""", replyTo=data.messageId)
    if type in mensaje and data.message != None and data.authorId != client.userId:       
        data.subClient.send_message(data.chatId,message=f"""[Ic]⸻ ❝{random.choice(listaS)}, {data.author}❞ ৴""", replyTo=data.messageId)
    


@client.command("afk")
def countdown(data):
    global afkdict
    z=int(data.message)
    x=data.subClient.get_user_info(data.authorId).icon
    response=requests.get(f"{x}")
    file=open(".saue.png","wb")
    file.write(response.content)
    file.close()
    img = open(".saue.png","rb")
    afkdict[data.authorId] = data.message
    data.subClient.send_message(data.chatId,message=f"""
︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿
[Ic]⸻ ❝ahora estas AFK, {data.author}, por {z} segundos❞ ৴
︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ """,mentionUserIds=[data.authorId], replyTo=data.messageId)
    t=0
    while t !=z:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1
    print("timer done")
    data.subClient.send_message(data.chatId,message=f"""
︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿
[Ic]⸻ ❝Bienvenido, {data.author}, te fuiste por {z} segundos❞ ৴
[Ic] ya no estas AFK
︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿""",embedImage=img,embedTitle=f"{data.author}",embedLink="ndc://x{data.comId}/user-profile/{data.authorId}",mentionUserIds=[data.authorId], replyTo=data.messageId)
t = int(1)

def getImageDirectory(keywords):
	absolute_image_paths = response.download({"silent_mode" : True, "keywords" : keywords, "limit" : 1, "print_urls" : False, "safe_search" : True, "socket_timeout" : 0.1, "delay" : 0.1, "format" : "png"})
	return absolute_image_paths

@client.command("getdelete")
def getdelete(data):
    if client.check(data,'staff'):
        messages = data.subClient.get_chat_messages(data.chatId, 100).messageId
        for m in messages:
            try:
               data.subClient.send_message(data.chatId, deleted_messages[data.chatId][m])
            except:
               pass
        
@client.command("json")
def create_community(data):
        if client.check(data,'staff'):
            with open(f'{path_amino}/{data.message}.json', 'w', encoding='utf8') as file:
                dict = {"welcome": "", "prefix": "!", "welcome_chat": "", "locked_command": [], "favorite_users": [], "favorite_chats": [], "banned_words": []}
                file.write(dumps(dict, sort_keys=False, indent=4))
                data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Json creado, {data.author}❞ ৴", replyTo=data.messageId)



@client.command("invitevc")
def inviteavc(data):
    if client.check(data,'staff'):
        h=data.subClient.get_online_users(start=0,size=100).profile.userId
        j=data.subClient.get_online_users(start=0,size=100).profile.nickname
        u=len(j)
        for ud in h:
            data.subClient.invite_to_vc(userId=ud,chatId=data.chatId)
        for i in range(1):
            data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻ ❝Invitado a {u} usuarios , {data.author}❞ ৴", replyTo=data.messageId)

@client.command("inviteall")
def inviteall(data):
    if client.check(data,'staff'):
        h=data.subClient.get_online_users(start=0,size=100).profile.userId
        j=data.subClient.get_online_users(start=0,size=100).profile.nickname
        u=len(j)
        for ud in h:
            data.subClient.invite_to_chat(userId=ud,chatId=data.chatId)
        for i in range(1):
            data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻ ❝Invitado a {u} usuarios , {data.author}❞ ৴", replyTo=data.messageId)




@client.command("all")
def mentionall(args):
    if client.check(args, 'staff', 'itsme', 'admin'):
        if args.message and client.check(args, 'itsme'):
            chat_ide = args.subClient.get_chat_id(args.message)
            if chat_ide:
                args.chatId = chat_ide
            args.message = " ".join(args.message.strip().split()[:-1])

        mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId).userId]
        test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId).userId])

        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"@everyone{test}", mentionUserIds=mention)



@client.command("ytr")
def ytr(data):
    if client.check(data,'staff'):
        fi= open("youtube.txt", "r+")
        fi.seek(0)
        fi.truncate()
        data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Link removido , {data.author}❞ ৴", replyTo=data.messageId)

@client.command("linkr")
def linkr(data):
    if client.check(data,'staff'):
        if os.path.exists("youtube.txt"):
            os.remove("youtube.txt")
            data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Link removido , {data.author}❞ ৴", replyTo=data.messageId)
        else:
            data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Link removido , {data.author}❞ ৴", replyTo=data.messageId)
            
@client.command("linknew")
def linknew(data):
    if client.check(data,'staff'):
        k=data.message
        lin=open("youtube.txt", "w")
        lin.write(f"{k}")
        lin.close()
        data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Link cargado {k}, {data.author}❞ ৴", replyTo=data.messageId)

@client.command("ytv")
def ytv(data):
    if client.check(data,'staff'):
        filess = open('youtube.txt', 'w')
        filess.write(f'{data.message}')
        filess.close()
        data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Link abierto, {data.author}❞ ৴", replyTo=data.messageId)   




@client.command("name")
def name(data):
    if client.check(data,'staff'):
        data.subClient.edit_profile(nickname=data.message)
        data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻ ❝Nombre cambiado, {data.author}❞ ৴", replyTo=data.messageId)


@client.command("nombre")
def nombre(data):
        data.subClient.edit_profile(nickname=data.message)
        data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻ ❝Nombre cambiado, {data.author}❞ ৴", replyTo=data.messageId)
         
#@client.on_member_leave_chat()
#def goodbye(data):
    #with open("salir.gif","rb") as fp:
        #data.subClient.send_message(data.chatId,file=fp, fileType="gif")
        
@client.command("peaches")
def peach(data):
    with open("peaches.mp3","rb") as fp:
        data.subClient.send_message(data.chatId,file=fp, fileType="audio")

@client.command("muerto")
def muerto(data):
			img9=open("pro.png","rb")
			img=open(".ripe.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				n=data.subClient.get_user_info(str(user)).nickname
				response=requests.get(f"{h}")
				file=open(".ai8yijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".ripe.png").resize((642,806))
				img1 = Image.open(".ai8yijhale.png").resize((300,300))
				img.paste(img1, (175,385))
				#img.paste(img1, (750,1250))
				img=img.save(".yivhh3.png")
				imgg=open(".yivhh3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId, file=imgg,fileType="image",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent="Te ha papeado, " + str(n))
				except:
					pass

@client.command("cum")
def cum(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("cumear.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Te esta cumeando, " + str(n))


@client.command("cumear")
def cumear(data):
			img=open("cumear.gif","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				n=data.subClient.get_user_info(str(user)).nickname
				response=requests.get(f"{h}")
				file=open(".ai8yijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open("cumear.gif").resize((642,806))
				img1 = Image.open(".ai8yijhale.png").resize((300,300))
				img.paste(img1, (175,385))
				#img.paste(img1, (750,1250))
				img=img.save("cum.gif")
				imgg=open("cum.gif","rb")
				try:
					data.subClient.send_message(chatId=data.chatId, message=f"Haz sido arrestado" + str(n), file=imgg,fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Te esta cumeando, " + str(n))
				except:
					pass


@client.command("botlog")
def botlog(data):
    if client.check(data,'staff'):
        data.subClient.add_favorite_chats(data.chatId)
        data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Botlog creado, {data.author}❞ ৴", replyTo=data.messageId)

@client.command("ubotlog")
def ubotlog(data):
	data.subClient.remove_favorite_chats(data.chatId)
	data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝Botlog cerrado, {data.author}❞ ৴", replyTo=data.messageId)
            
@client.command("checkin")
def checkin(data):
	client.check_all()
	data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝  Ana hizo checkin, {data.author}❞ ৴", replyTo=data.messageId)

@client.command("comid")
def comid(data):
	n=data.message
	fok=client.get_from_code(n)
	id=client.get_from_code(n).objectId
	cid=fok.path[1:fok.path.index("/")]
	data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻ ❝ cid de la comunidad = {cid}")

@client.command("tr")
def tr(args):
  data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  reply_message = data.json['extensions']
  if reply_message:
    reply_message = data.json['extensions']['replyMessage']['content']
    reply_messageId = data.json['extensions']['replyMessage']['messageId']
    translator = google_translator() 
    detect_result = translator.detect(reply_message)[1]
    translate_text = translator.translate(reply_message)
    reply = "[IC]"+str(translate_text)+"\n\n[c]Texto traducido por "+str(detect_result)
    print(reply)
    args.subClient.send_message(chatId=data.chatId,message=reply,replyTo=reply_messageId)	

@client.command("titulo")
def titulo(args):
    if client.check(args, 'staff', id_=client.botId):
        try:
            title, color = args.message.split("color=")
            color = color if color.startswith("#") else f'#{color}'
        except Exception:
            title = args.message
            color = None

        if args.subClient.add_title(args.authorId, title, color):
            args.subClient.send_message(args.chatId, f"[Ic]⸻ ❝Titulo otorgado, {args.author}❞ ৴", replyTo=args.messageId)

@client.command("music")
def music(args):
    img=open("pro.png","rb")
    ias=open(".tvs.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    args.subClient.send_message(args.chatId, f"""[C]Music Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ play (youtube link)

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",embedTitle="❝ 🧸̱﹕𝗝꯭𝗢꯭𝗡 ⸴⸴",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedImage=im,embedContent=" C R E A D O R  D E  A N A")

@client.event("on_chat_tip")
def on_chat_tip(data):
	try:
		commuId = data.json["ndcId"]
		subClient = client.get_community(commuId)
	except Exception:
		return
	args = Parameters(data, subClient)	
	raw_data = data.json
	nick_name = raw_data['chatMessage']['author']['nickname']
	coins = raw_data['chatMessage']['extensions']['tippingCoins']
	chatId = raw_data['chatMessage']['threadId']
	reply = "[Ic]⸻ ❝Gracias por las " + str(coins) + " Coins \n\n[C]" + str(nick_name)
	#print(raw_data)
	#print("chatId", chatId)
	subClient.send_message(chatId=args.chatId, message=reply)

@client.command("coinon")
def coinon(data):
            data.subClient.edit_chat(chatId=data.chatId, canTip=True)
            tz = pytz.timezone('Asia/Kolkata')  
            now = datetime.now(tz)  
            current_time=now.strftime("%H:%M:%S") 
            chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
            val=data.subClient.get_chat_thread(data.chatId).title 
            chats=data.subClient.favorite_chats
            for id, in zip(chats) : 
                data.subClient.send_message(chatId=id,message=f"""[c]{data.author} enabled CoinTip in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat:
{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")

@client.command("coinoff")
def coinoff(data):
        data.subClient.edit_chat(chatId=data.chatId, canTip=False)
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time=now.strftime("%H:%M:%S")
        chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
        val=data.subClient.get_chat_thread(data.chatId).title
        chats=data.subClient.favorite_chats
        for id, in zip(chats) :
            data.subClient.send_message(chatId=id,message=f"""[c]{data.author} disabled CoinTip in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat:
{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")

@client.command("viewde")
def vieode(data):
            data.subClient.edit_chat(chatId=data.chatId, viewOnly=True)
            time.sleep(60)
            data.subClient.edit_chat(chatId=data.chatId,viewOnly=False)
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time=now.strftime("%H:%M:%S")
            chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
            val=data.subClient.get_chat_thread(data.chatId).title
            chats=data.subClient.favorite_chats
            for id, in zip(chats) :
                		 	data.subClient.send_message(chatId=id,message=f"""[c]{data.author} puso en visualizacion {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat:
{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")

@client.command("prank")
def prank(data):
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
	data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="Clear")
	data.subClient.transfer_host(data.chatId,userIds=[client.userId])
	info=data.subClient.get_chat_thread(data.chatId)
	x=info.json['extensions']['organizerTransferRequest']['requestId']
	data.subClient.accept_organizer(chatId=data.chatId,requestId=x)
	#time.sleep(1)
	h=data.subClient.get_chat_thread(data.chatId).title
	data.subClient.kick(data.authorId,data.chatId,allowRejoin=True)
	data.subClient.start_chat(data.authorId,message=f"""
[c]Prank

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[c]{data.author}
[c]I kicked you from {h}

[c]You can join again your GC {h}
[c]Your Chatroom is safe

[c]How was my prank :)

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}			
""")
	chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
	chats=data.subClient.favorite_chats
	for id, in zip(chats) :
		data.subClient.send_message(chatId=id,message=f"""[c]Prank command by {data.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

  Chat : {chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {h}")

@client.command("anfi")
def anfi(data):
	#j=[client.userId]
	data.subClient.transfer_host(data.chatId,userIds=[client.userId])
	info=data.subClient.get_chat_thread(data.chatId)
	x=info.json['extensions']['organizerTransferRequest']['requestId']
	data.subClient.accept_organizer(chatId=data.chatId,requestId=x)
	data.subClient.send_message(data.chatId,message="Host changed")


@client.command("ghost")
def ghost(data):
        data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="Clear")
        data.subClient.send_message(data.chatId,data.message,messageType=109)
        #now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time=now.strftime("%H:%M:%S")
        #current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
        val=data.subClient.get_chat_thread(data.chatId).title
        chats=data.subClient.favorite_chats
        for id, in zip(chats) :
        	data.subClient.send_message(chatId=id,message=f"""[c]Ghost command by {data.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

    {data.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")

@client.command("arrestado")
def arrestado(data):
			img=open(".wanted.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".wanted.png")
				img1 = Image.open(".aale.png").resize((447,447))
				img.paste(img1, (145,250))
				img=img.save(".i3.png")
				imgg=open(".i3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass
                                
@client.command("wtf")
def wtf(data):
			img=open(".wf.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".wf.png")
				img1 = Image.open(".aijhale.png").resize((200,200))
				img.paste(img1, (750,350))
				img.paste(img1, (750,1250))
				img=img.save(".ihh3.png")
				imgg=open(".ihh3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass

@client.command("rip")
def rip(data):
			img=open(".ripe.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".ai8yijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".ripe.png").resize((642,806))
				img1 = Image.open(".ai8yijhale.png").resize((300,300))
				img.paste(img1, (175,385))
				#img.paste(img1, (750,1250))
				img=img.save(".yivhh3.png")
				imgg=open(".yivhh3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass
                            
                        
@client.command("kill")
def kill(data):
			img=open(".sword.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aiyijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".sword.png")
				img1 = Image.open(".aiyijhale.png").resize((175,175))
				img.paste(img1, (295,670))
				#img.paste(img1, (750,1250))
				img=img.save(".yihh3.png")
				imgg=open(".yihh3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass
                                
@client.command("castigo")
def castigo(data):
			img=open(".sank.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aiy88ijhale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".a8n8ie.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".sank.png")
				img1 = Image.open(".aiy88ijhale.png").resize((140,140))
				img2 =Image.open(".a8n8ie.png").resize((160,160))
				img.paste(img1, (700,505))
				img.paste(img2, (460,100))
				img=img.save(".ybi9hh3.png")
				imgg=open(".ybi9hh3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass
					
@client.command("door")
def door(data):
			img=open(".door.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a0jhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".door.png")
				img1 = Image.open(".a0jhale.png").resize((240,220))
				img.paste(img1, (405,20))
				#img.paste(img1, (750,1250))
				img=img.save(".yinhh3.png")
				imgg=open(".yinhh3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass				
@client.command("gay")
def gay(data):
			img=open(".gay.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a7ale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".gay.png").resize((800,800))
				img1 = Image.open(".a7ale.png").resize((800,800))
				#img.size
				#img1.size 
				#img_size = img.resize((800, 400))
				#img1_size = img1.resize((447, 447))
				img.putalpha(128)
				img1.paste(img, (0,0),img)
				img1=img1.save(".img73.png")
				imgg=open(".img73.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass

@client.command("disable")
def disable(data):
			img=open(".disability.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aa9le.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".disability.png")
				img1 = Image.open(".aa9le.png").resize((175,175))
				img.paste(img1, (450,325))
				img=img.save(".i7mg3.png")
				imgg=open(".i7mg3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass

@client.command("brazz")
def brazz(data):
			img=open(".braz.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aai9le.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".braz.png")
				img1 = Image.open(".aai9le.png")
				aspect = img1.width / img1.height
				new_height = int(img.height * aspect)
				new_width = int(img.width * aspect)
				scale = new_width / img1.width
				size = (int(new_width / scale / 2), int(new_height / scale / 2))
				img = img.resize(size).convert('RGBA')
				img1.paste(img, (img1.width - img.width,img1.height - img.height), img)
				#img.paste(img1, (450,325))
				img1=img1.save(".img3.png")
				imgg=open(".img3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass

@client.command("medal")
def medal(data):
			img=open(".medal.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aa999le.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".medal.png")
				img1 = Image.open(".aa999le.png").resize((200,200)) 
				#img.size
				#img1.size 
				#img_size = img.resize((800, 400))
				#img1_size = img1.resize((75,75))
				img.paste(img1, (120,73))
				img.paste(img1, (365,0))
				img=img.save(".im88ig3.png")
				imgg=open(".im88ig3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass


@client.command("shit")
def shit(data):
			img=open(".shit.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aokale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".shit.png")
				img1 = Image.open(".aokale.png").resize((135,135))
				img.paste(img1, (220,750))
				img=img.save(".im88g3.png")
				imgg=open(".im88g3.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass
                                
@client.command("ship")
def ship(data):
			img9=open("pro.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".axale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".ame.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".ame.png") 
				img1 = Image.open(".axale.png") 
				img.size
				img1.size 
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				msg = data.message + " null null "
				msg = msg.split(" ")
				msg[2] = msg[1]
				msg[1] = msg[0]
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image",embedTitle=f"ℓσѵε ɱαƭcɦ ❴ {random.randint(0,100)}% ❵",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent="𝑀𝑎𝑑𝑒 𝑏𝑦 ⁶❝ 🧸̱﹕𝗝꯭𝗢꯭𝗡 ⸴⸴⁹",embedImage=img9)
				except:
					pass
                                
@client.command("love")
def love(data):
			img9=open("pro.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".axuale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aikme.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aikme.png") 
				img1 = Image.open(".axuale.png") 
				img.size
				img1.size 
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				msg = data.message + " null null "
				msg = msg.split(" ")
				msg[2] = msg[1]
				msg[1] = msg[0]
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image",embedTitle=f"Love match❤️ {random.randint(0,100)}% ❵",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent="𝑀𝑎𝑑𝑒 𝑏𝑦 ❝ 🧸̱﹕𝗝꯭𝗢꯭𝗡 ⸴⸴』⁹",embedImage=img9)
				except:
					pass

@client.command("hate")
def hate(data):
			img9=open("pro.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a11ale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aike.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aike.png") 
				img1 = Image.open(".a11ale.png") 
				img.size
				img1.size 
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				msg = data.message + " null null "
				msg = msg.split(" ")
				msg[2] = msg[1]
				msg[1] = msg[0]
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image",embedTitle=f"Hate💔 ❴ {random.randint(0,100)}% ❵",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent="𝑀𝑎𝑑𝑒 𝑏𝑦 ❝ 🧸̱﹕𝗝꯭𝗢꯭𝗡 ⸴⸴",embedImage=img9)
				except:
					pass
                                


@client.command("bofetada")
def bofetada(data):
			img=open(".slap.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".haas.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aie.png","wb")
				file.write(response.content)
				file.close()
				#img2 = Image.open(".aie.png")
				img = Image.open(".slap.png") 
				img1 = Image.open(".haas.png").resize((250,250)) 
				img2= Image.open(".aie.png").resize((240,240))
				img.paste(img1, (740,300))
				img.paste(img2, (450,90))
				img=img.save(".ijs.png")
				imgg=open(".ijs.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass

@client.command("kiss")
def kiss(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("kiss.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Comenzó a besar a, " + str(n))

@client.command("golpe")
def golpe(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("golpe.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Golpea a " + str(n))

@client.command("mimos")
def mimos(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("mimos.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Comenzó a mimar a, " + str(n))

@client.command("zape")
def zape(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("zape.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Llena de zapes a, " + str(n))

@client.command("abrazo")
def abrazo(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("abrazo.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Le da un calido abrazo a " + str(n))

@client.command("nalgada")
def nalgada(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("nalgada.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif",embedTitle=f"{data.author}",embedLink="http://aminoapps.com/u/OtracuentadeJon98",embedContent= "Te va a romper las nalgas, " + str(n))

@client.command("help")
def help(data):
      img= open("pro.png", "rb")
      ias = ("help.jpg")
      im = open(".pr.png", "rb")
      yimg = open("youimage.png", "rb")
      Image.open(ias).resize((863, 400)).save("nsus.png")
      ff = open("nsus.png", "rb")
      msg = f"""[c]⌈                          ⌉
[c]
[uc]⁽ ↳ ♡'  𝗁ᥱ̅𝗒 𝗎. 𝗌𝖾𝗋 ⸺ 𝘄𝗲𝗹.𝖼᥆̅𝗆𝖾 ⭏ ¡ 💭̷ ! 
[c]﹫𝖨𝗋ᥱ̅𝗇𝖾'𝗌 𝖼. ᥆̅𝗆𝗆͟𝖺͟𝗇𝖽𝗌 ꜝ ﹝𔘓﹞⸺ 𝗎. 𝗌ᥱ̅ 𝗂𝗍 ˿
[c]
[c]⏝ .⏝ . ⏝ . ⏝ . ⏝. ⏝ . ⏝ . ⏝
[c]
[c]¡Hola usuario! Soy Ana, un  bot creado
[c]por﹫𝗝𝗼𝗻. A  continuación dejo mi lista
[c]de comandos, recuerda que el prefijo
[c]de uso es " ! "
[c]───────────────────
           !acciones 
                                  !staff  
           !herramientas  
                                  !helpers
           !reportes        
                                  !admins 
           !juegos  
                                  !chat   
[c]───────────────────
[c]
[cu]⁽  ↳ 𝖽᥆̅𝗇'𝗍 𝗮𝗯𝘂.𝗌ᥱ̅! ⸺ 𝖻𝗒𝖾 𝖻𝗒𝖾 𝗌. 𝗐𝖾𝖾𝗍𝗂𝖾﹕
[c]
[c]⌊                          ⌋"""
      data.subClient.full_embed("http://aminoapps.com/u/Jon87153782", ff, msg, data.chatId)

@client.command("staff")
def staff(data):
      img= open("pro.png", "rb")
      ias = ("help.jpg")
      im = open(".pr.png", "rb")
      yimg = open("youimage.png", "rb")
      Image.open(ias).resize((863, 400)).save("nsus.png")
      ff = open("nsus.png", "rb")
      msg = f"""[c]⌈                          ⌉
[c]
[uc]⁽ ↳ ♡'  𝗁ᥱ̅𝗒 𝗎. 𝗌𝖾𝗋 ⸺ 𝘄𝗲𝗹.𝖼᥆̅𝗆𝖾 ⭏ ¡ 💭̷ ! 
[c]﹫𝖨𝗋ᥱ̅𝗇𝖾'𝗌 𝖼. ᥆̅𝗆𝗆͟𝖺͟𝗇𝖽𝗌 ꜝ ﹝𔘓﹞⸺ 𝗎. 𝗌ᥱ̅ 𝗂𝗍 ˿
[c]
[c]⏝ .⏝ . ⏝ . ⏝ . ⏝. ⏝ . ⏝ . ⏝
[c]
[c]¡Hola usuario! Soy Ana, un  bot creado
[c]por﹫𝗝𝗼𝗻. A  continuación dejo mi lista
[c]de comandos, recuerda que el prefijo
[c]de uso es " ! "
[c]───────────────────
           !bane-- (Baneo de usuaruos)     
           !globl-- (Ver el global)
           !titulo-- (Colocar titulos)
           !joinall-- (Unir a todos los chats)
           !all-- (@ a todos) 
           !joinc-- (Unir a una comunidad)
           !limpieza-- (Limpieza en un chat)
           !unete-- (Unir a un chat especifico)
[c]───────────────────
[c]
[cu]⁽  ↳ 𝖽᥆̅𝗇'𝗍 𝗮𝗯𝘂.𝗌ᥱ̅! ⸺ 𝖻𝗒𝖾 𝖻𝗒𝖾 𝗌. 𝗐𝖾𝖾𝗍𝗂𝖾﹕
[c]
[c]⌊                          ⌋"""
      data.subClient.full_embed("http://aminoapps.com/u/Jon87153782", ff, msg, data.chatId)


@client.command("herramientas")
def herramientas(data):
      img= open("pro.png", "rb")
      ias = ("help.jpg")
      im = open(".pr.png", "rb")
      yimg = open("youimage.png", "rb")
      Image.open(ias).resize((863, 400)).save("nsus.png")
      ff = open("nsus.png", "rb")
      msg = f"""[c]⌈                          ⌉
[c]
[uc]⁽ ↳ ♡'  𝗁ᥱ̅𝗒 𝗎. 𝗌𝖾𝗋 ⸺ 𝘄𝗲𝗹.𝖼᥆̅𝗆𝖾 ⭏ ¡ 💭̷ ! 
[c]﹫𝖨𝗋ᥱ̅𝗇𝖾'𝗌 𝖼. ᥆̅𝗆𝗆͟𝖺͟𝗇𝖽𝗌 ꜝ ﹝𔘓﹞⸺ 𝗎. 𝗌ᥱ̅ 𝗂𝗍 ˿
[c]
[c]⏝ .⏝ . ⏝ . ⏝ . ⏝. ⏝ . ⏝ . ⏝
[c]
[c]¡Hola usuario! Soy Ana, un  bot creado
[c]por﹫𝗝𝗼𝗻. A  continuación dejo mi lista
[c]de comandos, recuerda que el prefijo
[c]de uso es " ! "
[c]───────────────────
           !s-- (Seguirte)     
           !Comentale-- (Comentar en su muro)
           !info-- (Colocar titulos)
           !bg-- (Tomar fonfo de un chat)
           !sticker-- (poner stickers para el bot) 
           !giogle-- (Buscar en google)
           !comentame-- (Comenta en mi muro)
[c]───────────────────
[c]
[cu]⁽  ↳ 𝖽᥆̅𝗇'𝗍 𝗮𝗯𝘂.𝗌ᥱ̅! ⸺ 𝖻𝗒𝖾 𝖻𝗒𝖾 𝗌. 𝗐𝖾𝖾𝗍𝗂𝖾﹕
[c]
[c]⌊                          ⌋"""
      data.subClient.full_embed("http://aminoapps.com/u/Jon87153782", ff, msg, data.chatId)


@client.command("comentame")
def comment_profile(data):
    data.subClient.comment(message=data.message, userId=data.authorId)
    data.subClient.send_message(data.chatId, f"Listo, ya comenté. {data.author}")

@client.command("iconuser")
def iconuser(data):
    id=client.get_from_code(data.message).objectId
    image = data.subClient.get_user_info(id).icon
    filename = image.split("/")[-1]
    filetype = image.split(".")[-1]
    if filetype != "gif":
        filetype = "image"
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            with suppress(Exception):
                data.subClient.send_message(data.chatId, file=fp, fileType=filetype)
                os.remove(filename)

  
@client.command("acciones")
def acciones(data):
      img= open("pro.png", "rb")
      ias = ("help.jpg")
      im = open(".pr.png", "rb")
      yimg = open("youimage.png", "rb")
      Image.open(ias).resize((863, 400)).save("nsus.png")
      ff = open("nsus.png", "rb")
      msg = f"""[c]⌈                          ⌉
[c]
[uc]⁽ ↳ ♡'  𝗁ᥱ̅𝗒 𝗎. 𝗌𝖾𝗋 ⸺ 𝘄𝗲𝗹.𝖼᥆̅𝗆𝖾 ⭏ ¡ 💭̷ ! 
[c]﹫𝖨𝗋ᥱ̅𝗇𝖾'𝗌 𝖼. ᥆̅𝗆𝗆͟𝖺͟𝗇𝖽𝗌 ꜝ ﹝𔘓﹞⸺ 𝗎. 𝗌ᥱ̅ 𝗂𝗍 ˿
[c]
[c]⏝ .⏝ . ⏝ . ⏝ . ⏝. ⏝ . ⏝ . ⏝
[c]───────────────────
           !kiss-- (Dar un beso)                         
           !zape-- (Dar un zape)
           !cum-- (Dar lechita)                       
           !abrazo-- (Dar un abrazo)
           !bofetada-- (Dar una cachetada)               
           !mimos-- (Dar un mimito)
           !golpe-- (Dar un golpe)                     
           !nalgada-- (Dar una nalgada)
[c]───────────────────
[c]
[cu]⁽  ↳ 𝖽᥆̅𝗇'𝗍 𝗮𝗯𝘂.𝗌ᥱ̅! ⸺ 𝖻𝗒𝖾 𝖻𝗒𝖾 𝗌. 𝗐𝖾𝖾𝗍𝗂𝖾﹕
[c]
[c]⌊                          ⌋"""
      data.subClient.full_embed("http://aminoapps.com/u/Jon87153782", ff, msg, data.chatId)



@client.command("jail")
def jail(data):
			img=open(".jail.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aauile.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".jail.png").resize((800,800))
				img1 = Image.open(".aauile.png").resize((800,800))
				#img1.size 
				#img1_size = img1.resize((350, 350))
				img1.paste(img, (0,0),img)
				img1=img1.save(".i3i.png")
				imgg=open(".i3i.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass					
				
							
@client.command("trash")
def trash(data):
			img=open(".trash.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a77ale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".trash.png") 
				img1 = Image.open(".a77ale.png").resize((483,483))
				img.paste(img1, (480,0))
				img=img.save(".iw83.png")
				imgg=open(".iw83.png","rb")
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image")
				except:
					pass

@client.command("sticker")
def sticker(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
                                   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
                                   filename = image.split("/")[-1]
                                   filetype = image.split(".")[-1]
                                   if filetype!="gif":
                                               filetype = "image"
                                               urllib.request.urlretrieve(image, filename)
                                               with open(filename, 'rb') as fp:
                                                      with suppress(Exception):
                                                             data.subClient.send_message(data.chatId, file=fp, fileType=filetype)
                           
@client.command("mention")
def mention(args):
    try:
        size = int(args.message.strip().split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 1

    val = args.subClient.get_user_id(args.message)
    if not val:
        args.subClient.send_message(chatId=args.chatId, message="Username not found")
        return

    if size > 5 and not (client.check(args, 'itsme', 'admin')):
        size = 5

    if val:
        for _ in range(size):
            with suppress(Exception):
                args.subClient.send_message(chatId=args.chatId, message=f"‎‏‎‏@{val[0]}‬‭", mentionUserIds=[val[1]])

@client.command("hidden")
def hidden(args):
    value = 0
    size = 1
    ment = None
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId,asStaff=True,reason="Clear")

    if "chat=" in args.message:
        chat_name = args.message.rsplit("chat=", 1).pop()
        chat_ide = args.subClient.get_chat_id(chat_name)
        if chat_ide:
            args.chatId = chat_ide
        args.message = " ".join(args.message.strip().split()[:-1])

    try:
        size = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 0

    try:
        value = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        value = size
        size = 1

    if not args.message and value == 1:
        args.message = f"‎‏‎‏@{args.author}‬‭"
        ment = args.authorId

    if size > 10 and not (client.check(args, 'itsme', 'admin')):
        size = 10

    for _ in range(size):
        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"{args.message}", messageType=value, mentionUserIds=ment)
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time=now.strftime("%H:%M:%S")
            chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
            val=args.subClient.get_chat_thread(args.chatId).title
            chats=args.subClient.favorite_chats
            for id, in zip(chats) :
            	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} used hidden message in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")


@client.command("abw")
def add_banned_word(args):
    if client.check(args, 'staff', 'itsme', 'admin'):
        if not args.message or args.message in args.subClient.banned_words:
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.add_banned_words(ar)
        args.subClient.send_message(args.chatId, f"{args.message} added to banned words")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time=now.strftime("%H:%M:%S")
        
        chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
        val=args.subClient.get_chat_thread(args.chatId).title
        chats=args.subClient.favorite_chats
        for id, in zip(chats) :
        	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} added banned word

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")


@client.command("rbw")
def remove_banned_word(args):
    if client.check(args, 'staff', 'itsme', 'admin'):
        if not args.message:
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.remove_banned_words(ar)
        args.subClient.send_message(args.chatId, f"{args.message} removed from banned words")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time=now.strftime("%H:%M:%S")
        
        chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
        val=args.subClient.get_chat_thread(args.chatId).title
        chats=args.subClient.favorite_chats
        for id, in zip(chats) :
        	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} removed banned word

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")


@client.command("bwl")
def banned_word_list(args):
    val = ""
    if args.subClient.banned_words:
        for elem in args.subClient.banned_words:
            val +="◈" + elem + "\n"
    else:
        val = "No words in the list"
    args.subClient.send_message(args.chatId, val)

@client.command("chatlist")
def get_chats(args):
    val = args.subClient.get_chats()
    for te, _ in zip(val.title, val.chatId):
        args.subClient.send_message(args.chatId, te)

@client.command("bast")
def blst(data):
	if data.message:
		k=data.message
		d=int(k)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		val=data.subClient.get_chat_thread(data.chatId).title
		ch=data.subClient.favorite_chats
		for id in ch:
			for i in range(1):
				data.subClient.send_message(chatId=id,message=f"""[c]Blast command by {data.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

 {d} Messages cleared

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")

@client.command("xc")
def clhr(data):
	k=data.message
	d=int(k)
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
	chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
	val=data.subClient.get_chat_thread(data.chatId).title
	ch=data.subClient.favorite_chats
	for id in ch:
			data.subClient.send_message(chatId=id,message=f"""[c]Clear command by {data.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙??𐄙𐄁

 {d} Messages cleared

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
			a=data.subClient.get_chat_messages(chatId=data.chatId,size=d).messageId
			if d<=10:
				for i in a:
					data.subClient.delete_message(chatId=data.chatId,messageId=i,asStaff=True,reason="Clear")
			elif d>=10:
				data.subClient.send_message(chatId=data.chatId,message="Can't clear more than 10",replyTo=data.messageId)

        
@client.command("chatid")
def chatid(data):
	data.subClient.send_message(data.chatId,message=f"{data.chatId}",replyTo=data.messageId)
        
@client.command("chatids")
def chat_id(args):
    if client.check(args,'staff', 'admin','itsme'):
        val = args.subClient.get_chats()
        for title, chat_id in zip(val.title, val.chatId):
        	args.subClient.send_message(args.chatId, f"{title} | {chat_id}")
                
@client.command("deljson")
def deljson(data):
	del client[data.subClient.community_id]
	data.subClient.send_message(data.chatId,message="File deleted")	

def telecharger(url):
    music = None
    if ("=" in url and "/" in url and " " not in url) or ("/" in url and " " not in url):
        if "=" in url and "/" in url:
            music = url.rsplit("=", 1)[-1]
        elif "/" in url:
            music = url.rsplit("/")[-1]

        if music in os.listdir(path_download):
            return music

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            'extract-audio': True,
            'outtmpl': f"{path_download}/{music}.webm",
            }

        with YoutubeDL(ydl_opts) as ydl:
            video_length = ydl.extract_info(url, download=True).get('duration')
            ydl.cache.remove()

        url = music+".mp3"

        return url, video_length
    return False, False

def decoupe(musical, temps):
    size = 170
    with open(musical, "rb") as fichier:
        nombre_ligne = len(fichier.readlines())

    if temps < 180 or temps > 540:
        return False

    decoupage = int(size*nombre_ligne / temps)

    t = 0
    file_list = []
    for a in range(0, nombre_ligne, decoupage):
        b = a + decoupage
        if b >= nombre_ligne:
            b = nombre_ligne

        with open(musical, "rb") as fichier:
            lignes = fichier.readlines()[a:b]

        with open(musical.replace(".mp3", "PART"+str(t)+".mp3"),  "wb") as mus:
            for ligne in lignes:
                mus.write(ligne)

        file_list.append(musical.replace(".mp3", "PART"+str(t)+".mp3"))
        t += 1
    return file_list

@client.command("play")
def play(args):
    music, size = telecharger(args.message)
    if music:
        music = f"{path_download}/{music}"
        val = decoupe(music, size)

        if not val:
            try:
                with open(music, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="audio")
            except Exception:
                args.subClient.send_message(args.chatId, "Error! File too heavy (9 min max)")
            os.remove(music)
            return

        os.remove(music)
        for elem in val:
            with suppress(Exception):
                with open(elem, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="audio")
            os.remove(elem)
        return
    args.subClient.send_message(args.chatId, "Error! Wrong link")

@client.command("say")
def say(args):
    audio_file = f"{path_download}/tpp{randint(1,500)}.mp3"
    #langue = list(lang.tts_langs().keys())
    if not args.message:
        args.message = args.subClient.get_chat_messages(chatId=args.chatId, size=2).content[1]
    gTTS(text=args.message, lang='en', tld='com',slow=False).save(audio_file)
    try:
        with open(audio_file, 'rb') as fp:
            args.subClient.send_message(args.chatId, file=fp, fileType="audio")
    except Exception:
        args.subClient.send_message(args.chatId, "Too heavy!")
    os.remove(audio_file)
        
@client.command("stopamino")
def stop_amino(args):
    if client.check(args,'itsme'):
        args.subClient.stop_instance()
        del client[args.subClient.community_id]

@client.command("ask")
def ask_thing(args):
    if client.check(args, 'staff', 'admin','itsme'):
        lvl = ""
        boolean = 1
        if "lvl=" in args.message:
            lvl = args.message.rsplit("lvl=", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl="+lvl, "").strip()
        elif "lvl<" in args.message:
            lvl = args.message.rsplit("lvl<", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl<"+lvl, "").strip()
            boolean = 2
        elif "lvl>" in args.message:
            lvl = args.message.rsplit("lvl>", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl>"+lvl, "").strip()
            boolean = 3
        try:
            lvl = int(lvl)
        except ValueError:
            lvl = 20

        args.subClient.ask_all_members(args.message+f"\n[CUI]This message was sent by {args.author}\n[CUI]I am Alexa and have a nice day^^", lvl, boolean)
        args.subClient.send_message(args.chatId, "sending...")
        args.subClient.send_message(args.chatId, "send successfuly...",replyTo=args.messageId)

@client.command("askstaff")
def ask_staff(args):
    if client.check(args, 'itsme', 'admin'):
        amino_list = client.client.sub_clients()
        for commu in amino_list.comId:
            client[commu].ask_amino_staff(message=args.message)
        args.subClient.send_message(args.chatId, "Asking...")

@client.command("admi")
def admi(args):
    if client.check(args, 'staff'):
        if not args.message or args.message == "alock":
            return

        command = args.subClient.admin_locked_command
        args.message = [args.message]

        if args.message[0] in command:
            args.subClient.remove_admin_locked_command(args.message)
        else:
            args.subClient.add_admin_locked_command(args.message)

        args.subClient.send_message(args.chatId, "Locked command list updated")

@client.command("level")
def level(args):
    if client.check(args, 'staff', 'admin','itsme'):
        try:
            args.message = int(args.message)
        except Exception:
            args.subClient.send_message(args.chatId, "Error, wrong level")
            return
        if args.message > 20:
            args.message = 20
        if args.message < 0:
            args.message = 0
        args.subClient.set_level(args.message)
        args.subClient.send_message(args.chatId, f"Level set to {args.message}!")
@client.command("msg")
def msg(args):
    value = 0
    size = 1
    ment = None
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId,asStaff=True,reason="Clear")

    if "chat=" in args.message:
        chat_name = args.message.rsplit("chat=", 1).pop()
        chat_ide = args.subClient.get_chat_id(chat_name)
        if chat_ide:
            args.chatId = chat_ide
        args.message = " ".join(args.message.strip().split()[:-1])

    try:
        size = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 0

    try:
        value = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        value = size
        size = 1

    if not args.message and value == 1:
        args.message = f"‎‏‎‏@{args.author}‬‭"
        ment = args.authorId

    if size > 10 and not (client.check(args, 'staff')):
        size = 10

    for _ in range(size):
        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"{args.message}", messageType=value, mentionUserIds=ment)
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time=now.strftime("%H:%M:%S")
            chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
            val=args.subClient.get_chat_thread(args.chatId).title
            chats=args.subClient.favorite_chats
            for id, in zip(chats) :
            	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} used hidden message in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")

@client.command("blast")
def blast(data):
	if client.check(data,'staff'):
		k=data.message
		d=int(k)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		val=data.subClient.get_chat_thread(data.chatId).title
		ch=data.subClient.favorite_chats
		a=data.subClient.get_chat_messages(chatId=data.chatId,size=d).messageId
		for _ in range(d):
			for i in a:
				Thread(target=data.subClient.delete_message(chatId=data.chatId,messageId=i,asStaff=True,reason="Clear")).start()
		data.subClient.send_message(chatId=id,message=f"""[c]Blast command by {data.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

 {d} Messages cleared

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")


@client.command("limpieza")
def limpieza (data):
    if client.check(data,'staff'):
        if data.subClient.is_in_staff(client.userId):
            m= int(data.message)
            if m:
                chatMembers = data.subClient.get_chat_users(chatId=data.chatId, size=500)
                x= chatMembers.json
                for i in x:
                    s= i["level"]
                    o= i["uid"]
                    if s <= m:
                        try:
                            data.subClient.kick(chatId=data.chatId, userId=o, allowRejoin=True)
                            time.sleep(2)
                        except:
                            pass
            else:
                data.subClient.send_message(message="[IC]Usa limpieza x, x es el rango maximo de usuarios que saldran del chat",chatId=data.chatId)    
        else:
            data.subClient.send_message(message="[IC]Solo el staff puede hacer limpieza.",chatId=data.chatId)


@client.command("limp")
def lim (data):
    if client.check(data,'staff'):
        if data.subClient.is_in_staff(client.userId):
            m= int(data.message)
            if m:
                chatMembers = data.subClient.get_chat_users(chatId=data.chatId, size=500)
                x= chatMembers.json
                for i in x:
                    s= i["level"]
                    o= i["uid"]
                    if s <= m:
                        try:
                            data.subClient.kick(chatId=data.chatId, userId=o, allowRejoin=True)
                            time.sleep(2)
                        except:
                            pass
            else:
                data.subClient.send_message(message="[IC]Usa limpieza x, x es el rango maximo de usuarios que saldran del chat",chatId=data.chatId)    
        else:
            data.subClient.send_message(message="[IC]Solo el staff puede hacer limpieza.",chatId=data.chatId)


@client.command()
def bio(data):
    if client.check(data,'staff'):
       data.subClient.edit_profile(content=data.message)
       data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻ ❝Biografia cargada, {data.author}❞ ৴")


@client.command()
def sigueme(data):
    if client.check(data,'staff'):
        data.subClient.follow_user(data.authorId)
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝Te sigo, {data.author}❞ ৴", replyTo=data.messageId)

@client.command()
def s(data):
        data.subClient.follow_user(data.authorId)
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝Te sigo, {data.author}❞ ৴", replyTo=data.messageId)

@client.command()
def acepta(data):
    if client.check(data,'staff'):
        data.subClient.accept_role(data)
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝Ahora tengo el poder, {data.author}❞ ৴", replyTo=data.messageId)

@client.command()
def nomesigas(data):
    if client.check(data,'staff'):
        data.subClient.unfollow_user(data.authorId)
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝Ya no te sigo, {data.author}❞ ৴", replyTo=data.messageId)

@client.command()
def anfitrion(data):
    if client.check(data,'staff'):
        if data.subClient.is_in_staff(client.userId):
            mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
            if mention:
                for user in mention:
                    data.subClient.transfer_host(data.chatId,userIds=user)
                    data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝[IC] Anfi hecho, {data.author}❞ ৴")
            else:
                data.subClient.transfer_host(data.chatId,userIds=data.authorId)
                data.subClient.send_message(data.chatId,message=f"[IC]Anfi hecho")
        else:
            data.subClient.send_message(chatId=data.chatId, message=f"[IC]No eres staff")
    else:
        data.subClient.send_message(message=f"[IC]comando solo para el staff",chatId=data.chatId,replyTo=data.messageId)


@client.command(name="joinc")
def joinc(data):
    if client.check(data,'staff'):
        url = data.message
        code = client.get_from_code(url)
        community_id = code.path[1:code.path.index('/')]
        if 'extensions' in code.json and 'invitationId' in code.json['extensions']:
            invitation_id = code.json['extensions']['invitationId']
            client.join_community(community_id, invitation_id)
            data.subClient.send_message(data.chatId,"unido", replyTo=data.messageId)
        else:
            client.join_community(community_id)
        Thread(target=client.threadLaunch, args=[community_id, True]).start()
        data.subClient.send_message(data.chatId,"unido", replyTo=data.messageId)

@client.command("visu")
def visu(data):
    if client.check(data,'staff'):
       chatsito=data.subClient.get_chat_id(data.message)
       data.subClient.edit_chat(chatId=chatsito, viewOnly=True)

@client.command("desvisu")
def desvisu(data):
   if client.check(data,'staff'):
       chatsito=data.subClient.get_chat_id(data.message)
       data.subClient.edit_chat(chatId=chatsito, viewOnly=False)

@client.command()
def joinall(data):
   if client.check(data,'staff'):
        data.subClient.join_all_chat()
        data.subClient.send_message(data.chatId, f"[Ic]⸻Unido a todos los chats, {data.author}❞ ৴", replyTo=data.messageId)

@client.command()
def unetetodo(data):
        data.subClient.join_all_chat()
        data.subClient.send_message(data.chatId, f"[Ic]⸻Unido a todos los chats, {data.author}❞ ৴", replyTo=data.messageId)

@client.command("Testeo")
def test(data):
   if client.check(data,'staff'):
        data.subClient.send_message(data.chatId, f"[Ic]⸻Hola, {data.author}, estoy aqui❞ ৴", replyTo=data.messageId)

@client.command("bienvenida")
def bienvenida(data):
   if client.check(data,'staff'):
       data.subClient.set_welcome_message(data.message)
       data.subClient.send_message(data.chatId,f"[Ic]⸻ ❝mensaje cargado!{data.author}❞ ৴", replyTo=data.messageId)

@client.command(name="ban")
def ban(data):
    titulos= ['»🐾ᤲ ↴ 𝗥ə𝗽 ❞', 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            print('Usuario Autorisado')
            url = data.message
            print("url:", url)
            id=client.get_from_code(url).objectId
            data.subClient.get_user_info(id)
            data.subClient.ban(id, "Estaba haciendo spam")
            data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝ El usuario a sido expulsado, {data.author}❞ ৴", replyTo=data.messageId)

@client.command(name="invitar")
def invitar(data):
    titulos= ["( 𝕻 ) 𝐄̸̷ 𝐑 𝐔 𖤐", 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
             print('Usuario Autorisado')
             h=data.subClient.get_online_users(start=0,size=200).profile.userId
             j=data.subClient.get_online_users(start=0,size=200).profile.nickname
             u=len(j)
             for ud in h:
                data.subClient.invite_to_chat(userId=ud,chatId=data.chatId)
             for i in range(1):
                data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻Listo, ya invite a todos, {data.author}❞ ৴", replyTo=data.messageId)


@client.command()
def unete(data):
    if client.check(data,'staff'):
        url = data.message
        print("url:", url)
        id=client.get_from_code(url).objectId
        data.subClient.join_chat(chatId= id)
        data.subClient.send_message(data.chatId, message = f"[Ic]⸻Listo, me uni al chat, {data.author}❞ ৴", replyTo=data.messageId)

def inviteall(data):
    if client.check(data,'staff'):
        h=data.subClient.get_online_users(start=0,size=100).profile.userId
        j=data.subClient.get_online_users(start=0,size=100).profile.nickname
        u=len(j)
        for ud in h:
            data.subClient.invite_to_vc(userId=ud,chatId=data.chatId)
        for i in range(1):
            data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻Listo, ya invite a todos, {data.author}❞ ৴", replyTo=data.messageId)

@client.command("invitape")
def invitape(data):
    titulos= ["( 𝕻 ) 𝐄̸̷ 𝐑 𝐔 𖤐", 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            h=data.subClient.get_online_users(start=0,size=200).profile.userId
            j=data.subClient.get_online_users(start=0,size=200).profile.nickname
            u=len(j)
            for ud in h:
                data.subClient.invite_to_chat(userId=ud,chatId=data.chatId)
            for i in range(1):
                data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻Listo, ya invite a todos, {data.author}❞ ৴", replyTo=data.messageId)



@client.command("bgcolor")
def bgcolor(data):
    if client.check(data,'staff'):
        data.subClient.edit_profile(backgroundColor=data.message)
        data.subClient.send_message(chatId=data.chatId,message=f"[Ic]⸻Listo, fondo de color puesto, {data.author}❞ ৴",replyTo=data.messageId)

@client.command("background")
def background(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
		image = info.json['extensions']['replyMessage']['mediaValue']
		for i in range(1,3):
			try:
				data.subClient.edit_profile(chatRequestPrivilege=image)
			except Exception:
				data.subClient.send_message(data.chatId, message="BG pic changed",replyTo=data.messageId)
                        
@client.command("portada")
def portada(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
		image = info.json['extensions']['replyMessage']['mediaValue']
		for i in range(1,3):
			try:
				data.subClient.edit_profile(imageList=image)
			except Exception:
				data.subClient.send_message(data.chatId, message="BG pic changed",replyTo=data.messageId)
                        


@client.command("anuncio")
def anuncio(data):
    if client.check(data,'staff',):
        try:
            val =data.subClient.get_chats()
            val3=data.subClient.get_chat_thread(data.chatId).title
            for g, in zip(val.chatId):
                data.subClient.send_message(chatId=g,message=f"""
{data.message}""")
        except Exception:
            data.subClient.send_message(data.chatId,message=f"""
[Ic]⸻Listo, anuncio finalizado ❞ ৴
""")
afkdict={}

@client.command("anunciar")
def anunciar(data):
    titulos= ["( 𝕻 ) 𝐄̸̷ 𝐑 𝐔 𖤐", 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            try:
                val =data.subClient.get_chats()
                val3=data.subClient.get_chat_thread(data.chatId).title
                for g, in zip(val.chatId):
                    data.subClient.send_message(chatId=g,message=f"""
{data.message}""")
            except Exception:
                data.subClient.send_message(data.chatId,message=f"""[Ic]⸻Listo, anuncio finalizado ❞ ৴""")


@client.command("chatmem")
def chatmem(data):
    if client.check(data,'staff',):
        o=""
        q=data.subClient.get_chat_users(chatId=data.chatId,start=0,size=100).profile.nickname
        s=[q]
        y=s.append(q)
        for uid in y:
            o=o+uid+"\n"
        data.subClient.send_message(chatId=data.chatId,message=f"""
[c]⸻Miembros en linea ❞ ৴
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

@client.command("donar")
def donar(args):
        coins = args.subClient.get_wallet_amount()
        if coins >= 1:
            amt = 0
            while coins > 500:
                args.subClient.pay(500, chatId=args.chatId)
                coins -= 500
                amt += 500
            args.subClient.pay(int(coins), chatId=args.chatId)
            args.subClient.send_message(args.chatId, f"Sending {coins+amt} coins...")
        else:
            args.subClient.send_message(args.chatId, "Account is empty!")

@client.command(name="getusers")
def getusers(data):
    val = inspect.getmembers(data.subClient.get_all_users(start=0, size=5, type="recent"))
    for elem in val[3][1]['json']['userProfileList']:
        print(elem)
        print(elem['nickname'])
        
@client.command("clear")
def clear(data):
    if client.check(data,'staff'):
        k=data.message
        d=int(k)
        a=data.subClient.get_chat_messages(chatId=data.chatId,size=d).messageId
        if d<=20:
           for i in a:
                 data.subClient.delete_message(chatId=data.chatId,messageId=i,asStaff=True,reason="Clear")
        elif d>=20:
            data.subClient.send_message(chatId=data.chatId,message="Can't clear more than 10",replyTo=data.messageId)

@client.command("borrar")
def borrar(data):
    titulos= ["( 𝕻 ) 𝐄̸̷ 𝐑 𝐔 𖤐", 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            k=data.message
            d=int(k)
            a=data.subClient.get_chat_messages(chatId=data.chatId,size=d).messageId
            if d<=20:
                for i in a:
                    data.subClient.delete_message(chatId=data.chatId,messageId=i,asStaff=True,reason="Clear")
            elif d>=20:
                data.subClient.send_message(chatId=data.chatId,message="No puedes borrar mas de 20 mensajes, papi",replyTo=data.messageId)

                    
	#data.subClient.send_message(chatId=id,message=f"""[c]Clear command by {data.author}

#[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙??𐄙𐄁

 #{d} Messages cleared

#[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

#Chat : {chatlink}

#Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
        
@client.command(name="globl")
def globl(data):
    if client.check(data,'staff'):
        url = data.message
        print("url:", url)
        id=client.get_from_code(url).objectId
        data.subClient.get_user_info(id)
        AID=client.get_user_info(userId=str(id)).aminoId
        data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝ https://aminoapps.com/u/"+str(AID) + "❞ ৴", replyTo=data.messageId)

@client.command("level")
def level(args):
    if client.check(args, 'staff', 'admin','itsme'):
        try:
            args.message = int(args.message)
        except Exception:
            args.subClient.send_message(args.chatId, "Error, wrong level")
            return
        if args.message > 20:
            args.message = 20
        if args.message < 0:
            args.message = 0
        args.subClient.set_level(args.message)
        args.subClient.send_message(args.chatId, f"Level set to {args.message}!")

@client.command("google")
def google(args):
    msg = args.message.split(" ")
    msg = '+'.join(msg)
    args.subClient.send_message(chatId=args.chatId, message=f"https://www.google.com/search?q={msg}",replyTo=args.messageId)

@client.command("aceptar")
def aceptar(args):
    if client.check(args, 'staff','itsme'):
        if args.subClient.accept_role( args.chatId):
            args.subClient.send_message(args.chatId, "Accepted role")
            return
        val = args.subClient.get_notices(start=0, size=25)
        for elem in val:
            print(elem["title"])
        ans = None
        res = None

        for elem in val:
            if 'become' in elem['title'] or "host" in elem['title']:
                res = elem['noticeId']
            if res:
                ans = args.subClient.accept_role(res)
            if ans:
                args.subClient.send_message(args.chatId, "Aceptado!")
                return
        else:
            args.subClient.send_message(args.chatId, "Error!")


@client.command("info")
def info(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		ic=data.subClient.get_user_info(str(user)).icon
		response=requests.get(f"{ic}")
		file=open(".yays.png","wb")
		file.write(response.content)
		file.close()
		imgg=open(".yays.png","rb")
		repa= data.subClient.get_user_info(userId=str(user)).reputation
		h=data.subClient.get_user_info(userId=str(user)).nickname
		lvl = data.subClient.get_user_info(userId=str(user)).level
		crttime = data.subClient.get_user_info(userId=str(user)).createdTime
		followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
		profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
		commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
		posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
		followed = data.subClient.get_user_info(userId=str(user)).followingCount
		data.subClient.send_message(data.chatId,message=f"""
[C]Profile Info
[C]┅┅┅┅┅┅┅┅┅┅┅┅┅┅

•Nombre: {h}
•Id: {str(user)}
•Tiempo de creacion de la cuenta: {crttime}
•Perfil: {profilchange}
•Reputacion numero: {repa}
•Nivel de cuenta: {lvl}
•Numero de publicaciones: {posts}
•Numero de comentarios: {commentz}
•Siguiendo: {followed}
•Seguidores: {followers}""",embedImage=imgg,embedTitle=f"{h}",embedContent=f"Nivel {lvl}")
	

@client.command(name="glob")
def glob(data):
    titulos= ['»🐾ᤲ ↴ 𝗥ə𝗽 ❞', 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            print('Usuario Autorisado')
            url = data.message
            print("url:", url)
            id=client.get_from_code(url).objectId
            data.subClient.get_user_info(id)
            AID=client.get_user_info(userId=str(id)).aminoId
            data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝ https://aminoapps.com/u/"+str(AID) + "❞ ৴", replyTo=data.messageId)


@client.command(name="linkg")
def linkg(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    AID=data.subClient.get_user_info(userId=str(id)).aminoId
    data.subClient.send_message(data.chatId,message=f"[Ic]⸻ ❝ ndc://x{data.comId}/user-profile/{str(AID)}❞ ৴", replyTo=data.messageId)


@client.command()
def sacar(data):
    titulos= ['ೃ*    ೫. 𝘦𝘭𝘱ǝ𝘳   *୭̥', 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            print('Usuario Autorisado')
            mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
            for user in mention:
                h=data.subClient.get_user_info(userId=str(user)).nickname
                data.subClient.client.kick(userId=str(user), chatId=data.chatId, allowRejoin=False)
                data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝{h} a sido sacado del chat por este helper {data.author}❞ ৴", replyTo=data.messageId)

@client.command("chao")
def chao(data):
    titulos= ["( 𝕻 ) 𝐄̸̷ 𝐑 𝐔 𖤐", 'helper']
    x= data.subClient.get_user_info(data.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            print('Usuario Autorisado')
            mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
            for user in mention:
                h=data.subClient.get_user_info(userId=str(user)).nickname
                data.subClient.client.kick(userId=str(user), chatId=data.chatId, allowRejoin=False)
                data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝{h} a sido sacado del chat por el lider agente {data.author}❞ ৴", replyTo=data.messageId)


@client.command("all")
def mentionall(args):
    titulos= ["( 𝕻 ) 𝐄̸̷ 𝐑 𝐔 𖤐", 'helper']
    x= args.subClient.get_user_info(args.authorId).json['extensions']['customTitles']
    for titulo in x:
        title= titulo['title']
        if title in titulos:
            if args.message and client.check(args, 'itsme'):
                chat_ide = args.subClient.get_chat_id(args.message)
                if chat_ide:
                    args.chatId = chat_ide
                args.message = " ".join(args.message.strip().split()[:-1])

            mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId).userId]
            test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId).userId])

            with suppress(Exception):
                args.subClient.send_message(chatId=args.chatId, message=f"@everyone{test}", mentionUserIds=mention)



@client.command('linkinvite')
def linkinvite(data):
    if client.check(data,'staff'):
        if data.subClient.is_in_staff(client.userId):
            val = data.subClient.get_invite_codes()
            code= val.json
            for element in code:
                x=element['link']
                data.subClient.send_message(data.chatId, message=f"[IC]⸻ ❝Link: {x}❞ ৴", replyTo=data.messageId)
                time.sleep(2)
        else:
            data.subClient.send_message(data.chatId, message="[IC]⸻ ❝Necesitas ser lider❞ ৴")
    else:
        data.subClient.send_message(message="[IC]⸻ ❝Commando solo para el staff❞ ৴",chatId=data.chatId,replyTo=data.messageId)



@client.command()
def joinc(data):
    if client.check(data,'staff'):
        url = data.message
        code = client.get_from_code(url)
        community_id = code.path[1:code.path.index('/')]
        if 'extensions' in code.json and 'invitationId' in code.json['extensions']:
            invitation_id = code.json['extensions']['invitationId']
            client.join_community(community_id, invitation_id)
        else:
            client.join_community(community_id)
        Thread(target=client.threadLaunch, data=[community_id, True]).start()
        data.sub_client.send_message(data.chatId, message="Joined", replyTo=data.messageId)

@client.command(name="b")
def bansito(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    data.subClient.ban(id, "Estaba haciendo spam")
    data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝ El usuario a sido expulsado, {data.author}❞ ৴", replyTo=data.messageId)

@client.command(name="g")
def globalito(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    AID=client.get_user_info(userId=str(id)).aminoId
    data.subClient.send_message(data.chatId,message="[Ic]⸻ ❝ https://aminoapps.com/u/"+str(AID) + "❞ ৴", replyTo=data.messageId
    )

@client.command(name="bane")
def bane(data):
    if client.check(data,'staff'):
        url = data.message
        print("url:", url)
        id=client.get_from_code(url).objectId
        data.subClient.get_user_info(id)
        data.subClient.ban(id, "Estaba haciendo spam")
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝ El usuario a sido expulsado, {data.author}❞ ৴", replyTo=data.messageId)


@client.command(name="bansito")
def bansito(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    chat="25cced0a-7978-484c-a52b-bd7a4e2f8a3a"
    if data.message in chat:
        ids="1fb0766e-70b6-417d-8e42-971dc73d76ae"
        data.subClient.ban(id, "Estaba haciendo spam")
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝ El usuario a sido expulsado, {data.author}❞ ৴", replyTo=data.messageId)
    data.subClient.send_message(chatId=ids, message=f"[Ic]⸻ ❝ {data.author}, a expulsado a, {url}❞ ৴", replyTo=data.messageId)

@client.command(name="banepin")
def banepin(data):
    if client.check(data,'staff'):
        url = data.message
        print("url:", url)
        id=client.get_from_code(url).objectId
        data.subClient.get_user_info(id)
        data.subClient.ban(id, "Perfil inadecuado y no cambiado en 7 dias")
        data.subClient.send_message(data.chatId, f"[Ic]⸻ ❝ El usuario con perfil inadecuado a sido expulsado, {data.author}❞ ৴", replyTo=data.messageId)

@client.command("userid")
def userid(data):
    data.subClient.get_user_info(data.authorId).reputation
    data.subClient.send_message(data.chatId, message=f"""
[C]Nickname: {data.author}
[C]UserId: {data.authorId}""")      

@client.command("id")
def id(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.get_user_info(str(user)).reputation
        data.subClient.send_message(data.chatId, message=f"""
[C]Nickname: {data.author}
[C]UserId: {data.authorId}""") 


@client.command("icon")
def icon(args):
    if client.check(args, 'staff'):
        info = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
        reply_message = info.json['extensions']
        if reply_message:
            image = info.json['extensions']['replyMessage']['mediaValue']
        filename = image.split("/")[-1]
        filetype = image.split(".")[-1]
        if filetype != "gif":
            filetype = "image"
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as image:
            for i in range(1,3):
                try:
                    args.subClient.edit_profile(icon=image)
                except Exception:
                        args.subClient.send_message(args.chatId, message="ready",replyTo=args.messageId)

print("El bot inicio")
client.launch(True)