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