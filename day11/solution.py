from typing import List

def hex_distance(ns_offset: int, nesw_offset: int, nwse_offset: int) -> int:
    return abs(ns_offset) + abs(nesw_offset) + abs(nwse_offset) - min(
        abs(ns_offset), abs(nesw_offset), abs(nwse_offset)
    )

def hex_grid(steps: List[str]) -> int:
    ns_offset = 0
    nesw_offset = 0
    nwse_offset = 0
    for step in steps:
        if step == 'n':
            ns_offset += 1
        elif step == 'ne':
            nesw_offset += 1
        elif step == 'se':
            nwse_offset -= 1
        elif step == 's':
            ns_offset -= 1
        elif step == 'sw':
            nesw_offset -= 1
        elif step == 'nw':
            nwse_offset += 1
        else:
            raise ValueError(step)
    return hex_distance(ns_offset, nesw_offset, nwse_offset)

def hex_grid2(steps: List[str]) -> int:
    ns_offset = 0
    nesw_offset = 0
    nwse_offset = 0
    furthest = 0
    for step in steps:
        if step == 'n':
            ns_offset += 1
        elif step == 'ne':
            nesw_offset += 1
        elif step == 'se':
            nwse_offset -= 1
        elif step == 's':
            ns_offset -= 1
        elif step == 'sw':
            nesw_offset -= 1
        elif step == 'nw':
            nwse_offset += 1
        else:
            raise ValueError(step)
        furthest = max(
            furthest, hex_distance(ns_offset, nesw_offset, nwse_offset)
        )
    return furthest
