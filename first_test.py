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
     
    print(message.content)
    print(message.author)

    if ('daour') in message.content or ('@daour') in message.content or ('Daour') in message.content:
    #if message.content.contains('@daour') or (message.content.contains('daour')):
        print(message.author)
        print(message.author.roles)
        print ('{0.author.roles}')
        msg = 'Frankie wishes he could take on daours knowledge'.format(message)
        await client.send_message(message.channel, msg)  
        return
       
    '''   
    if message.content.startswith('Hi Strange'):
        msg = 'Hello {0.author.mention} I have been expecting you.'.format(message)
        await client.send_message(message.channel, msg)
        return
    if ('cancer') in message.content:
        print(message.author)
        msg = 'Sataniel is cancer indeed.'.format(message)
        await client.send_message(message.channel, msg)        
        return      
    if ('Strange who is the king') in message.content:
        print(message.author)
        msg = 'Either {0.author.mention}, or King Joey.'.format(message)
        await client.send_message(message.channel, msg)        
        return    
    if ('him') in message.content or ('Him') in message.content:
        msg = 'Him is a godly man.'.format(message)
        await client.send_message(message.channel, msg)
        return       
    if message.content.startswith('Who is king joey?'):
        print(message.author)
        msg = 'King Joey is above the one above all. A pioneer, a savant, philanthropist, but most importantly he is the interpreter of the majestic 1992 Marvel Power Ranking Cards. Some say he is the Oracle of Delphi reincarnated, only time will tell.'.format(message)
        await client.send_message(message.channel, msg) 
        return     
    ''' 
    if message.content.startswith('strange assign me'):
        #msg = 'trying to add this role {0.author.roles}'.format(message)
        #await client.send_message(message.channel, msg)   
        author = message.author
        role_names = [role.name for role in author.roles]
        print(role_names)
        role = discord.utils.get(message.server.roles, name="him role")     
        msg = 'trying to add this role {0.author.roles}'.format(message)
        await client.add_roles(message.author, role)           
        await client.send_message(message.channel, msg) 
        print('role assignment')   
        return

        
      
  
       
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    return

client.run(TOKEN)

if __name__ == "__main__":
    client.run(TOKEN)
#    app.run(host='0.0.0.0',port=os.environ['PORT'])
