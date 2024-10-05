import requests
import os
import sys

file_name = 'discord.deb'

print('Downloading Discord...')
file = requests.get("https://discord.com/api/download?platform=linux&format=deb", allow_redirects=True)
with open(file_name, "wb") as discord:
    discord.write(file.content)
    discord.close()
print('Discord Downloaded!')

if os.getuid() != 0:
    print('The command dpkg cannot be used.\nAre you Root?')
    sys.exit()
print('Installing Discord...')
os.system(f'sudo dpkg -i {file_name}')
print('Discord Installed.')
