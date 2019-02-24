import sys

inFile = sys.argv[1]

with open(inFile, 'r') as i:
	lines = i.readlines()

def setupTestCase(line):
	parameters_txt = lines[line]
	parameters = parameters_txt.split(' ')
	parameters_dict = {
		'rows': int(parameters[0]),
		'columns': int(parameters[1]),
		'energy': int(parameters[2]),
		'starting_row': int(parameters[3]),
		'starting_column': int(parameters[4]),
		'ending_row': int(parameters[5]),
		'ending_column': int(parameters[6])
	}
	for row in range(parameters_dict["rows"]):
		print(lines[line + 1 + row])
	return parameters_dict

print(setupTestCase(1))

