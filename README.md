
# EngineWatch - Discord File Scanner
EngineWatch source is a bot for discord that scans files sent by users in your server, It will
Download and scan the files through (VirusTotal) with over 73 Anti-Virus Engines, Aswell
as including Md5 Scanning and Hash Scanning.

# File Scanning
**For File Scans and Uploads It will scan each message for attatchments and if detected will download the
attatched file to a cache folder, Next it will get the Md5 Hash of the downloaded file and scan it using the VirusTotal Engine API.
Next will it return the information needed through a JSON format which will be returned to the user.**

![alt text](https://github.com/i64-sudo/EngineWatch/blob/main/media/sc1.png?raw=true)

# MD5 Scanning ($md5 HASH)
**MD5 Scanning works the same as File Scanning in terms of the file scanning but skips the download and upload part,
If the user knows the Md5 Hash of the file they are trying to scan they can use command ( $md5 HASH ) replacing HASH with the MD5
Hash you are trying to scan, Which will go through the same process as the File Scan and return the information needed in a JSON Format which will
be returned to the user.**

![alt text](https://github.com/i64-sudo/EngineWatch/blob/main/media/sc2.png?raw=true)

# Console Logs
**Console Logs don't really matter all to much but give a LOG for all files detected, scanned, uploaded and more.**
![alt text](https://github.com/i64-sudo/EngineWatch/blob/main/media/sc3.png?raw=true)


# Setup
**install required libraries**
```bash
pip install -r requirements.txt
```
**Edit bot.py with your token & api key for virus total**
```py
class fData:
    dtoken="DISCORD-BOT-TOKEN"
    virusTotal_APIKey="VIRUS-TOTAL-API-KEY"
```
* **To get a API Key for Virus Total go to the website https://www.virustotal.com/ And create a account and login, Next under your profile options you will see a option for API Key or Your API Key, There you shall find your personal API Key, This will give you access to Malware Scanning and so on.**

# Notes | bot.py
This will soon be replaced with Commands once Interactions are added.
```python
exceptions = [
    'png', 'jpg', 'jpeg', 'gif',  # Images
    'bmp', 'tiff', 'webp', 'svg', 'ico',
    'mp4', 'avi', 'mov', 'wmv', 'mkv',  # Videos
    'flv', 'webm', 'm4v', '3gp', 'mpeg',
    'mp3', 'wav', 'flac', 'aac', 'wma',  # Songs
    'ogg', 'm4a', 'alac', 'opus', 'mid'
    # Add more formats as needed
]
```

# Change-Log
> Version 2.0
> * **Updated Name from SpyWatcher to EngineWatch (New REPO)**
> * **Fixed Time-To-Upload and Uploading/Downloading Errors***
> * **Added better FileType Exceptions**
> * **Fixed Interaction Buttons**
> * **Added (💉 Status) Field to Embed [Based On Detection Status]**
> * **Added (📢 Report) Field to Embed [Functions Have To Be Added]**
> * **Added (📅 Scan Date/Time) Field to Embed**
> * **Optimized Code and Lowered amount of used Libraries**
>
> Version 1.4.1
> * **Fixed P.u.t call to VirusTotal Engine**
> * **Switched from Private to Public on Github page**
>
> Version 1.3
> * **Updated Menu Class for discord.ui.View (FIX)**
> * **Added Exception List to file uploads**
>
> Version 1.2
> * **Added Manual MD5 Hash Scanning ($md5 HASH)**
>
> Version 1.1
> * **Added Form Style Buttons to Embed Message**
>
> Version 1.0
> * **Added File Detection and Downloading of Files**
> * **Added VirusTotal API for Engine Scanning**
>
