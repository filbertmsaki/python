#python List
subject = ['Physics','Chemistry','Geograph','History','Biology'];
marks = [70,20,50,40,85,69,98,20,11,10,34,45,51];
grade = ['A','B','C','D','E','F'];

#Accessing Values in lists
print ("subject[1] = ",subject[1]);
print ("marks[1:4] = ",marks[1:4]);
print ("\n");

#Updating the List
print ("Current Marks = ",marks);
marks[1]=21;
print ("Updated Marks = ", marks);
print ("\n");

#Delete List
print ("Current Grades = ", grade);
del grade[5];
print ("Remaining Grades", grade);
print ("\n");

#Check the lenght of list maximum and minimum values
print("Length of marks is", len(marks));
print("Maximum value of marks is ",max(marks));
print("Minimum value of marks is ", min(marks));
print("\n");

#remove(), insert(), reverse(), sort()
print("List of Subject",subject);
subject.remove('History');
print("New list ", subject); 

subject.insert(1,'History');

grade.insert(5,'F');
print("\n","New List After Insert");
print ("Subjects : ",subject);
print ("Grades :", grade);
#reverse
grade.reverse();
print ("Grades",grade);

#Sort
grade.sort();
print ("Grades",grade);


