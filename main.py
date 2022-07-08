# Created by simonboiii\vivid\landen
# Fixed + Extra code by $ twies

import requests
import os
from colorama import Fore
from colorama import init


session = requests.Session()
session.trust_env = False
            
def main():
    file = open('tokens.txt', 'r')
    lines = list(dict.fromkeys(file.readlines()))
    print("Found ", len(lines), " tokens")
    print()
    for token in lines:
        token = token.strip()
        headers = {
        "Authorization": token,
        "accept": "*/*",
        "accept-language": "en-US",
        "connection": "keep-alive",
        "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "DNT": "1",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "referer": "https://discord.com/channels/@me",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
        r=session.get('https://discord.com/api/v9/users/@me', headers=headers)
        if r.status_code == 200:
            print(f"{Fore.GREEN}  Valid {Fore.CYAN}| {Fore.RESET}{token}")
            fileValid = open('valid.txt', 'w')
            fileValid.write(f'{token}\n')
        elif r.status_code == 429:
            print(f"{Fore.YELLOW}  Rate Limited {Fore.YELLOW}[{Fore.RESET}429{Fore.YELLOW}] {Fore.CYAN}| {Fore.RESET}{token}")
        else:
            print(f"{Fore.RED}  Invalid {Fore.CYAN}| {Fore.RESET}{token}")


main()
