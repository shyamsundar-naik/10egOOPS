class jobSeeker:
    """Entries for who are looking for jobs"""
    listOfCompanies = ['IBM','Dell','Tesla','Spacex','Concious']
    def __init__(self,job,company):
        self.job = job
        self.company = company

    def getDetails(self):
        return self.job, self.company

class instructor:
    """ Instructor who teaches students"""
    def __init__(self,name,specialization):
        self.name = name
        self.specialization = specialization

    def getDetails(self):
        return self.name, self.specialization


class enquiry:
    """Enquiries for courses"""
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def getDetails(self):
        return self.name, self.course