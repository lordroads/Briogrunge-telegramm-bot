import logging

from configs.config import settings
from aiogram.utils import executor
from bot.init import dispatcher
from handlers import client


logging.basicConfig(
    level=settings.LOGGER_LEVEL,
    # filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S'
    )
logger = logging.getLogger(__name__)

client.register_handlers_client(dispatcher)


async def on_startup(_):
    logger.info('Bot start!')


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
