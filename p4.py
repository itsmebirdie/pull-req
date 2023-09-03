# A python program to create a dictionary whose keys are months names and values are number of days in that month. Ask the user to enter a month name and print the number of days in that month
months = {'january':31,'february':28,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}
month = input('Enter a month name: ')
print('Number of days in ',month,' is ',months[month.lower()])