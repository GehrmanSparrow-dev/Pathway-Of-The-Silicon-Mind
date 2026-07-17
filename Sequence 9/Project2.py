import csv
import json

input_file = "C:\\Pathway of the Silicon Mind\\Sequence 9\\Grades.csv"
output_file = "student_summary.json"

students = []
cgpas = []

# Read the CSV file
with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Replace missing values
        for key in row:
            if row[key].strip() == "":
                row[key] = "N/A"

        # Convert CGPA to float
        row["CGPA"] = float(row["CGPA"])
        cgpas.append(row["CGPA"])

        students.append(row)

# Calculate average CGPA
average_cgpa = round(sum(cgpas) / len(cgpas), 2)

# Find top student
top_student = max(students, key=lambda student: student["CGPA"])

# Create summary
summary = {
    "average_cgpa": average_cgpa,
    "top_student": {
        "seat_no": top_student["Seat No."],
        "cgpa": top_student["CGPA"]
    },
    "total_students": len(students),
    "students": students
}

# Write to JSON
with open(output_file, "w") as file:
    json.dump(summary, file, indent=4)

print("Data processed successfully!")
print("Average CGPA:", average_cgpa)
print("Top Student:", top_student["Seat No."], "-", top_student["CGPA"])
print("Results saved to", output_file)