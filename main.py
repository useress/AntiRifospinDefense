from telethon.sync import TelegramClient, events
from random import randint

# '~' == your info
api_id = '~'
api_hash = '~'
phone_number = '~'
client = TelegramClient(phone_number, api_id, api_hash)
chat_id = '~' 

ANSWERS = ['ну ой ой ой', '🤡', '"я больше не буду парить вам мозги"', 'топ 100 адекватности, просто удача -100',
           'надоело гэта слухаць', 'fired.gif', 'emoji-drop.gif', 'brainbang.gif', 'kekw.gif']

def generate_answer(mes: str):
       pass 

@client.on(events.NewMessage(chats=chat_id))
async def handle_new_message(event: events):
    sender = await event.get_sender()
    if sender.id == '~':
        ANSWERS.append(event.message.text[::-1])
        x = randint(0, len(ANSWERS) - 1)

        if '.gif' in ANSWERS[x]:
             await event.reply(file=ANSWERS[x])
        else:
             await event.reply(ANSWERS[x])

if __name__ == '__main__':
    
    client.start()
    client.run_until_disconnected()
