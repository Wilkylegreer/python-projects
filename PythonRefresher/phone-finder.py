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


def check_extra_entry(ip, mac, devices_list):
    for device_ip, device_mac in devices_list:
        if device_ip == ip and device_mac == mac:
            return True
    return False


if __name__ == "__main__":
    network_range = "172.20.1.0/24"
    devices = get_connected_devices(network_range)

    list2_extra_ip = "172.20.1.151"
    list2_extra_mac = "6E:9C:08:B9:60:EE"

    if check_extra_entry(list2_extra_ip, list2_extra_mac, devices):
        print(
            f"Extra entry from List 2 found - IP: {list2_extra_ip}, MAC: {list2_extra_mac}")
    else:
        print("Extra entry from List 2 not found in the scanned devices.")
