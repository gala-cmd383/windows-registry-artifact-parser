from Registry import Registry
import sys
import json

def parse_registry_hive(hive_path):
    try:
        print(f"[*] Loading Registry Hive: {hive_path} ...")
        reg = Registry.Registry(hive_path)
        print("[+] Hive loaded successfully!\n")
        
     
        root = reg.root()
        print(f"[*] Root Key Name: {root.name()}")

        print("\n[+] Scanning subkeys...")
        for subkey in root.subkeys()[:10]: 
            print(f"    - Subkey: {subkey.name()} (Last Modified: {subkey.timestamp()})")
            
    except Exception as e:
        print(f"[-] Error parsing registry hive: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[-] Usage: python src/parser.py <path_to_registry_hive_file>")
        sys.exit(1)
    
    hive_file = sys.argv[1]
    parse_registry_hive(hive_file)