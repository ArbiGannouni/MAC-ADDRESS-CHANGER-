import subprocess
import optparse
import re

def get_arguments():
    """Parses command-line arguments for interface and new MAC address."""
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="network_interface", help="This is for network interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="This place is for MAC Address")
    (options, arguments) = parser.parse_args()

    if not options.network_interface:
        parser.error("[-] Specify Network Interface, type -h for help")
    
    if not options.new_mac:
        parser.error("[-] Specify MAC Address, type -h for help")
        
    return options

def mac_changer(network_interface, new_mac):
    """Changes the MAC address for a given network interface."""
    print(f"[+] Changing MAC Address for {network_interface} to {new_mac}")
    
    # These are the system commands that will change the mac address
    # Note: Used function arguments 'network_interface' and 'new_mac' instead of 'options.network_interface'
    subprocess.call(f"ifconfig {network_interface} down", shell=True)
    subprocess.call(f"ifconfig {network_interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {network_interface} up", shell=True)

def get_mac(network_interface):
    """Filters and returns the current MAC address of the interface."""
    # Note: Used function argument 'network_interface' instead of 'options.network_interface'
    try:
        ifconfig_result = subprocess.check_output(f"ifconfig {network_interface}", shell=True).decode("utf-8")
        
        # Search for the MAC address pattern
        mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
        
        if mac_address_search_result:
            # Note: Used .group(0) to correctly extract the matched string
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read MAC address.")
            return None
    except subprocess.CalledProcessError:
        print(f"[-] Error: Could not execute ifconfig on interface {network_interface}.")
        return None

# --- Main execution ---

options = get_arguments()

print("[+] Getting current MAC address...")
current_mac = get_mac(options.network_interface)
if current_mac:
    print(f"[+] Current MAC = {current_mac}")

mac_changer(options.network_interface, options.new_mac)

# Verify the change
new_mac_address = get_mac(options.network_interface)

if new_mac_address == options.new_mac:
    print(f"[+] MAC address has changed successfully to {new_mac_address}")
else:
    print("[-] Something went wrong. MAC address was not changed.")
