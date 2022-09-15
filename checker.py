import requests

with open('nitros.txt', 'r') as nitrofile:
    nitros = nitrofile.read().split("\n")
nitrofile.close()

with open('proxies.txt', 'r') as proxiefile:
    proxies = proxiefile.read().split("\n")
proxiefile.close()

for i in range(len(nitros)):
    nitro = nitros[i]
    proxy = proxies[i]
    ProxyParam = {'http://': proxy, 'https://': proxy}
    url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}", proxies=ProxyParam, timeout=5)
    if url.status_code == 200:
        with open('nitrovalidcodes.txt', 'w') as nitrovalidfile:
            nitrovalidfile.write(nitro)
        nitrovalidfile.close()
        print(f"Valid code : {nitro}")
    else:
        print('Nitro not valid')