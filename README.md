# MAC-ADDRESS-CHANGER-
A simple command-line utility written in Python 3 to change the MAC address of a network interface on Linux-based systems

# Python MAC Address Changer

A simple command-line utility written in Python 3 to change the MAC address of a network interface on Linux-based systems.

This script automates the process of taking a network interface down, changing its hardware (MAC) address, and bringing it back up. It also verifies that the change was successful.

## Disclaimer

This tool is intended for educational purposes, such as learning about network administration and cybersecurity in a controlled lab environment. Changing your MAC address can be used for legitimate privacy reasons on public networks, but it can also violate the terms of service of some networks. Use this script responsibly and only on networks you are authorized to use.

## Requirements

* **Operating System:** Linux (the script depends on the `ifconfig` command)
* **Python:** Python 3
* **Permissions:** Root/sudo privileges are required to change network settings.

## How to Use

1.  **Clone the repository (or download the script):**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Find your network interface:**
    Run `ifconfig` or `ip addr` to find the name of the interface you want to change (e.g., `eth0`, `wlan0`, `enp3s0`).

    ```bash
    $ ifconfig
    enp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.1.10  netmask 255.255.255.0  broadcast 192.168.1.255
            inet6 fe80::...  prefixlen 64  scopeid 0x20<link>
            ether 54:e1:ad:1d:69:79  txqueuelen 1000  (Ethernet)
            ...
    ```

3.  **Run the script:**
    You must run the script with `sudo` privileges. Use the `-i` or `--interface` flag to specify the interface and the `-m` or `--mac` flag to specify the new MAC address.

    **Syntax:**
    ```bash
    sudo python3 mac.py --interface <interface_name> --mac <new_mac_address>
    ```

    **Example:**
    ```bash
    sudo python3 mac.py -i enp3s0 -m 54:e1:ad:1d:69:80
    ```

## Example Output
