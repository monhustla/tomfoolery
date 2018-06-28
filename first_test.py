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
        #print(client.user)
        return

    if message.content.startswith('Strange '):
        msg = 'Hello {0.author.mention} I have been expecting you.'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        #print(client.user)
        return

    if message.content.startswith('Strange who is the king?'):
        print(message.author)
        msg = 'Either {0.author.mention}, or King Joey.'.format(message)
        await client.send_message(message.channel, msg)        

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Who is king joey?'):
        print(message.author)
        msg = 'King Joey is above the one above all. A pioneer, a savant, philanthropist, but most importantly he is the interpreter of the majestic 1992 Marvel Power Ranking Cards. Some say he is the Oracle of Delphi reincarnated, only time will tell.'.format(message)
        await client.send_message(message.channel, msg)          

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        #print(client.user)
        return
    
    if ('daour') in message.content or ('@daour') in message.content or ('Daour') in message.content:
    #if message.content.contains('@daour') or (message.content.contains('daour')):
        print(message.author)
        print(message.author.roles)
        print '{0.author.roles}'
        msg = 'Frankie wishes he could take on daours knowledge'.format(message)
        await client.send_message(message.channel, msg)             

     
@client.event
async def on_message(message):
    if message.content.startswith('strange assign me'):
        mention_role = 'poop'
        if 'poop' in mention_role:
            role = '0x7f88982147c8'
async def alert(message, role):
    await client.add_roles(message.author, role)
    await client.send_message(message.channel, f'{message.server.default_role}, {message.author.mention} has been added to {role.mention}!!')


@client.event
async def on_message(message):
    if message.content.startswith('strange assign me'):
        assigned_role = discord.utils.get(
            message.server.roles, id=assigned_role_id)
        if assigned_role not in message.author.roles:
            for word in trigger_words:
                if case_sensitive:
                    if word in message.content:
                        await alert(message, assigned_role)
                        return
                else:
                    if word.lower() in message.content.lower():
                        await alert(message, assigned_role)
                        return        
                        
                       
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
