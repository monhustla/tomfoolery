import discord
import web
urls = (
'/input', 'index'
)
class index:
    def GET(self):
        i = web.input(name=None)
        return render.index(i.name)
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
render = web.template.render('templates/')
TOKEN = "NDM2NjczODQzMTAxMTcxNzMy.DhXOtA.zHQKVp9UKeFrCisivE4uUhQykeQ"

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
