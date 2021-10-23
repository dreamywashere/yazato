import colorama, time, os
from colorama import Fore, Style, init
import secrets
import random
import threading
from threading import Thread
from httpx import Client
from httpx_socks import SyncProxyTransport
from hfuck import Bypass
import requests

os.system("cls")
genned = 0
bypassed = 0
color = f"{Fore.CYAN}{Style.BRIGHT}"
### ASCII ###
os.system("title Yazato Token Generator - Main Menu")
print(f"""
                                       \u001b[38;5;45m╦ ╦┌─┐┌─┐┌─┐┌┬┐┌─┐
                                       \u001b[38;5;51m╚╦╝├─┤┌─┘├─┤ │ │ │
                                       \u001b[38;5;87m ╩ ┴ ┴└─┘┴ ┴ ┴ └─┘{Fore.RESET}
""")
### INPUTS ###
proxytype = input(f"{color}>{Fore.RESET} ProxyType [http/https/socks4/socks5]{color}:{Fore.RESET} ")
username = input(f"{color}>{Fore.RESET} Username{color}:{Fore.RESET} ")
invite = input(f"{color}>{Fore.RESET} Invite{color}:{Fore.RESET} ")
maxThreads = input(f'{color}>{Fore.RESET} How many accounts?{color}:{Fore.RESET} ')
savefile = input(f'{color}>{Fore.RESET} Save tokens to tokens.txt [True/False]{color}:{Fore.RESET} ')

print()
print()

def title():
    global genned, bypassed
    while True:
        os.system(
            f"title Yazato Generator - Generated: {genned} ^| Solved Captchas: {bypassed} ^| Invite: {invite} ^| Name: {username} ^| yazato.xyz")
thread = threading.Thread(target=title, args=(), daemon=True)
thread.start()

### SEX HAPPENS KIDS ###
class Generator:

    def __init__(self):
        self.tokens = open("Data/tokens.txt", "a")
        self.proxies = open("Data/proxies.txt").read().splitlines()
        self.color = f"{Fore.CYAN}{Style.BRIGHT}"
        self.headers = {
            "Host": "discord.com", "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Fingerprint": "", "Accept-Language": "en-US", "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
            "Content-Type": "application/json", "Authorization": "undefined",
            "Accept": "*/*", "Origin": "https://discord.com",
            "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty", "Referer": "https://discord.com/register",
            "X-Debug-Options": "bugReporterEnabled",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": "OptanonConsent=version=6.17.0; locale=th"
        }

    def getProxy(self):
        return random.choice(self.proxies)

    def gen(self):
        global genned, bypassed, savetokens
        bypassCaptcha = Bypass()
        bypassed += 1
        while True:
            try:
                with Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{self.getProxy()}')) as request:
                    r = request.post("https://discord.com/api/v9/auth/register",
                                     headers={"Host": "discord.com", "Connection": "keep-alive",
                                              "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                                              "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                                              "X-Fingerprint": "", "Accept-Language": "en-US", "sec-ch-ua-mobile": "?0",
                                              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
                                              "Content-Type": "application/json", "Authorization": "undefined",
                                              "Accept": "*/*", "Origin": "https://discord.com",
                                              "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors",
                                              "Sec-Fetch-Dest": "empty", "Referer": "https://discord.com/register",
                                              "X-Debug-Options": "bugReporterEnabled",
                                              "Accept-Encoding": "gzip, deflate, br",
                                              "Cookie": "OptanonConsent=version=6.17.0; locale=th"},
                                     json={"fingerprint": "", "username": f'{secrets.token_urlsafe(4)} | {username}',
                                           "email": secrets.token_hex(6) + '@gmail.com', "password": "discordbest1$A",
                                           "invite": invite, "consent": True, "gift_code_sku_id": "",
                                           "captcha_key": bypassCaptcha}).json()
                if savefile == True:
                    self.tokens.write(f'{r["token"]}\n')
                    self.tokens.flush()
                else: pass
                genned += 1
                toe = r["token"]
                re = requests.get(f'https://discord.com/api/v9//users/@me',
                                  headers={"Content-Type": "application/json", "authorization": toe,
                                           "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"})
                usernamee = re.json()['username'] + '#' + re.json()['discriminator']
                return r['token'], usernamee
            except Exception as e:
                try:
                    self.proxies.remove(self.getProxy)
                except:
                    pass
                pass

    def start(self):
        print(
            f"{color}>{Fore.RESET} Created{color}:{Fore.RESET} {self.gen()}".replace("(", "").replace("'", "").replace(
                ")", "").replace(",", f"{color} >{Fore.RESET}"))

    def Client(self):
        for i in range(int(maxThreads)):
            try:
                threading.Thread(target=self.start).start()
            except Exception as e:
                print(e)
                pass

### CUM MOMENT ###
if __name__ == "__main__":
    Generator().Client()