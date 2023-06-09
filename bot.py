"""
MIT License

Copyright (c) 2023 --卡拉马里毒药..

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import Engine
import os, requests
from colorama import *
import discord, random
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)
exceptions = [
    'png', 'jpg', 'jpeg', 'gif',  # Images
    'bmp', 'tiff', 'webp', 'svg', 'ico',
    'mp4', 'avi', 'mov', 'wmv', 'mkv',  # Videos
    'flv', 'webm', 'm4v', '3gp', 'mpeg',
    'mp3', 'wav', 'flac', 'aac', 'wma',  # Songs
    'ogg', 'm4a', 'alac', 'opus', 'mid'
    # Add more formats as needed
]


class fData:
    dtoken="DISCORD-BOT-TOKEN"
    virusTotal_APIKey="VIRUS-TOTAL-API-KEY"

class Menu(discord.ui.View):
    @discord.ui.button(label="🧪 Detections", style=discord.ButtonStyle.green)
    async def menu1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("s1")
    @discord.ui.button(label="💉 Signatures", style=discord.ButtonStyle.green)
    async def menu2(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("s2")
    @discord.ui.button(label="❌ Report", style=discord.ButtonStyle.green)
    async def menu3(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f'**Report Feature has not been setup by administrator.**')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="📛 10.3k Servers 📛"))
    await client.tree.sync()

@client.event
async def on_message(message):
    if str(message.attachments) == '[]':
        pass
    else:
        if message.author.bot:
            pass
        else:
            global s
            split_v1 = str(message.attachments).split("filename='")[1] # Split Attatchment into filename, url, filetype,
            filename = str(split_v1).split("' ")[0]
            url=str(message.attachments[0])
            filetype = str(os.path.splitext(filename)[1]).replace('.', '')
            # md5, total, detected, fileType, fileSize, scanDate, scanUrl, cachedir, filename
            await message.reply(f'**Woah {message.author.mention}, Please wait while we scan your files for any suspicous malware or virus like content, Thank you.**')
            unique_identifier = random.randint(1, 192648)
            print(unique_identifier)
            os.makedirs(f'cache\\{unique_identifier}')
            r=requests.get(url, allow_redirects=True)
            open(f'cache\\{unique_identifier}\\{filename}', 'wb').write(r.content)
            s=Engine.Engine.scanFile(cachedir=f"cache\\{unique_identifier}", filename=f"{filename}", filetype=f"{filetype}")
            embed = discord.Embed(title=f'Malware Analysis', colour=discord.Colour.blue())
            embed.set_author(name=f"{filename}", url=f"{s[6]}", icon_url=f"{s[6]}")
            embed.set_thumbnail(url=f"{message.author.avatar}")
            embed.add_field(name=f'🦠 Detections', value=f"{s[2]}/{s[1]}")
            embed.add_field(name=f'📁 File Size', value=f"{s[4]}MB")
            embed.add_field(name=f'🔒 File Type', value=f"{s[3]}")
            if s[2] < 10:
                embed.add_field(name='💉 Status', value='🟢 Safe / Trusted')
            elif s[2] >= 10 and s[2] < 15:
                embed.add_field(name='💉 Status', value='🟡 Low Risk / False-Positive')
            elif s[2] >= 15 and s[2] < 20:
                embed.add_field(name='💉 Status', value='🟡 Moderate Risk / Suspicous Activity')
            elif s[2] >= 20 and s[2] < 30:
                embed.add_field(name='💉 Status', value='🟠 Elevated Risk / Use At Risk ')
            elif s[2] >= 30 and s[2] < 42:
                embed.add_field(name='💉 Status', value='🔴 High Risk / Dangerous')
            else:
                embed.add_field(name='💉 Status', value='⚫ Critical Risk / Malicous')
            if s[2] > 24:
                embed.add_field(name='📢 Report', value='This file has been reported for further analysis.', inline=True)
            else:
                embed.add_field(name='📢 Report', value='**File was considered safe and not reported**', inline=True)
            embed.add_field(name='📅 Scan Date/Time', value=f'{s[5]}', inline=True)
            embed.set_footer(text=f"MD5- {s[0]}")
            #file = discord.File(f"{s[7]}//{s[8]}")
            try:
                view = Menu()
                await message.reply(view=view, embed=embed)
                print(f'{Fore.LIGHTBLACK_EX}{s[5]} FILE {Fore.BLUE}-{Fore.CYAN} {filename} {Fore.GREEN} "{s[7]}"{Fore.WHITE} 200{Fore.MAGENTA} 20107')
                print(f'{Fore.LIGHTBLACK_EX}{s[5]} FILE {Fore.BLUE}-{Fore.LIGHTMAGENTA_EX} Md5 "{s[0]}" Detections "{s[2]}/{s[1]}" FileSize "{s[4]}Mb" FileType "{s[3]}"')
            except:
                await message.reply(f'**Failed to analyze file**')
            # Delete Cache #
            for file in os.scandir(s[7]):
                os.remove(file.path)
            os.rmdir(s[7])
    if '$md5' in str(message.content):
        p=str(message.content).split()
        md5=str(p[1])
        s=Engine.Engine.md5Scan(md5=md5)
        # md5, total, detected, fileType, fileSize, scanDate, scanUrl, cachedir, filename
        await message.reply(f'**Scanning MD5 Hash for {message.author.mention}...**')
        embed = discord.Embed(title=f'MD5 Hash Scan', colour=discord.Colour.blue())
        embed.set_author(name=f"{md5}", url=f"{s[6]}", icon_url=f"{s[6]}")
        embed.set_thumbnail(url=f"{message.author.avatar}")
        embed.add_field(name=f'🦠 Detections', value=f"{s[2]}/{s[1]}")
        embed.add_field(name=f'📁 MD5 Length', value=f"{s[4]} Bytes")
        embed.add_field(name=f'🔒 MD5 Type', value=f"128 Bits")
        if s[2] < 10:
            embed.add_field(name='💉 Status', value='🟢 Safe / Trusted')
        elif s[2] >= 10 and s[2] < 15:
            embed.add_field(name='💉 Status', value='🟡 Low Risk / False-Positive')
        elif s[2] >= 15 and s[2] < 20:
            embed.add_field(name='💉 Status', value='🟡 Moderate Risk / Suspicous Activity')
        elif s[2] >= 20 and s[2] < 30:
            embed.add_field(name='💉 Status', value='🟠 Elevated Risk / Use At Risk ')
        elif s[2] >= 30 and s[2] < 42:
            embed.add_field(name='💉 Status', value='🔴 High Risk / Dangerous')
        else:
            embed.add_field(name='💉 Status', value='⚫ Critical Risk / DO NOT RUN')
        if s[2] > 24:
            embed.add_field(name='📢 Report', value='This file has been reported for further analysis.', inline=True)
        else:
            embed.add_field(name='📢 Report', value='**File was considered safe and not reported**', inline=True)
        embed.add_field(name='📅 Scan Date/Time', value=f'{s[5]}', inline=True)
        embed.set_footer(text=f"MD5- {s[0]}")
        #file = discord.File(f"{s[7]}//{s[8]}")
        try:
            view = Menu()
            await message.reply(view=view, embed=embed)
            print(f'{Fore.LIGHTBLACK_EX}{s[5]} MD5  {Fore.BLUE}-{Fore.CYAN} {md5}{Fore.GREEN}  "cache//{md5}.md5"{Fore.WHITE} 200{Fore.MAGENTA} 20107')
            print(f'{Fore.LIGHTBLACK_EX}{s[5]} MD5  {Fore.BLUE}-{Fore.LIGHTMAGENTA_EX} Md5 "{md5}" Detections "{s[2]}/{s[1]}" MD5 Length "{s[4]} Bytes" MD5 Type "128 Bits"')
        except:
            await message.reply(f'**Failed to analyze file**')

if __name__=="__main__":
    client.run(str(fData.dtoken))
