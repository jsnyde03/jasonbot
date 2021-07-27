import asyncio
import discord
import logging
import os
import config
import restock_monitor

class DiscordTask(discord.Client):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get("messages") is None:
            raise Exception("no messages to send")
        if kwargs.get("monitor") is None:
            raise Exception("no database provided")
        
        self.messages = kwargs.get("messages")
        self.monitor = kwargs.get("monitor")
    
    async def on_ready(self):
        logging.info('Logged in as {}#{}'.format(self.user.name, self.user.id))
        try:
            await self.monitor.publish_new_products(self.messages, self)
        except Exception as e:
            logging.exception(e)
        finally:
            await self.close()