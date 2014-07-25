#!/usr/bin/python2.2 -tt
# Copyright 2014 Ethan Fuller. All Rights Reserved.
import os

def main():
    os.system('clear')
    print 'GPA calculator by Ethan Fuller'
    print 'Begin by entering your quarter grades. Only numbers.'
    
# Course inputs
    course_one = input('Course one: ')
    course_two = input('Course two: ')
    course_three = input('Course three: ')
    course_four = input('Course four: ')
    course_five = input('Course five: ')
    course_six = input('Course six: ')
    
# Average grade calculation
    course_sum = course_one + course_two + course_three + course_four + course_five + course_six
    course_average = course_sum / 6
    
# GPA grading system and results
    if course_average >= 93 and course_average <= 100:
        print 'Average grade: %d GPA: 4.00' % course_average
    elif course_average >= 90 and course_average <= 92:
        print 'Average grade: %d GPA: 3.67' % course_average
    elif course_average >= 87 and course_average <= 89:
        print 'Average grade: %d GPA: 3.33' % course_average
    elif course_average >= 83 and course_average <= 86:
        print 'Average grade: %d GPA: 3.00' % course_average
    elif course_average >= 80 and course_average <= 82:
        print 'Average grade: %d GPA: 2.67' % course_average
    elif course_average >= 77 and course_average <= 79:
        print 'Average grade: %d GPA: 2.33' % course_average
    elif course_average >= 73 and course_average <= 76:
        print 'Average grade: %d GPA: 2.00' % course_average
    elif course_average >= 70 and course_average <= 72:
        print 'Average grade: %d GPA: 1.67' % course_average
    elif course_average >= 65 and course_average <= 69:
        print 'Average grade: %d GPA: 1.33' % course_average
    elif course_average >= 60 and course_average <= 64:
        print 'Average grade: %d GPA: 1.00' % course_average
    else:
        print 'Average grade: %d GPA: 0.00' % course_average

if __name__ == '__main__':
    main()
