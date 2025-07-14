#!/usr/bin/env python3
import sys

# substitution map derived from your example (cipherletter -> plainletter)
_mapping = {
    'a': 'h', 'b': 'd', 'c': 'b', 'd': 'e', 'e': 'f', 'f': 'o',
    'g': 'l', 'h': 'a', 'i': 'j', 'j': 'p', 'k': 'k', 'l': 'u',
    'm': 'g', 'n': 'm', 'o': 'r', 'p': 'x', 'q': 's', 'r': 'v',
    's': 'w', 't': 't', 'u': 'i', 'v': 'z', 'w': 'c', 'x': 'n',
    'y': 'y', 'z': 'q'
}

def decode(text):
    result_chars = []
    for ch in text:
        if ch.isalpha():
            lower = ch.lower()
            if lower in _mapping:
                dec = _mapping[lower]
                # preserve case
                result_chars.append(dec.upper() if ch.isupper() else dec)
            else:
                result_chars.append(ch)
        else:
            result_chars.append(ch)
    return ''.join(result_chars)

def main():
    data = sys.stdin.read()
    sys.stdout.write(decode(data))

if __name__ == "__main__":
    main()
