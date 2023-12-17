from telethon.sync import TelegramClient, events
from random import randint
import asyncio

# '~' == your info
api_id = 25655106
api_hash = 'd7293f5b1b6277b7b4230dc71fcab1de'
phone_number = '+375256081568'
client = TelegramClient(phone_number, api_id, api_hash)
f = open('info.txt', 'r')
a = f.read().split()
chat_id = int(a[0])
friend_id = int(a[1])

ANSWERS = ['ну ой ой ой', '🗿', '"я больше не буду парить вам мозги"', 'топ 100 адекватности, просто удача -100',
           'надоело гэта слухаць', 'fired.gif', 'emoji-drop.gif', 'brainbang.gif', 'kekw.gif']

@client.on(events.NewMessage(chats=chat_id))
async def handle_new_message(event: events):
    sender = await event.get_sender()
    if sender.id == friend_id:
        ANSWERS.append(event.message.text[::-1])
        mes = ANSWERS[randint(0, len(ANSWERS) - 1)]
        del ANSWERS[-1]
        if '.gif' in mes:
             await event.reply(file=mes)
        else:
             await event.reply(mes)
        

async def main():
    async with client:
        client.add_event_handler(handle_new_message, events.NewMessage(chats=chat_id))
        await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
