import random

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:

    nitrocode = ''

    for i in range(16):
        nitrocode = f"{nitrocode}{random.choice(caracteres)}" 

    print(f"{nitrocode}")

    with open("nitros.txt", "a+") as nitroFile:

        nitroFile.write(f"{nitrocode}\n")

        nitroFile.close()

        ###MADE BY AXELFROMFRANCE####

        # FREE PROXIES IN PROXIES.TXT, IF YOU WANT FREE PROXIES TO CHANGE THEM JUST GO ON https://proxyscrape.com/free-proxy-list AND CLICK ON DOWNLOAD