# Ask user for a numerical grade
grade_input = input("Enter a numerical grade (0-100): ").strip()

# Check if input is a number
if not grade_input.isdigit():
    print("Error: Please enter a number")
else:
    grade = int(grade_input)

    # Check if grade is within range
    if grade < 0 or grade > 100:
        print("Error: Grades must be between 0 and 100")
    else:
        # Convert grade to letter
        if grade >= 80:
            letter = "A"
        elif grade >= 60:
            letter = "B"
        elif grade >= 50:
            letter = "C"
        elif grade >= 40:
            letter = "D"
        else:
            letter = "F"

        print(f"Your grade is: {letter}")
