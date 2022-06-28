import requests

domain = input("Enter Domain :")
file = open('sub.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = (f"http://{subdomain}.{domain}")

    try:
        requests.get(url1)
        print(f"Discovered URL : {url1}")
        
        
    except requests.ConnectionError:
        pass



