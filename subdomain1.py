import requests

domain = input("Enter Domain :")
file = open('sub.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url2 = (f"https://{subdomain}.{domain}")

    try:
        requests.get(url2)
        print(f"Discovered URL : {url2}")
        
    except requests.ConnectionError:
        pass




