import ipaddress

def convert_ipv6_to_ipv4(ipv6_address):
    try:
        ip6_obj =ipaddress.IPv6Address(ipv6_address)
    except ipaddress.AddressValueError:
        print("Invalid IPv6 address.")
        return None
    
    # converts IPv4 addresses to IPv6 using the `::ffff:` prefix and IPv6 addresses to IPv4 using the `ipv4_mapped` attribute.

    if ip6_obj.ipv4_mapped:
        ipv4_address = ip6_obj.ipv4_mapped.exploded
        return ipv4_address
    else:
        print("The provided IPv6 Address is not IPv4-mapped")

def convert_ipv4_to_ipv6(ipv4_address):
    # Check if the provided IPv4 address is valid
    try:
        ipaddress.IPv4Address(ipv4_address)
    except ipaddress.AddressValueError:
        print("Invalid IPv4 address.")
        return None

    # Convert IPv4 address to IPv6 using the ::ffff: prefix
    ipv6_address = ipaddress.IPv6Address(f"::ffff:{ipv4_address}").compressed

    return ipv6_address

def main():
    # Get input IPv4 address from the user
    print("Choose IP convertion \n\n1: IPv4 to IPv6 \n2: IPv6 to IPv4")

    

    choice = input("\nEnter Your Choice (1 or 2): ")

    if choice == "1":
        ipv4_address = input("\nEnter an IPv4 Address: ")
        ipv6_address = convert_ipv4_to_ipv6(ipv4_address)

        if ipv6_address:
            print(f"\nIPv4 Address: {ipv4_address}")
            print(f"\nIPv6 Address: {ipv6_address}")
    
    elif choice == "2":
        ipv6_address = input("\nEnter the IPv6 address:")
        ipv4_address = convert_ipv6_to_ipv4(ipv6_address)

        if ipv4_address:
            print(f"IPv6 Address : {ipv6_address}")
            print(f"Ipv4 Address : {ipv4_address}")
    else:
        print("Invalid Choice")
if __name__ == "__main__":
    main()