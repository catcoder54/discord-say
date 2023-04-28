import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('./say'):
        text = message.content.replace('./say', '').strip()

        # Send message
        channel = message.channel
        await channel.send(text)

        # Delete original message
        await message.delete()

client.run('your-token-here')
