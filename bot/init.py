from configs.config import settings
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

bot = Bot(token=settings.TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def checking_properties():
    logger.debug(f'Token is - {settings.TOKEN is not None} admin is - {settings.ADMIN_ID is not None}')
