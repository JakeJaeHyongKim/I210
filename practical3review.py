class Student(object):
    student_list = []

    def __init__(self, name, current_gpa, initial_gpa = 3.0):
        self.name=name
        self.current_gpa=current_gpa
        self.initial_gpa=initial_gpa
        Student.student_list.append(self)


    def __str__():
        reply="Student name: "+self.name
        reply+="\nInitial GPA"+


    def __cmp__():
        #Compares the current GPA of two students
        pass


    @staticmethod
    def best_student():
        #Best Student is..(drumroll)
        #Prints out the student's status
        pass



    def hack():
        #Trade the current GPA of two students that you specify
        pass


class good_student(Student):

    def semester(self,num):
        #A good student's current GPA goes up by a random number between 0.1 and 0.5 each semester(num)
        #The highest grade a student can hold is 4.3
        pass


class bad_student(Student):

    def semester(self,num):
        #A bad student's current GPA goes down by a random number between 0.1 and 0.5 each semester(num)
        #The lowest grade a student can hold is 0.0
        pass

        

#Main Code
student1 = bad_student("John", 3.3, 3.1)
student2 = good_student("Billy", 2.7, 2.9)
student3 = bad_student("Susan", 3.5)
student4 = good_student("Minji", 3.8, 3.4)

print ("Current Students:\n")
print (student1)
print (student2)
print (student3)
print (student4)

Student.best_student()

student1.hack(student3)
student2.hack(student4)

print ("Current Students:\n")
print (student1)
print (student2)
print (student3)
print (student4)

Student.best_student()

print ("The Students have gone through two semesters")
student1.semester(2)
student1.semester(2)
student1.semester(2)
student1.semester(2)

print ("Current Students:\n")
print (student1)
print (student2)
print (student3)
print (student4)

print ("The Students have gone through four semesters")
student1.semester(4)
student1.semester(4)
student1.semester(4)
student1.semester(4)

print ("Current Students:\n")
print (student1)
print (student2)
print (student3)
print (student4)


##OUTPUTS:
##Current Students:
##Student name: John
##Initial GPA: 3.1
##Current GPA: 3.3
##
##Student name: Billy
##Initial GPA: 2.9
##Current GPA: 2.7
##
##Student name: Susan
##Initial GPA: 3.0
##Current GPA: 3.5
##
##Student name: Minji
##Initial GPA: 3.4
##Current GPA: 3.8
##
##
##Best Student is..(drumroll)
##Student name: Minji
##Initial GPA: 3.4
##Current GPA: 3.8
##
##
##Swapping John and Susan...
##Swapping Billy and Minji...
##
##Current Students:
##Student name: John
##Initial GPA: 3.1
##Current GPA: 3.5
##
##Student name: Billy
##Initial GPA: 2.9
##Current GPA: 3.8
##
##Student name: Susan
##Initial GPA: 3.0
##Current GPA: 3.3
##
##Student name: Minji
##Initial GPA: 3.4
##Current GPA: 2.7
##
##
##Best Student is..(drumroll)
##Student name: Billy
##Initial GPA: 3.4
##Current GPA: 3.8
##
##
##The Students have gone through two semesters
##Current Students:
##Student name: John
##Initial GPA: 3.1
##Current GPA: ???
##
##Student name: Billy
##Initial GPA: 2.9
##Current GPA: ???
##
##Student name: Susan
##Initial GPA: 3.0
##Current GPA: ???
##
##Student name: Minji
##Initial GPA: 3.4
##Current GPA: ???
##
##
##The Students have gone through four semesters
##Current Students:
##Student name: John
##Initial GPA: 3.1
##Current GPA: ???
##
##Student name: Billy
##Initial GPA: 2.9
##Current GPA: ???
##
##Student name: Susan
##Initial GPA: 3.0
##Current GPA: ???
##
##Student name: Minji
##Initial GPA: 3.4
##Current GPA: ???
