# -*- coding: utf-8 -*-


greeting = raw_input ("Welcome to mad libs, What's your name? ").title()

name = raw_input( "Tell me a girls name, and press enter. ").title()
food = raw_input("What is your favorite food to eat, and press enter. ")
noun = raw_input("Tell me a noun, and press enter. ")
adjective = raw_input("Give me an adjective, and press enter. ")

number = raw_input("Give me a number, and press enter. ")
if type(raw_input) !=int:
      number = raw_input("Please spell out the number.  ")  



print


print '_________________________'
print
print 'Once upon a time at San Diego State University, there lived' 
print 'a princess whose name was Princess' , name +'.' ' Princess' 
print name, 'liked to eat' ,food, 'but her kingdom had little'
print food, 'to offer her. '  'One day' ,number,  'of Princess' ,name+"'s" 
print 'students went out into the kingdom and found a' 
print noun +'.'  ' The' ,number, 'students brought the' ,noun, 'back'  
print 'to the SDSU Palace for the Princess. Princess' ,name, '  '
print  'discovered she liked eatng a' ,noun, 'better than' ,food +'.'  
print 'Princess' ,name, 'continued to reign over her kingdom'
print 'feeling' ,adjective+'.' 
print  
print "The End!"

