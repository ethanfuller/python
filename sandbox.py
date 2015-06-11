#!/usr/bin/python2.2 -tt
# Copyright 2014 Ethan Fuller. All Rights Reserved.
import os

def main():
    os.system('clear')
    print ''

# Propose the question    
print 'What is the sqaure-root of 36?'
answer = raw_input('Answer: ')

# Determine if they're correct
if answer == '6':
    print 'Correct!'
    reset = raw_input('')
else:
    print 'Wrong'
    reset = raw_input('')

if __name__ == '__main__':
    main()
