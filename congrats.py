#!/usr/bin/env python

WINTER_2017 = ['K. Student', 'J. Student', 'L. Student', 'M. Student', 'Z. Student']
# ADD A NEW LINE HERE TO ADD YOURSELF TO THE LIST using +=
WINTER_2017 += ['A. Husmann', 'G. Carvalho']

print 'YAY!'

def wish_congrats(class_list) :
	for students in class_list: 
		print 'Congrats %s!  You completed Programming for Data Analytics!' % students

print 'YOU GUYS ARE AWESOME!!!'
wish_congrats(WINTER_2017)
