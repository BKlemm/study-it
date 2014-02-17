#!/usr/bin/env python
import string

def vchiffre_enc(s,k):
	plains = []
	for i in s:
		if i in string.ascii_letters:
			plains.append((ord(i)+k)%52)
		else:
			plains.append(ord(i))
	return ord_to_text(plains)

def vchiffre_dec(s,k):
	plains = []
	for i in s:
		if i in string.ascii_letters:
			plains.append((ord(i)-k)%52)
		else:
			plains.append(ord(i))
	return ord_to_text(plains)

def ord_to_text(seq):
	return ''.join([chr(i) for i in seq])

enc = vchiffre_enc("ab cd,e('l')",5)
print enc

print vchiffre_dec(enc,5)
