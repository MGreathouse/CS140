# Marcus Greathouse
# CS 140
# Chapter 1: Project 3

# Population Estimator
# input
#years = int(input('Years from now to check: '))
years = 15

# constants
current_population = 307357870	#people
days_year = 365					#days_year
hours_day = 24					#hours
seconds_hour = 3600				#seconds
birth_rate = 7					#seconds per person
death_rate = 13					#seconds per person
immigration_rate = 35			#seconds per person

# variables
seconds_changed = years * days_year * hours_day * seconds_hour
estimated_population = current_population + (seconds_changed / birth_rate) - (seconds_changed / death_rate) + (seconds_changed / immigration_rate)

print('There should be about', estimated_population, 'in', years, 'years.')
