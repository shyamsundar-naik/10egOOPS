import logging
class blogs:
    """This class will hold information about the blog topic, whether the student has created it or not, and the
    number of people clapped about the blog."""
    __hasCreatedBlog = False
    def __init__(self,topic,ncps,rollno):
        #There are two private data members(__hasCreatedBlog and __nopplclapped) and one public data member(topic).
        self.topic = topic
        self.__nopplclapped = int(ncps)
        self.rollno = rollno

    def increaseClap(self):
        """This method will increase the number of claps by 1."""
        self.__nopplclapped = self.__nopplclapped + 1

    def totalClaps(self):
        """This method will provide a number of claps for a student."""
        return self.__nopplclapped

    def getHasCreatedBlog(self):
        """This method will return if the Student has created a blog."""
        return self.__hasCreatedBlog

    def setHasCreatedBlog(self,created):
        """This method will return if the Student has created a blog."""
        self.__hasCreatedBlog = created


class internship:
    """Internship Class which has details about the client, project and overall feedback"""
    def __init__(self,client,project,overallfeedback,rollno):
        self.client = client
        self.project = project
        self.overallfeedback = overallfeedback
        self.rollno = rollno

    def getdetails(self):
        return self.client, self.project, self.overallfeedback


class askActivitiesQuestions:
    def askQuestionBlog(self,nameStudent):
        logging.info(nameStudent + ': Are you interested to create blog? y/n ==>')
        inpyn = input(nameStudent + ': Are you interested to create blog? y/n ==>')
        logging.info(inpyn)
        if inpyn == 'y':
            logging.info("Please enter topic of blog:")
            topic = input("Please enter topic of blog and number of claps: ")
            logging.info(topic)
        else:
            topic = ',0'
        return inpyn, topic

    def askQuestionIntership(self,nameStudent):
        logging.info(nameStudent + ': Are you interested Internship? y/n ==>')
        inpyn = input(nameStudent + ': Are you interested Internship? y/n ==>')
        logging.info(inpyn)
        if inpyn == 'y':
            logging.info("Please enter topic of blog:")
            iDetails = input("Please enter topic of client,project,feedback: ")
            logging.info(iDetails)
        else:
            iDetails = ',,'
        return inpyn, iDetails


class overallreport(internship,blogs):
    def __init__(self,rollno,blogtopic,ncps,client,project,feedback,instructorfeedback):
        blogs.__init__(self,blogtopic,ncps,rollno)
        internship.__init__(self,client,project,feedback,rollno)
        self.__instructorfeedback = instructorfeedback

    def getInstructorfeedback(self):
        return self.__instructorfeedback