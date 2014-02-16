#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ggT(a,b):
	while True:
		r = a%b
		if r == 0:
			g=b
			return g
		else:
			a,b=b,r

def kgV(a,b):
	if a < b: a,b=b,a
	if a == b: return a
	maxi = max(a,b)
	while True:
		if a % b == 0:
			return a
		a += maxi

def isprim(a):
	return True

def phi(a,b):
	if isprim(a) and isprim(b):
		mod = a*b
		return (mod,(a-1)*(b-1))



if __name__=='__main__':
	import sys
	a = b = 0
	if len(sys.argv) != 4:
		print "Usage: ./krypto --ggt a b"
	else:
		a = int(sys.argv[2])
		b = int(sys.argv[3])
		if not isinstance(a,int) or not isinstance(b,int):
			raise TypeError, "wrong type"

	if sys.argv[1] == '--ggt':
		print ggT(a,b)

	if sys.argv[1] == '--kgv':
		print kgV(a,b)

	if sys.argv[1] == '--phi':
		print phi(a,b)