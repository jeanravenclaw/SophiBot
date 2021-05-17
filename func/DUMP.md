# embeds
```py
# embeds

embed = discord.Embed(title = 'Test Embed', description = 'hello world')
embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too

# Images
embed.set_image(url = 'Image Url')
embed.set_thumbnail(url = 'Image Url')

embed.set_author(name = 'Author name', url = 'Url to author', icon_url = 'Image Url') # appears on top
embed.set_footer(text = 'Example footer', icon_url = 'Image Url') 
embed.timestamp = datetime.datetime.utcnow() 

embed.add_field(name = 'Name [256 char max]', value = 'Content [1024 char]', inline=True) 
# max 25 fields

# Async:
await bot.say(embed=embed)
# or: await bot.send_message(channel, embed=embed)

# Rewrite:
await ctx.send(embed=embed)
 # or: await channel.send(embed=embed)
```