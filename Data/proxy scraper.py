import requests
from colorama import Fore, init


init()

print(Fore.GREEN + "Getting proxies..")
out_file = "proxies.txt"
f = open(out_file,'wb')
r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
r2 = requests.get("https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt")
f.write(r1.content)
f.write(r2.content)
f.close()
print("Got proxies, you can close this now")
input()