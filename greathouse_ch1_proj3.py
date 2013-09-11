# Marcus Greathouse
# CS 140
# Chapter 1: Project 3

# Oil Conversions & Calculations

# input
gallons_gas =  float(input('Gallons of gasoline: '))

# constants
liters_gallon = 3.78541 #liters per gallon
gallons_barrel = 19.5	#gallons
co2_gallon = 20			#lbs
btu_gas = 115000		#btu per gallons
btu_ethanol = 75700		#btu per gallons
price = 3.00				#dollars per gallons

#variables
liters = gallons_gas * liters_gallon			#liters
barrels = gallons_gas / gallons_barrel			#barrels
co2 = gallons_gas * co2_gallon					#lbs
ethanol = gallons_gas * btu_gas / btu_ethanol	#gallons
cost = gallons_gas * price						#dollars

print(gallons_gas, 'of gas is equivalent to', liters_gallon, 'liters.\n',
	'It takes', barrels, 'barrels to make that much gas.\n',
	co2, 'lbs of carbon dioxide is produced.\n',
	'It would take', ethanol, 'gallons of ethanol to produce the same amount of energy.\n',
	'At {:.2f} dollars a gallon, that much gas costs {:.2f} dollars.'.format(price, cost))
