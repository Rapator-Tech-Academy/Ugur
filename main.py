import json

from actions import CreateStudent, CreateStaff, CreateLesson, DeleteUser

create_student = CreateStudent()
create_staff = CreateStaff()
create_lesson = CreateLesson()
delete_user = DeleteUser()

user_selection = input("Which process do you want to start? (Delete - D, Add - A): ")

if user_selection == "D":
    with open('datas.json', 'r') as file:
        data = file.read()
        print(data)

    id = input("Please enter id of contact: ")
    delete_user.run(id=id)

elif user_selection == "A":
    type = int(input("Please enter type (1-Student, 2-Staff, 3-Lesson): "))

    if type == 3:
        time = input("Please enter time: ")
        lesson_type = input("Please enter type of lesson (Online or Offline): ")
        team = input("Please enter name of team: ")

        create_lesson.run(
            time = time,
            type = lesson_type,
            team = team
        )
    else :
        name = input("Please enter contact name: ")
        surname = input("Please enter contact surname: ")
        age = input("Please enter contact age: ")
        number = input("Please enter phone number: ")

        if type == 1:
            create_student.run(
                name = name,
                surname = surname,
                age = age,
                number = number
            )
        elif type == 2:
            salary = input("Please enter salary of staff person: ")

            create_staff.run(
                name=name,
                surname=surname,
                age=age,
                number=number,
                salary=salary
            )
else:
    print("Please try again")














