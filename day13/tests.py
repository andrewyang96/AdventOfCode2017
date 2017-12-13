from solution import get_packet_scan_severity
from solution import get_packet_scan_delay

with open('input.txt', 'r') as f:
    firewall = {}
    for line in f:
        idx, height = line.strip().split(': ')
        firewall[int(idx)] = int(height)

assert get_packet_scan_severity({0:3,1:2,4:4,6:4}) == 24
print(get_packet_scan_severity(firewall))

assert get_packet_scan_delay({0:3,1:2,4:4,6:4}) == 10
print(get_packet_scan_delay(firewall))
