from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
from replit import db
from discord.ext import commands
from func.data import value_check
from func.data import get_rank
from func.data import progress_bar

# cooldown
message_cooldown = commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.user)

"""

lvl = current level
lvl_xp = current xp
lvl_next = how much xp you need for next level

"""

class Levelling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # adds the user xp every 1 minute of messaging
    @commands.Cog.listener('on_message')
    async def foo(self, message: discord.Message):
        channel = message.channel
        author = message.author
        if author.bot == False:
            # await channel.send("")
            authorid = message.author.id

            # sets default values to avoid errors
            value_check(authorid, "lvl", 0)
            value_check(authorid, "lvl_xp", 0)
            value_check(authorid, "lvl_next", 1)
            
            # cooldown stuff
            bucket = message_cooldown.get_bucket(message)
            retry_after = bucket.update_rate_limit()

            var = db[str(authorid)] # your id's value
            # var["key"] is the value of 'key'
            # eg. the value of var["lvl_xp"]

            if retry_after: # if there's a cooldown
                retry = round(retry_after)
                print(f"xp for {message.author} in {retry} seconds")

            else: # add xp to user
                rand = random.randint(5, 7)
                var["lvl_xp"] += rand
                print(f"{message.author} recieved {rand} xp and now has {var['lvl_xp']}.")

            if var["lvl_xp"] >= var["lvl_next"]: # if they could level up
                var["lvl_xp"] = var["lvl_xp"] - var["lvl_next"]
                
                if var['lvl'] == 0: # if they ranked up for the first time
                    var['lvl_next'] = 100 # set next level to 100
                else: # else set next level to this:
                    var["lvl_next"] += round(var["lvl_next"] / 5) # whatever calculation

                var["lvl"] += 1 # level up

                print(f"{message.author} levelled up to level {var['lvl']}")
                await message.channel.send(f"<@{message.author.id}> levelled up to level {var['lvl']}!")
    
    @commands.command(
        name="rank",
        help="Checks your current rank in the server's levelling system.",
        brief="Checks your current rank.")
    async def rank(self, ctx):
        u = ctx.author
        rank = get_rank(u.id)
        var = db[str(u.id)]
        bar = progress_bar(var["lvl_xp"], var["lvl_next"])

        print(bar)

        embed = discord.Embed(
            # title = f"{u} | #{rank}", 
            description = f"{bar}"
        )

        embed.set_author(
            name = u,
            icon_url = u.avatar_url
        )

        embed.add_field(
            name = f"Level {var['lvl']}", 
            value = f"{var['lvl_xp']} / {var['lvl_next']}", 
            inline=True
        )

        embed.add_field(
            name = f"Rank {rank}", 
            value = f"{var['lvl_next'] - var['lvl_xp']} xp left", 
            inline=True
        )
        
        """ print(f"https://api.no-api-key.com/api/v2/rank?user_image={u.avatar_url}&text_heading=hey%20there%20lol&username={u.name}&level= {var['lvl']}&rank=1&total_xp={var['lvl_next']}&current_xp={var['lvl_xp']}&usertag={u.discriminator}&primary=white&secondary=crimson&background=https://cdn.discordapp.com/attachments/743128328705409080/771288922222231552/unknown.png") """
        await ctx.send(embed=embed)

    @commands.command(
        name="leaderboard",
        help="Displays the server's levelling leaderboard",
        brief="Displays the server's leaderboard",
        aliases=["lb", "ranks"])
    async def leaderboard(self, ctx):
        # var = db[str(ctx.author.id)]

        keys = db.keys()
        list_of_dicts = []

        for user_key in keys:
            # user_key is just a key (aka string)
            u = db[str(user_key)] # get the db value of the key
            lvl = u["lvl"]
            lvl_xp = u["lvl_xp"]
            # lvl_next = u["lvl_next"]
            # we don't need this lol

            user_dict = {
                "id": user_key,
                "level": lvl,
                "xp": lvl_xp
            } # this way, our data can be used easily

            list_of_dicts.append(user_dict)

        """ 
        list_of_dicts = [
            {
                "id": "id",
                "level": "level"
                "xp": "xp",
            },
            {
                "id": "690173341104865310",
                "level": "1"
                "xp": "63",
            },
        ]
        """

        # print(list_of_dicts)
        def myFunc(e):
            return e["level"]
        
        list_of_dicts.sort(reverse=True, key=myFunc)

        new_list = []
        iterator = 0

        for u in list_of_dicts:
            iterator += 1
            # this is a list of strings instead of 
            # a list of dictionaries
            string = f"`{iterator}` | <@{u['id']}> - level {u['level']}"
            new_list.append(string)

        description = "\n".join(new_list)

        embed = discord.Embed(
            title = f"User Leaderboard", 
            description = description
        ) 

        """

        lvl = current level
        lvl_xp = current xp
        lvl_next = how much xp you need for next level

        """

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Levelling(bot))