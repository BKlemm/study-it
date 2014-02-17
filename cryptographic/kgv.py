#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kgV(a,b):
	if a == 0 or b == 0:
		sys.exit(-1)
	aba = abs(a)
	abb = abs(b)
	if aba == abb:
		return a
	else:
		mina = min(a)
		minb = min(b)
		maxa = max(a)
		maxb = max(b)

		kgV(maxa,maxb)

def ggT(a,b):
	while True:
		r = a%b
		if r == 0:
			g=b
			return g
		else:
			a,b=b,r

def erwEuklid(a,b):
	if b == 0:
		return (a,1,0)
	else:
		d,x,y = erwEuklid(b,a%b)
		return (d,y,x-(a/b)*y)

def mod_expo(a,b,n):
	from math import pow
	return pow(a,b) % n

def crt(k,m,n):
	res = mu = mo = i = 0
	for i in range(n):
		res = (res + k[i]*mu[i]) % mo
	return res

def coset(s):
	import random
	l=[]
	for i in s:
		l.append(chr(ord(i) ^ random.randint(0,10)))
	return ''.join(l)

def selfinv_chiffre(s,k):
	s=list(s)
	k=list(k)
	lg = len(k)
	l=[];j=0
	for i in s:
		c = ord(i) - ord(' ')
		key = ord(k[j%lg]) - ord(' ')
		c ^= key
		l.append(chr(c+ord(' ')))
		j += 1
	return ''.join(l)

def onetimepad(s,k):
	bs = binary(s)
	ks = binary(k)
	l.append(z ^= r)
	return 

def binary(s):
	l=[]
	for i in s:
		l.append(bin(ord(i))[2:])

	return ''.join(l)


print onetimepad("hallo","asasa")