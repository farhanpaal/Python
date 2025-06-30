
def main():
    print("=" * 50)
    print("        ADVANCED AVERAGE CALCULATOR")
    print("=" * 50)
    print("INSTRUCTIONS:")
    print("• Enter -1 to exit at any time")
    print("• Choose from multiple average calculation methods")
    print("• View detailed statistics")
    print("-" * 50)
    
    while True:
        try:
            print("\nSelect calculation method:")
            print("1. Simple Average (Arithmetic Mean)")
            print("2. Weighted Average")
            print("3. Grade Point Average (GPA)")
            print("4. Multiple Students Average")
            print("5. Statistical Analysis")
            print("6. Exit")
            
            choice = int(input("\nEnter your choice (1-6): "))
            
            if choice == -1 or choice == 6:
                print("Thank you for using Average Calculator!")
                break
            elif choice == 1:
                simple_average()
            elif choice == 2:
                weighted_average()
            elif choice == 3:
                gpa_calculator()
            elif choice == 4:
                multiple_students()
            elif choice == 5:
                statistical_analysis()
            else:
                print("Invalid choice! Please select 1-6.")
                
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def simple_average():
    print("\n--- SIMPLE AVERAGE CALCULATOR ---")
    numbers = []
    
    while True:
        try:
            num = input("Enter a number (or -1 to calculate): ")
            if num == "-1":
                break
            numbers.append(float(num))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"\nNumbers entered: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Sum: {sum(numbers):.2f}")
        print(f"Average: {avg:.2f}")
    else:
        print("No numbers entered!")

def weighted_average():
    print("\n--- WEIGHTED AVERAGE CALCULATOR ---")
    values = []
    weights = []
    
    while True:
        try:
            value = input("Enter value (or -1 to calculate): ")
            if value == "-1":
                break
            value = float(value)
            weight = float(input("Enter weight for this value: "))
            
            values.append(value)
            weights.append(weight)
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
    
    if values and weights:
        weighted_sum = sum(v * w for v, w in zip(values, weights))
        total_weight = sum(weights)
        weighted_avg = weighted_sum / total_weight
        
        print(f"\nValues: {values}")
        print(f"Weights: {weights}")
        print(f"Weighted Average: {weighted_avg:.2f}")
    else:
        print("No data entered!")

def gpa_calculator():
    print("\n--- GPA CALCULATOR ---")
    print("Grade Scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0")
    
    total_points = 0
    total_credits = 0
    subjects = []
    
    while True:
        try:
            subject = input("Enter subject name (or -1 to calculate): ")
            if subject == "-1":
                break
                
            grade = input("Enter grade (A, B, C, D, F): ").upper()
            credits = float(input("Enter credit hours: "))
            
            grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
            
            if grade in grade_points:
                points = grade_points[grade] * credits
                total_points += points
                total_credits += credits
                subjects.append({"subject": subject, "grade": grade, "credits": credits, "points": points})
            else:
                print("Invalid grade! Use A, B, C, D, or F.")
                continue
                
        except ValueError:
            print("Invalid input for credits!")
    
    if total_credits > 0:
        gpa = total_points / total_credits
        print(f"\n--- GPA REPORT ---")
        for sub in subjects:
            print(f"{sub['subject']}: {sub['grade']} ({sub['credits']} credits)")
        print(f"\nTotal Credits: {total_credits}")
        print(f"Total Points: {total_points:.2f}")
        print(f"GPA: {gpa:.2f}")
        
        # GPA Classification
        if gpa >= 3.5:
            print("Classification: Excellent")
        elif gpa >= 3.0:
            print("Classification: Good")
        elif gpa >= 2.0:
            print("Classification: Satisfactory")
        else:
            print("Classification: Needs Improvement")
    else:
        print("No subjects entered!")

def multiple_students():
    print("\n--- MULTIPLE STUDENTS AVERAGE ---")
    students = []
    
    while True:
        try:
            name = input("Enter student name (or -1 to calculate): ")
            if name == "-1":
                break
                
            marks = []
            print(f"Enter marks for {name}:")
            
            while True:
                mark = input("Enter mark (or 'done' to finish this student): ")
                if mark.lower() == "done":
                    break
                marks.append(float(mark))
            
            if marks:
                avg = sum(marks) / len(marks)
                students.append({
                    "name": name,
                    "marks": marks,
                    "average": avg,
                    "total": sum(marks),
                    "count": len(marks)
                })
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
    
    if students:
        print(f"\n--- RESULTS FOR {len(students)} STUDENTS ---")
        class_total = 0
        
        for student in students:
            print(f"\n{student['name']}:")
            print(f"  Marks: {student['marks']}")
            print(f"  Average: {student['average']:.2f}")
            print(f"  Total: {student['total']:.2f}")
            class_total += student['average']
        
        class_avg = class_total / len(students)
        print(f"\n--- CLASS STATISTICS ---")
        print(f"Class Average: {class_avg:.2f}")
        
        # Find top performer
        top_student = max(students, key=lambda x: x['average'])
        print(f"Top Performer: {top_student['name']} ({top_student['average']:.2f})")
    else:
        print("No students entered!")

def statistical_analysis():
    print("\n--- STATISTICAL ANALYSIS ---")
    numbers = []
    
    while True:
        try:
            num = input("Enter a number (or -1 to analyze): ")
            if num == "-1":
                break
            numbers.append(float(num))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if numbers:
        numbers.sort()
        n = len(numbers)
        
        # Basic statistics
        mean = sum(numbers) / n
        median = numbers[n//2] if n % 2 == 1 else (numbers[n//2-1] + numbers[n//2]) / 2
        minimum = min(numbers)
        maximum = max(numbers)
        range_val = maximum - minimum
        
        # Variance and Standard Deviation
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_dev = variance ** 0.5
        
        print(f"\n--- STATISTICAL ANALYSIS REPORT ---")
        print(f"Data: {numbers}")
        print(f"Count: {n}")
        print(f"Mean (Average): {mean:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Minimum: {minimum:.2f}")
        print(f"Maximum: {maximum:.2f}")
        print(f"Range: {range_val:.2f}")
        print(f"Variance: {variance:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")
        
        # Quartiles
        q1 = numbers[n//4] if n >= 4 else "N/A"
        q3 = numbers[3*n//4] if n >= 4 else "N/A"
        print(f"First Quartile (Q1): {q1}")
        print(f"Third Quartile (Q3): {q3}")
        
    else:
        print("No numbers entered!")

if __name__ == "__main__":
    main()
