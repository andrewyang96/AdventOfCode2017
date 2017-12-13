from typing import Dict

def get_packet_scan_severity(firewall: Dict[int, int]) -> int:
    severity = 0
    curr_pos = {idx: 0 for idx in firewall}
    dirs = {idx: 1 for idx in firewall}
    for idx in range(max(firewall.keys())+1):
        if curr_pos.get(idx) == 0:
            severity += idx * firewall[idx]
        for i, pos in curr_pos.items():
            if firewall[i] > 1:
                if pos == firewall[i] - 1:
                    dirs[i] = -1
                elif pos == 0:
                    dirs[i] = 1
                curr_pos[i] += dirs[i]

    return severity

def get_packet_scan_delay(firewall: Dict[int, int], debug_interval=1000) -> int:
    curr_pos = {idx: 0 for idx in firewall}
    dirs = {idx: 1 for idx in firewall}
    delays = [None for _ in range(max(firewall.keys())+1)]
    count = 0
    while True:
        delays = [count] + delays[:-1]
        for i, pos in curr_pos.items():
            if pos == 0:
                delays[i] = None
        if delays[-1] is not None:
            return delays[-1]
        for i, pos in curr_pos.items():
            if firewall[i] > 1:
                if pos == firewall[i] - 1:
                    dirs[i] = -1
                elif pos == 0:
                    dirs[i] = 1
                curr_pos[i] += dirs[i]
        if count % debug_interval == 0:
            print(count)
        count += 1
