import logging

from configs.config import settings
from aiogram.utils import executor
from bot.init import dispatcher


logging.basicConfig(
    level=settings.LOGGER_LEVEL,
    # filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S'
    )
logger = logging.getLogger(__name__)


async def on_startup(_):
    logger.info('Bot start!')


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
