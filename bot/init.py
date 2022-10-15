from configs.config import settings
from aiogram import Bot, Dispatcher
import logging

bot = Bot(token=settings.token)
dispatcher = Dispatcher(bot)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start():
    logger.debug(f'Token is - {settings.token} admin is - {settings.admin_id}')
