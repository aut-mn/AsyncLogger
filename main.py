"""AsyncLogger, an asynchronous logging utility"""
import asyncio, aiofiles
from datetime import datetime

class AsyncLogCollector:
    def __init__(self, filename):
        if not filename: raise ValueError("Filename cannot be None or empty.")
        self.filename = filename
        self.log_format = "%(timestamp)s [%(level)s] %(message)s"
        self.log_queue = asyncio.Queue()
        self.log_levels = {'DEBUG': '\033[90mDEBUG\033[0m', 'INFO': '\033[32mINFO\033[0m', 'WARN': '\033[33mWARN\033[0m', 'ERROR': '\033[31mERROR\033[0m', 'FATAL': '\033[31;1mFATAL\033[0m'}
    async def log(self, level, message):
        timestamp = self.get_colored_timestamp()
        print(self.log_format % {'timestamp': timestamp, 'level': self.log_levels.get(level, level), 'message': message})
        async with aiofiles.open(self.filename, mode='a') as file: await file.write(self.log_format % {'timestamp': self.get_timestamp(), 'level': level, 'message': message} + '\n')
    async def debug(self, message): await self.log('DEBUG', message)
    async def info(self, message): await self.log('INFO', message)
    async def warn(self, message): await self.log('WARN', message)
    async def error(self, message): await self.log('ERROR', message)
    async def fatal(self, message): await self.log('FATAL', message)
    def get_colored_timestamp(self): return '\033[90m' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\033[0m'
    @staticmethod
    def get_timestamp(self): return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
