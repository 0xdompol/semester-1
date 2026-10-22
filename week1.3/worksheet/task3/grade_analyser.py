# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
file_name = input("What is the student file name: ")
# open the file
def read_data():
    n = 0
    ids = []
    means = []
    grades = []
    with open(f"{file_name}.csv", "r") as infile:
        for line in infile:
            if n == 0:
                n += 1
            else:
                data = line.strip().split(",")
                ids.append(data[0])
                data = [int(item) for item in data[1:] if item.strip()]
                mean = sum(data)/len(data)
                means.append(mean)
                if mean >= 70:
                    grade = "1"
                elif mean >= 60:
                    grade = "2:1"
                elif mean >= 50:
                    grade = "2:2"
                elif mean >= 40:
                    grade = "3"
                else:
                    grade = "F"
                grades.append(grade)
    return ids,means,grades,data
# read in the data, and for each student calculate their average grade and classification

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f} 

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder
def write_out(ids,means,grades):
    new_file_name = file_name + ".csv_out.csv"
    with open(new_file_name, "w") as outfile:
        for x in range(0,len(ids)):
            outfile.write(f"{ids[x]},{means[x]:.2f},{grades[x]}\n")

#write_out(ids,means,grades,data)
ids,means,grades,data = read_data()
write_out(ids,means,grades)