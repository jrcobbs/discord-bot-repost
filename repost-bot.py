import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='repost')
async def repeat_image(ctx, count: int):
    # Check if there's an attachment in the message
    if ctx.message.attachments:
        attachment_url = ctx.message.attachments[0].url
        for _ in range(count):
            await ctx.send(attachment_url)
    else:
        await ctx.send("No image found in the message!")

# Get the bot token from environment variable
TOKEN = os.getenv('BOT_TOKEN')

if TOKEN:
    bot.run(TOKEN)
else:
    print("Bot token not found!")
