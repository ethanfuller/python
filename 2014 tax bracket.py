#!/usr/bin/python2.2 -tt
# Copyright 2014 Point_Four. All Rights Reserved.
import os

def main():
    os.system('clear')
    print ''

# Chart variables
    personal_exemption = 3950
    std_deduction_single = 6200
    std_deduction_marriedj = 12400
    std_deduction_marrieds = 6200

# Start/Filing status
    print 'Filing status'
    print 'a.) Single'
    print 'b.) Married filing jointly & surviving spouses'
    print 'c.) Married filing seperate returns'
    print '* Select by letter'
    status_select = raw_input('>> ')


# Single (Background selection)
    if status_select == 'a':
        print 'Filing status: Single'
        salary = input('Anual salary: ')
        dependents = input('Number of dependents (including you): ')

        personal_exemption_dependents = personal_exemption * dependents
        algorithm = salary - personal_exemption_dependents - std_deduction_single
        print 'Bracket salary: %d' % algorithm

# Married filing jointly & surviving spouses
    elif status_select == 'b':
        print 'Filing status: Married filing jointly & surviving spouses'
        salary = input('Anual salary: ')
        dependents = input('Number of dependents (including you): ')

        personal_exemption_dependents = personal_exemption * dependents
        algorithm = salary - personal_exemption_dependents - std_deduction_marriedj
        print 'Bracket salary: %d' % algorithm

# Married filing seperate returns
    elif status_select == 'c':
        print 'Filing status: Married filing seperate returns'
        salary = input('Anual salary: ')
        dependents = input('Number of dependents (including you): ')

        personal_exemption_dependents = personal_exemption * dependents
        part_algorithm = salary - personal_exemption_dependents - std_deduction_marrieds
        algorithm = part_algorithm / 2
        print 'Bracket salary: %d' % algorithm


if __name__ == '__main__':
    main()
