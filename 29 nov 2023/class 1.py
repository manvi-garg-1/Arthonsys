class Student:
    def __init__(self,Student_id,Student_name,Student_Branch,Student_Address):
        self.Student_id=Student_id
        self.Student_name=Student_name
        self.Student_Brach=Student_Branch
        self.Student_Address=Student_Address
    def Student_Add(self,S_ID,S_Name,S_Branch,S_A):
        ob=Student(S_ID,S_Name,S_Branch,S_A)
        ls.append(ob)
    def Student_Details(self):
        print(f"Student ID: {self.Student_id} \n"
              f"Student Name: {self.Student_name} \n"
              f"Student Branch Name: {self.Student_Brach} \n"
              f"Student Address: {self.Student_Address}")
        print()
    def Student_Search(self,StudentID):
        for i in range(ls.__len__()):
            if ls[i].Student_id == StudentID:
                return i
    def Student_Delete(self,StudentID):
        i=obj.Student_Search(StudentID)
        del ls[i]
    def Student_Update(self,StudentID,Number):
        i=obj.Student_Search(StudentID)
        ID= Number
        ls[i].Student_id = ID
ls =[]
obj=Student(0,'','','')
while(True):
    print(" 1. Student Add \n 2. Student Details \n 3.Student Search \n 4. Student Delete \n 5 Student Details Update \n 6. Exit")
    choice=int(input("Enter the choice:"))
    if choice ==1:
        obj.Student_Add(101,'mahendra sain','MCA','Jaipur')
        obj.Student_Add(102,'Nihit','MCA','Jaipur')
        obj.Student_Add(103,'gagan','MCA','Jaipur')
    elif choice ==2:
        print("Student of List ")
