import logging

import Utils.Activities
from Utils import Student,Office
logging.basicConfig(filename="story.log",level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')


#Lets have few list of courses
Courses = []
c1 = Student.iNeuronCourse('Python with Analytics','7000')
Courses.append(c1)
c2 = Student.iNeuronCourse('Python with FullStack Data Science','15000')
Courses.append(c2)
c3 = Student.iNeuronCourse('Python with Networking','7000')
Courses.append(c3)
c4 = Student.iNeuronCourse('Python with FullStack Web Development','10000')
Courses.append(c4)
c5 = Student.iNeuronCourse('Basic Python','3000')
Courses.append(c5)

logging.info("iNeuron has below courses".center(100,"*"))
for course in Courses:
    name, fees = course.courseDetails()
    logging.info("Name of course -" + name + " : " + " Fees of Course - " + fees)


#Lets get details of Enquiries
Enquiries=[]

Enquiries.append(Office.enquiry("Chandu","Basic Python"))
Enquiries.append(Office.enquiry("Muskaan","Python with FullStack Web Development"))
Enquiries.append(Office.enquiry("Cheetah","Python with Networking"))
Enquiries.append(Office.enquiry("John","Python with FullStack Data Science"))
Enquiries.append(Office.enquiry("Saajid","Python with Analytics"))
Enquiries.append(Office.enquiry("Shyam","Python with FullStack Web Development"))
Enquiries.append(Office.enquiry("Suraj","Python with Networking"))
Enquiries.append(Office.enquiry("Ashwini","Python with FullStack Data Science"))
Enquiries.append(Office.enquiry("Shraddha","Basic Python"))
Enquiries.append(Office.enquiry("Varsha","Python with FullStack Web Development"))
Enquiries.append(Office.enquiry("Deepak","Python with Networking"))
Enquiries.append(Office.enquiry("Deepika","Python with FullStack Data Science"))
Enquiries.append(Office.enquiry("Amit","Python with Analytics"))
Enquiries.append(Office.enquiry("Govardan","Python with FullStack Web Development"))
Enquiries.append(Office.enquiry("Keerthi","Python with Networking"))
Enquiries.append(Office.enquiry("Sachin","Python with FullStack Data Science"))

logging.info("Below are list of students who enquired".center(100,"*"))
for Enq in Enquiries:
    name, course = Enq.getDetails()
    logging.info("Name of inquiry -" + name + " : " + " course intereseted in - " + course)

#Lets check how many enquiries have turned to students
enquiriesT = tuple(Enquiries)
enroll = []

getFees = lambda x: [i.coursename for i in Courses].index(x)

logging.info("Ineuron calls these list of students who had enquired".center(100,"*"))
try:
    for Enq in Enquiries:
        logging.info(Enq.name + ": You had inquired for course " + Enq.course + ". Do you want to enroll?")
        inpYesNo = input("Please Type Yes if " + Enq.name + " student is willing to enroll or No =>")
        logging.info(inpYesNo)
        if inpYesNo.strip() == 'Yes':
            inpFrom = input('You are referenced by')
            enroll.append( Student.enrollment(Enq.course,Courses[getFees(Enq.course)]._coursefees,Enq.name,inpFrom,True,True))

except Exception as e:
    logging.error(e)

try:
    logging.info("Below are the enrolled students".center(100, "*"))
    for enrolled in enroll:
        logging.info("Name:" + enrolled.name + "| course :" + enrolled.course + "| Reference by :" + enrolled.getReferenceFrom() + "| course fees: " + enrolled._coursefees)

except:
    logging.error(e)

#Settling the amount in the Account section
students = []
print("".center(100,'*'))
try:
    logging.info("Account section checks the payment Details of student".center(100, "*"))
    inpCount = 1
    for enrolled in enroll:

        logging.info("Please enter phone number and email address of " + enrolled.name + " student ->")
        pe = input("Please enter phone number and email address of " + enrolled.name + " student ->")
        logging.info(pe)
        logging.info('Has ' + enrolled.name + " paid course fees? Total Course fees" + enrolled._coursefees )
        s = Student.Student(enrolled.name, enrolled.course, enrolled._coursefees, enrolled.getReferenceFrom(), enrolled.getSyllabusShared(),enrolled._enrolled, pe.split(',')[0], pe.split(',')[1], inpCount)
        inpYesNo = input("Please Type Yes if " + enrolled.name + " has paid and the fees or else No. For example: Yes,200; Total CourseFees" + enrolled._coursefees +" ->")
        logging.info("Please Type Yes if " + enrolled.name + " has paid and the fees or else No. For example: Yes,200; Total CourseFees" + enrolled._coursefees +" ->")
        logging.info(inpYesNo)
        if inpYesNo.strip().find('Yes') > 0:
            s.hasPaidFees, s.initialFees = True, inpYesNo.split(',')[1]
        else:
            s.hasPaidFees, s.initialFees = False, '0'
        students.append(s)
        inpCount += 1
except Exception as e:
    logging.error(e)

try:
    logging.info("Below are Student Details".center(100, "*"))
    for student in students:
        n,p,e,r = student.getDetails()
        logging.info("Name :" + n + "|| Phone Number :" + p + "|| email id :" + e + "|| Roll no:" + str(r))
except Exception as e:
    logging.error(e)

#Below are few instructors
try:
    logging.info("Arranging the list of instructors".center(100, "*"))
    instructors = []
    instDict ={}
    i1 = Office.instructor('Sudha','Python with Analytics')
    instructors.append (i1)
    i2 = Office.instructor('Shyam','Python with Analytics, Baisc Python, Python with FullStack Data Science')
    instructors.append(i2)
    logging.info("Below are the list of instructors with specialization".center(100, "*"))
    for instructor in instructors:
        n,s = instructor.getDetails()
        instDict.update({n:s})
        logging.info(n + " has the specialization of " + s)
    logging.info(instDict)
except Exception as e:
    logging.error(e)


#Below are few of student activities
try:
    logging.info("Overall Student Activitities".center(100,'~'))
    overallreport = []
    quest = Utils.Activities.askActivitiesQuestions()
    for student in students:
        blogResponse, bDetails = quest.askQuestionBlog(student.name)
        intResponse, intDetails = quest.askQuestionIntership(student.name)
        overallObject = Utils.Activities.overallreport(student.getrollno(),bDetails.split(',')[0],bDetails.split(',')[1],intDetails.split(',')[0],intDetails.split(',')[1],intDetails.split(',')[2],"Good")
        if blogResponse == 'y':
            overallObject.setHasCreatedBlog(True)
        else:
            overallObject.setHasCreatedBlog(False)
        overallreport.append(overallObject)
except Exception as e:
    logging.error(e)

try:
    logging.info("List of Overall activities".center(100,'>'))
    for rep in overallreport:
        dictStud = {student.getrollno(): student.name for student in students}
        logging.info("Blog Topic:" + rep.topic + "| Creator(Student): " + dictStud[rep.rollno] + "| For Blog Number of claps:" + str(rep.totalClaps()) + "| Internship client:" + rep.client + "|Internship project: " + rep.project + "| Instructor Feedback: " + rep.getInstructorfeedback())
except Exception as e:
    logging.error(e)


