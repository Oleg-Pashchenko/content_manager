import os

import yadisk
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('YANDEX_DISK_TOKEN')


async def upload(filename):
    y = yadisk.YaDisk(token=token)
    y.upload(filename, filename)

