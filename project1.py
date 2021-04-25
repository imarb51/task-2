import csv

def writer_info_csv(info_list):
    with open('student.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() ==0:
            writer.writerow(["Name","Age","Contact No","E-mail"])
            
        writer.writerow(info_list)

if __name__ == "__main__":
    condition = True
    student_num = 1


while(condition):
    student=input("Enter student #{} the name  age contact no. Email :".format(student_num))

    #split
    student_nfo_1 = student.split(' ')
    print("\nThe Entered Information is -\nName: {}\nAge: {}\nContact No: {}\nE-mail: {}"
          .format(student_nfo_1 [0], student_nfo_1 [1], student_nfo_1[2], student_nfo_1[3]))
    
    choice_check=input("Is the entered information correct?: ")
    
    if choice_check == "yes":
        writer_info_csv(student_nfo_1)
        condition_check=input("Enter stop to Stop the another information of students: ")
        if condition_check == "stop":
            condition = False 
        elif condition_check == "Go on":
            condition = True
            student_num =student_num + 1
    elif choice_check=="no":
        print("reenter the values.")
     
