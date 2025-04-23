import random

def get_students ():
    students  = []
    print("Enter student names separated by commas (e.g., yash,anil,hari,kushi,akshy,kishan,akash,suhas):")
    input_str = input("Your list : ")
    students = [name.strip() for name in input_str.split(",")if name.strip()]
    return students 


def pick_random_student(students):
    if students: 
        return random.choice(students)
    else:
        return None

def main():
    students = get_students()
    if students:

        selected_student = pick_random_student(students)
        print(f"\n 🎉 The randomly selected student is : {selected_student}")

    else:
        print("No student entered. please try again.")

if __name__ == "__main__":
    main()



