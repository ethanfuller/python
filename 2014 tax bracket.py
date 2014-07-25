#!/usr/bin/python2.2 -tt
# Copyright 2014 Ethan Fuller. All Rights Reserved.
import os

def main():
  os.system('clear')
  personal_exemption = 3950
  std_deduction_single = 6200
  std_deduction_married_joint = 12400
  std_deduction_married_single = 6200
  
  # Background selection 
  print 'Background:'
  print 'a.) Single'
  print 'b.) Married Filling Jointly & Surviving Spouses'
  print 'c.) Married Filling Seperate Returns'
  background_choice = raw_input('Enter number to select: ')
  
  
  # Single
  deduction_exemption_combo_single = 10150
  if background_choice == 'a':
    print '' 
    anual_salary_single = input('Anual salary: ')
    bracket_salary_single = anual_salary_single - deduction_exemption_combo_single
    print 'Bracket salary: %d' % bracket_salary_single
    
  # Married Filling Jointly & Surviving Spouses  
  #deduction_exemption_combo_married_joint = 16350
  elif background_choice == 'b':
    print ''
    anual_salary_married_joint = input('Anual salary: ')
    children_married_joint = input('# of children: ')
    exemp_children_married_joint = personal_exemption * children_married_joint
    a_married_joint = anual_salary_married_joint - exemp_children_married_joint
    bracket_salary_married_joint = a_married_joint - std_deduction_married_joint
    
    print 'Bracket salary: %d' % bracket_salary_married_joint
    
  # Married Filling Seperate Returns
  elif background_choice == 'c':
    print ''
    anual_salary_married_single = input('Anual salary: ')
    children_married_single = input('# of children: ')
    exemp_children_married_single = personal_exemption * children_married_single
    a_married_single = anual_salary_married_single - exemp_children_married_single
    edit_bracket_salary_married_single = a_married_single - std_deduction_married_single
    bracket_salary_married_single = edit_bracket_salary_married_single / 2
    print 'Bracket salary: %d' % bracket_salary_married_single
    
if __name__ == '__main__':
  main()
