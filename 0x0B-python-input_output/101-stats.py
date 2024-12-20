#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""

import sys

total_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0


def print_stats():
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) > 2:
            size = int(parts[-1])
            status = parts[-2]
            total_size += size
            if status in status_codes:
                status_codes[status] += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
