import nmap


def get_connected_devices(network_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-sn')

    connected_devices = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            device_ip = nm[host]['addresses']['ipv4']
            device_mac = nm[host]['addresses']['mac']
            connected_devices.append((device_ip, device_mac))

    return connected_devices


if __name__ == "__main__":
    network_range = "172.20.1.0/24"  # Change this to your network range
    devices = get_connected_devices(network_range)

    if devices:
        print("Connected devices:")
        for idx, (ip, mac) in enumerate(devices, start=1):
            print(f"{idx}. IP: {ip}, MAC: {mac}")
    else:
        print("No devices found.")
