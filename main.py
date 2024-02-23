import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    if message.author.bot:
        return

    print(f'[{message.channel}] {message.author}> {message.content}')
    try:
        await message.channel.send('Hello!')
    except Exception as e:
        print(e)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
