# ...existing code...
import sys

def caesar_encrypt(text, shift):
    s = shift % 26
    res_chars = []
    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            res_chars.append(chr(base + (ord(ch) - base + s) % 26))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            res_chars.append(chr(base + (ord(ch) - base + s) % 26))
        else:
            res_chars.append(ch)
    return ''.join(res_chars)
text = sys.stdin.readline().rstrip('\n')
shift_line = sys.stdin.readline().strip()
shift = int(shift_line) if shift_line != "" else 0

print(caesar_encrypt(text, shift))