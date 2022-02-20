#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:18:43 2021

@author: sofiacalatrava
"""

def comp():
	a = open("output.txt", "r")
	b = open("sudokus_finish.txt", "r")
	line1 = a.readline()
	line2 = b.readline()
	while line1 and line2:
		if (line1 != line2):
			return False
		line1 = a.readline()
		line2 = b.readline()
	a.close()
	b.close()
	return True

def main():
    
    print(comp())

if __name__ == '__main__':
    main()
