import requests
from concurrent.futures import ThreadPoolExecutor

def dns_lookup(domain):
    try:
        api_url = f"https://api.api-ninjas.com/v1/dnslookup?domain={domain}"
        headers = {'X-Api-Key': 'APIKEY_KAU_LER'}  # Ganti 'APIKEY_KAU_LER', Regist dulu di https://api-ninjas.com
        response = requests.get(api_url, headers=headers)

        if response.status_code == requests.codes.ok:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code} {response.text}")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def is_domain_dakaktif(domain):
    try:
        dns_data = dns_lookup(domain)
        if dns_data and isinstance(dns_data, list) and len(dns_data) > 0:
            for record in dns_data:
                if record.get("record_type") == "A":
                    return False
            return True
        else:
            return True
    except Exception as e:
        print("Error:", e)
        return True 

def main(domain):
    text = '\033[33;1m#\033[0m ' + domain
    try:
        if is_domain_dakaktif(domain):
            text += ' ======>\033[31;1mDNS Poblem\033[1m'
            with open('TO!.txt', 'a') as file:
                file.write(domain + '\n')
        else:
            text += ' ======> \033[34;1mDNS Normal\033[0m'
    except Exception as e:
        print("Error:", e)
        text += ' => \033[32;1mError\033[0m'
        with open('list_domain_error.txt', 'a') as error_file:
            error_file.write(domain + '\n')
    print(text)

if __name__ == '__main__':
    print("""
\033[35;1m
 ██╗    ██╗███████╗██╗    ██╗
 ██║    ██║██╔════╝██║    ██║
 ██║ █╗ ██║█████╗  ██║ █╗ ██║ 
 ██║███╗██║██╔══╝  ██║███╗██║
\╚███╔███╔╝███████╗╚███╔███╔╝
  ╚══╝╚══╝ ╚══════╝ ╚══╝╚══╝ 
  ░ ▓░▒ ▒  ░░ ▒░ ░░ ▓░▒ ▒  
    ▒ ░ ░   ░ ░  ░  ▒ ░ ░  
    ░   ░     ░     ░   ░  
      ░       ░  ░    ░  
𝔍𝔲𝔰𝔱 𝔇𝔑𝔖 𝔖𝔠𝔞𝔫𝔫𝔢𝔯 - 𝔉𝔬𝔯 𝔗𝔞𝔨𝔢 𝔒𝔳𝔢𝔯 𝔇𝔬𝔪𝔞𝔦𝔫 ! \033[0m""")
    
    try:
        filename = input("\033[36;1mEnter the filename containing domains ( ex : list.txt): \033[0m")
        num_threads = int(input("\033[36;1mEnter the number of threads (1-50): \033[0m"))
    except KeyboardInterrupt:
        print("Scan aborted by user.")
        exit()
    
    try:
        with open(filename, 'r') as file:
            domains = [line.strip() for line in file if line.strip()]
    except:
        print("Error reading the file.")
        exit()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(main, domains)
