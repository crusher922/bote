from telethon import TelegramClient, events

# Reemplaza con tus datos
api_id = 24587662
api_hash = 'eb9d992d7a73c15b6d0acfd6f2e9c1c4'

# Crea el cliente
client = TelegramClient('session_name', api_id, api_hash)


# Función para reenviar mensajes
async def reenviar_mensaje(message, chat_destino):
    # Reenvía el mensaje
    await client.send_message(chat_destino, message)


# Escucha nuevos mensajes en el chat origen
@client.on(events.NewMessage)
async def main(event):
    chat_origen = [-1001629605754, -1001179560361]

    chat_destino = -4106805637

    if event.chat_id in chat_origen:
        modified_message = "     👑💎💵💴  ACE Trading  💷💶💎👑 \n\n" + event.message.text

        await client.send_message(chat_destino, modified_message)


# Inicia el bucle de eventos del cliente
client.start()
client.run_until_disconnected()