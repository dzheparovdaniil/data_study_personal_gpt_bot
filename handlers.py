from aiogram import types, F, Router
from bot import bot
from aiogram.filters import CommandStart
from config import MISTRAL_TOKEN
from mistralai import Mistral
from aiogram.types import CallbackQuery, Message
import os

router = Router()


@router.message(CommandStart())
async def message_handler(message: types.Message):
        await message.answer('привет! \n это GPT-бот, можешь писать любые вопросы в чат')

@router.message(F.text)
async def message_handler(message: types.Message):
          msg = await message.answer('происходит обработка...')
          await message.answer(await generate_ai_answer(message.text), parse_mode='Markdown')
          await msg.delete()


conversation_history = []
async def generate_ai_answer(message):
        api_key = MISTRAL_TOKEN
        model = "mistral-large-latest"

        client = Mistral(api_key=api_key)

        conversation_history.append({"role": "user", "content": message})

        chat_response = client.chat.complete(
            model = model,
            messages = conversation_history
        )

        conversation_history.append({"role": "assistant", "content": chat_response.choices[0].message.content})
        return chat_response.choices[0].message.content
        