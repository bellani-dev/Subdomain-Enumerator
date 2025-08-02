import requests
import threading

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        print(f"[+] Found: {url} ({response.status_code})")
    except requests.ConnectionError:
        pass

def main():
    domain = input("Enter target domain (e.g., example.com): ")
    wordlist = input("Enter path to wordlist: ")

    with open(wordlist, 'r') as file:
        subdomains = file.read().splitlines()

    threads = []
    for subdomain in subdomains:
        t = threading.Thread(target=check_subdomain, args=(domain, subdomain))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
