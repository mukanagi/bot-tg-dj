import asyncio
from django.core.management.base import BaseCommand
from apps.bot.main_bot import bot


class Command(BaseCommand):
    help = "Load the bot"

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
        print("++++++++++++ Bot was stoped +++++++++++++")
