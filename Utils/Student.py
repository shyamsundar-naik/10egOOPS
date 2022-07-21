import Utils.Office

class iNeuronCourse:
    """iNeuronCourse class is a class used to hold information about the course, course fees, references, and syllabus shared"""
    def __init__(self,coursename,coursefees):
        #Here we create data members for the class. There are two protected data members(_coursefees, _syllabusshared),
        # one private data member(__referencefrom), and one public data member (coursename).
        self.coursename = coursename
        self._coursefees = coursefees
        #self.__referencefrom = referencefrom
        #self._syllabusshared = syllabusshared

    def courseDetails(self):
        """This method will return the name of the course and fees related to the course."""
        return self.coursename, self._coursefees


#One of example for inheritance
class enrollment(iNeuronCourse,Utils.Office.enquiry):

    def __init__(self, course, fees, name, referenceFrom, syllabusShared,enrolled):
        iNeuronCourse.__init__(self,course,fees)
        Utils.Office.enquiry.__init__(self,name,course)
        self.__referenceFrom = referenceFrom
        self.__syllabusShared = syllabusShared
        self._enrolled = enrolled

    def getReferenceFrom(self):
        return self.__referenceFrom

    def getSyllabusShared(self):
        return self.__syllabusShared

    def getDetails(self):
        return self.name, self.coursename, self.fees


class Student(enrollment):
    """
    Student class represents a template that will hold information about students' basic details like name, phone number,
    email id, etc. Some methods are used to access the information about the student.
    """
    hasPaidFees = False
    initialFees = 0
    def __init__(self,name,course,fees,referenceFrom,sH,enroll,phonenumber,emailid,roll):
        #Here we can see that there are two protected data members(_phonenumber, _emailid), one public data member(name),
        # and one private data member (__rollno)
        enrollment.__init__(self,course,fees,name,referenceFrom,sH,enroll)
        self._phonenumber = phonenumber
        self._emailid = emailid
        self.__rollno = roll

    def getrollno(self):
        """This method is an example to showcase data abstraction. It's the first example of data abstraction."""
        return self.__rollno

    def getDetails(self):
        """This method will return information about a student's name, phone number, email, and roll no."""
        return self.name,self._phonenumber,self._emailid, self.__rollno

