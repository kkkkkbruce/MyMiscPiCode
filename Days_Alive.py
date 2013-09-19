#-------------------------------------------------------------------------------
# Name:        Days_Alive
# Purpose:
#
# Author:      KKKKKBruce
#
# Created:     13/02/2013
# Copyright:   (c) Kevin 2013
# Licence:     The MIT License (MIT)
#-------------------------------------------------------------------------------
import sys
from datetime import date

def days_alive(birthdate):
    today = date.today()
    delta = today - birthdate
    return delta.days

def main():
    if len(sys.argv) == 4:
	birthyear = int(sys.argv[1])
	birthmonth = int(sys.argv[2])
	birthday = int(sys.argv[3])
    else:
        print('LETS FIND OUT HOW MANY DAYS OLD YOU ARE')
        birthyear = input("Enter your birthday year (use 4 digits):")
        birthmonth = input("Enter your birthday month (1-12):")
        birthday = input("Enter your birthday day (1-31):")

    print('\n You are {:,} days old today. How are you going to spend today? \n'.format(days_alive(date(birthyear,birthmonth,birthday))))
    pass

if __name__ == '__main__':
    main()
