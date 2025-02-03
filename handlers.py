from aiogram import F, Router
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

def setup_routers(dp: Dispatcher):
    router = Router()