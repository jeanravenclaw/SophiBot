import discord
from discord.ext import tasks, commands
from datetime import datetime
from datetime import date
import calendar

class Crons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.before_cron()
        self.cron.start()
    
    @tasks.loop(minutes=1)
    async def cron(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)
        channel = self.bot.get_channel(768095329244413995)

        def double_digits(num):
            num = str(num)
            if len(num) < 2:
                num = "0" + num
            return num

        def start(name : str):
            my_date = date.today() # gets day
            day = calendar.day_name[my_date.weekday()]  #'Wednesday'
            
            time = current_time
            split = time.split(":")
            
            hour = int(split[0])
            minute = int(split[1])
            ampm = "am"
            
            hour += 3 # add 3 to the hour

            if hour > 12:
                hour -= 12
                ampm = "pm"
            
            # convert to double digits
            hour = double_digits(hour)
            minute = double_digits(minute)

            new_time = f"{hour}:{minute} {ampm}"

            embed = discord.Embed(
                title = f'{day} | {new_time}', 
                description = f'{name}')
            return embed

        if current_time == "04:00": 
            embed = start("Tutor Period")
            await channel.send(embed=embed)

        if current_time == "04:20": 
            embed = start("**Period 1**")
            await channel.send(embed=embed)
        if current_time == "05:00": 
            embed = start("Period 2")
            await channel.send(embed=embed)

        if current_time == "05:40": 
            embed = start("**Period 3**")
            await channel.send(embed=embed)
        if current_time == "06:20":
            embed = start("Period 4")
            await channel.send(embed=embed)

        if current_time == "07:00":
            embed = start("**Break 1**")
            await channel.send(embed=embed)

        if current_time == "07:25":
            embed = start("**Period 5**")
            await channel.send(embed=embed)
        if current_time == "08:05":
            embed = start("Period 6")
            await channel.send(embed=embed)

        if current_time == "08:45":
            embed = start("**Break 2**")
            await channel.send(embed=embed)
            
        if current_time == "09:10":
            embed = start("**Period 7**")
            await channel.send(embed=embed)
        if current_time == "09:50":
            embed = start("Period 8")
            await channel.send(embed=embed)

        if current_time == "10:30":
            embed = start("**Dismissal**")
            await channel.send(embed=embed)
            
        
        """ 
        07:00 am = 04:00
        08:00 am = 05:00
        09:00 am = 06:00
        10:00 am = 07:00
        11:00 am = 08:00
        12:00 am = 09:00
        01:00 pm = 10:00
        02:00 pm = 11:00
        03:00 pm = 12:00
        04:00 pm = 13:00
        \"""
        
        if current_time == "14:25":
            await channel.purge(limit=100)
            embed = start("**Lesson Alarms!**\n" + \
            "From now on, you'll get lesson alarms from SophiBot!\n" + \
            "This will provide us with more detailed info and more frequent reminders.")
            await channel.send(embed=embed)
        """ 
        

        # UTC = time - 3h

    @cron.before_loop
    async def before_cron(self):
        await self.bot.wait_until_ready() 

def setup(bot):
    bot.add_cog(Crons(bot))