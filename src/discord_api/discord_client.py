import os
from dotenv import load_dotenv
from discord.client import Client
from discord.flags import Intents
from discord.message import Message

from openai_api.openapi_connector import get_chat_gpt_response

load_dotenv()

bot_caller: str = "/bot"

discord_token = os.environ.get("DISCORD_TOKEN")


class CustomDiscordClient(Client):
    async def on_ready(self):
        print(f"--- Estou conectado ao Discord com o user {self.user} ---")

    async def on_message(self, message: Message):
        message_content: str = message.content
        if bot_caller in message_content:
            prompt: str = message_content.split(bot_caller)[1]
            print(f"--- User message: {prompt} ---")
            await message.channel.send(content="Processando resposta...")
            chat_gpt_response: str = get_chat_gpt_response(question=prompt)
            if chat_gpt_response:
                print(f"--- IA message: {chat_gpt_response} ---")
                await message.channel.send(content=chat_gpt_response)
            else:
                await message.channel.send(
                    content="Erro ao processar pergunta, tente novamente."
                )


intents = Intents.default()
intents.message_content = True
custom_discord_client: CustomDiscordClient = CustomDiscordClient(intents=intents)
