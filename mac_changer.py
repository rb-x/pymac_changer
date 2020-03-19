import subprocess
import optparse
from sys import argv


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["interface", interface, "up"])
    print("[+] Done")


def parse_args():
    parser = optparse.OptionParser(
        f"Usage : {argv[0]} -i <interface> -m <mac_address>")
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (options, args) = parser.parse_args()
    if not options.interface or not options.new_mac:
        print(parser.usage)
        exit(1)
    return options


def main():
    options = parse_args()
    change_mac(options.interface, options.new_mac)
    print(f"[+] Changing MAC for {interface} to  {new_mac}")


if __name__ == "__main__":
    main()
