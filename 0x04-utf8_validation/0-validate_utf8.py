#!/usr/bin/python3
"""valid UTF8"""


def validUTF8(data):
    """method to validate UTF8"""
    nbytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for a in data:
        z = 1 << 7
        if nbytes == 0:
            while z & a:
                nbytes += 1
                z = z >> 1
                if nbytes == 0:
                    continue
                if nbytes == 1 or nbytes > 4:
                    return False
                else:
                    if not (a & byte1 and not (a & byte2)):
                        return False
                    nbytes -= 1
            return nbytes == 0
