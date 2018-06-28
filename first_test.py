import discord
from discord.ext.commands import Bot
from discord.ext import commands
#from flask import Flask, request, abort

#app = Flask(__name__)

TOKEN = "NDM2NjczODQzMTAxMTcxNzMy.DhXOtA.zHQKVp9UKeFrCisivE4uUhQykeQ"

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('strange '):
        msg = 'Hello {0.author.mention} I have been expecting you.'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


    
client.run(TOKEN)
if __name__ == "__main__":
    client.run(TOKEN)
#    app.run(host='0.0.0.0',port=os.environ['PORT'])
