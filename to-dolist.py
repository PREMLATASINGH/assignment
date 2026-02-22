to_do_list=["Buy groceries",
           "Finish project report","Call mom",
           "Exercise for 30 minutes",]
print("To-Do List:")
print(to_do_list)
to_do_list.append("Read a book")
print(to_do_list)
to_do_list.remove("Call mom")
print(to_do_list)
to_do_list[1]="Finish project report and send email"
print(to_do_list)
if "Exercise for 30 minutes" in to_do_list:
    print("Don't forget to exercise!")
else:
    print("You have completed your exercise for the day!")