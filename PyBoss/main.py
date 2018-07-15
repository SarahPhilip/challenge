import csv
import us_state_abbrev as s

csv_path_input = "employee_data.csv"
csv_path_output = "cleaned_data.csv"
with open(csv_path_input,'r') as infile, \
	open(csv_path_output, 'w', newline ='') as outfile :
	reader = csv.reader(infile, delimiter = '\n')
	writer = csv.writer(outfile)

	writer.writerow(["Emp ID"])
	csv_header = next(infile)
	for row in reader:
		this_row = row[0].split(',')
		emp_id = this_row[0]
		name = this_row[1].split(' ')
		first_name = name[0]
		last_name = name[1]
		dob = this_row[2].split('-')
		dob_new = dob[1] + '/' + dob[2] + '/' + dob[0]
		ssn = this_row[3]
		ssn_new = "***-**-"+ssn[-4:]
		state = this_row[4]
		if state in s.us_state_abbrev:
			state_new = s.us_state_abbrev[state]
		writer.writerow([emp_id,first_name,last_name,dob_new,state_new])
		# print(state_new)
		# print(ssn_new)
		# print(emp_id)
		# print(first_name)
		# print(last_name)
		# print(dob_new)
		

