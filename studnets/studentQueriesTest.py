import unittest
from studentQueries import *
from students import studentsList

class studentTest(unittest.TestCase):
    def test_hieghest(self):
        actualStudent = highest(studentsList,'mathematics')

        self.assertEqual("Dharmendra Singh",actualStudent['name'])
        self.assertEqual(1001,actualStudent["roll_num"])
        self.assertEqual(97,actualStudent["mathematics"])

        actualStudent = highest(studentsList,"english")

        self.assertEqual("Jai Om Pandey",actualStudent['name'])
     	self.assertEqual(1009,actualStudent["roll_num"])
     	self.assertEqual(98,actualStudent["english"])

        actualStudent = highest(studentsList,"computer_science")
        self.assertEqual("Jai Om Pandey",actualStudent['name'])
     	self.assertEqual(1009,actualStudent["roll_num"])
     	self.assertEqual(98,actualStudent["computer_science"])

    def test_lowest(self):
        actualStudent = lowest(studentsList,'mathematics')

        self.assertEqual("Ganesh Patil",actualStudent['name'])
        self.assertEqual(1045,actualStudent["roll_num"])
        self.assertEqual(0,actualStudent["mathematics"])

        actualStudent = lowest(studentsList,"english")

        self.assertEqual("Suman Das",actualStudent['name'])
     	self.assertEqual(1030,actualStudent["roll_num"])
     	self.assertEqual(4,actualStudent["english"])

        actualStudent = lowest(studentsList,"computer_science")

        self.assertEqual("Supriya Gole",actualStudent['name'])
     	self.assertEqual(1014,actualStudent["roll_num"])
     	self.assertEqual(0,actualStudent["computer_science"])

    def test_above(self):
         actualStudents = above(studentsList,"mathematics",90);
         expectedNames=["Adarsh Kumar Sandilya","Anusree Prakash","Dharmendra Singh","Saranraj Sekar"]
         actualNames = map(lambda x : x['name'] , actualStudents)

         self.assertEqual(4,len(actualNames))
         self.assertEqual(expectedNames , actualNames)

         actualStudents = above(studentsList,"english",90);
         expectedNames=["Jai Om Pandey","Sagar Maurya","Saranraj Sekar"]
         actualNames = map(lambda x : x['name'] , actualStudents);

         self.assertEqual(3,len(actualNames))
         self.assertEqual(expectedNames , actualNames)

         actualStudents = above(studentsList,"computer_science",90);
         expectedNames=["Arindam Karmakar","Ashwin Kumar KA","Jai Om Pandey","Mitesh Kumar Jha","Sayan Bisui"]
         actualNames = map(lambda x : x['name'] , actualStudents);

         self.assertEqual(5,len(actualNames))
         self.assertEqual(expectedNames , actualNames);

    def test_below(self):
         actualStudents = below(studentsList,"mathematics",5);
         expectedNames=["Ashwin Kumar KA","Bindu S","Ganesh Patil","Nimesh P"]
         actualNames = map(lambda x : x['name'] , actualStudents);

         self.assertEqual(4,len(actualNames))
         self.assertEqual(expectedNames , actualNames);

         actualStudents = below(studentsList,"english",10)
         expectedNames=["Gaurav K","Prasun Kumar Palchodhary","Suman Das"]
         actualNames = map(lambda x : x['name'] , actualStudents)

         self.assertEqual(3,len(actualNames))
         self.assertEqual(expectedNames , actualNames);

         actualStudents = below(studentsList,"computer_science",10);
         expectedNames=["Abhishek Gupta","Rahul Nandi","Saranraj Sekar","Suman Maity","Supriya Gole","Surajit Chongder"]
         actualNames = map(lambda x : x['name'] , actualStudents)

         self.assertEqual(6,len(actualNames))
         self.assertEqual(expectedNames , actualNames);

    def test_phoneBook(self):
        phone_book = phoneBook(studentsList);
        self.assertEqual(2,len(phone_book["B"]));
        self.assertEqual(16,len(phone_book["S"]));
        self.assertEqual(0,len(phone_book["Z"]));
        self.assertEqual(undefined,phone_book["7"])

        namesThatBeginWithB =map(lambda x : x['name'] , phone_book["B"])
        self.assertEqual(["Bindu S","Brindaban Patra"],namesThatBeginWithB);

    def test_phoneBook(self):
        actualMathematicsAverage = averageOf(studentsList,"mathematics");
        self.assertEqual(50,actualMathematicsAverage);

        actualCSAverage = averageOf(studentsList,"computer_science");
        self.assertEqual(52,actualCSAverage);

        actualEnglishAverage = averageOf(studentsList,"english");
        self.assertEqual(52,actualEnglishAverage);

    def test_between(self):
        actualStudents = between(studentsList,"mathematics",10,20)
        expectedNames = ['Anjaly Joy',
                        'Arindam Karmakar',
                        'Jai Om Pandey',
                        'Madhuri Patil',
                        'Rahul Nandi',
                        'Sagar Maurya',
                        'Sayan Bisui' ]
        actualNames = map(lambda x : x['name'] , actualStudents)

        self.assertEqual(7,len(actualStudents));
        self.assertEqual(expectedNames,actualNames)

if __name__ == '__main__':
	unittest.main()
