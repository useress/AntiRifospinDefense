from telethon.sync import TelegramClient, events
from random import randint

api_id = 25655106
api_hash = 'd7293f5b1b6277b7b4230dc71fcab1de'
phone_number = '+375256081568'
client = TelegramClient(phone_number, api_id, api_hash)
chat_id = -1001855909836 

ANSWERS = ['ну ой ой ой', '🤡', '"я больше не буду парить вам мозги"', 'топ 100 адекватности, просто удача -100',
           'надоело гэта слухаць', 'fired.gif', 'emoji-drop.gif', 'brainbang.gif', 'kekw.gif']

def generate_answer(mes: str):
       pass 

@client.on(events.NewMessage(chats=chat_id))
async def handle_new_message(event: events):
    sender = await event.get_sender()
    if sender.id == 948419219:
        ANSWERS.append(event.message.text[::-1])
        x = randint(0, len(ANSWERS) - 1)
        
        if '.gif' in ANSWERS[x]:
             await event.reply(file=ANSWERS[x])
        else:
             await event.reply(ANSWERS[x])

if __name__ == '__main__':
    
    client.start()
    client.run_until_disconnected()
