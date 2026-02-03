from colorama import Fore, init
import json
import pyfiglet

init(autoreset=True)

def print_header(target, os_info, threads):
    ascii_banner = pyfiglet.figlet_format("ScannerLogic v1")
    print(Fore.CYAN + ascii_banner)
    
    print(f"{Fore.WHITE}" + "*" * 80) 
    print(f"{Fore.WHITE}ip address    : {Fore.WHITE}{target}")
    print(f"{Fore.WHITE}os detection  : {Fore.MAGENTA}{os_info}")
    print(f"{Fore.WHITE}threads value : {Fore.WHITE}{threads}")
    print(f"{Fore.WHITE}" + "*" * 80)
    print(f"{Fore.RED}{'PORT':<9} {'STATUS':<9} {'SERVICE':<12} {'BANNER'}")

def print_footer(duration_str):
    print(f"{Fore.WHITE}" + "*" * 80)
    print(f"{Fore.CYAN}Scan time: {Fore.CYAN}{duration_str}")
    print(f"{Fore.WHITE}" + "*" * 80)

def save_report(filename, results, target, os_info, duration_str):
    if not filename:
        return
    
    if not filename.endswith('.txt'):
        filename += ".txt"
        
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("*" * 80 + "\n")
            f.write(f"ip address    : {target}\n")
            f.write(f"os detection  : {os_info}\n")
            f.write("*" * 80 + "\n")
            f.write(f"{'PORT':<9} {'STATUS':<9} {'SERVICE':<12} {'BANNER'}\n")
            f.write("-" * 80 + "\n")
            
            for res in sorted(results, key=lambda x: x['port']):
                f.write(f"{res['port']:<5}/tcp  {'open':<9} {res['service']:<12} {res['banner']}\n")
            
            f.write("*" * 80 + "\n")
            f.write(f"Scan time: {duration_str}\n")
            f.write("*" * 80 + "\n")
            
        print(f"{Fore.YELLOW}[!] Report saved to: {Fore.YELLOW}{filename}")
        
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")