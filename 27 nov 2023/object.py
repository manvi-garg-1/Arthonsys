'''Q2. Object Instantiation Instantiate multiple `Student` objects and showcase their attributes and methods.'''

class Student:
  Address="Jaipur"
  Name="manvi"
  Branch="MCA"
  College="IIIM"
  Rollno=11
  def Show(self):
    print("IIIM College Student information")
    print("Student Name: ", self.Name +
          "\nBranch Name: ", self.Branch +
          "\nCollege Name: ", self.College +
          "\nAddress Name: ", self.Address +
          "\nStudent Rollno: ", self.Rollno)


a =Student()
a.Show()
b=Student()
b.Address="DHOLPUR"
b.Show()