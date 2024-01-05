
class University:
    '''
    Describes a University object with a name, location, motto, and date
    it was built.
    Instance attributes:
        name (str): name of the University
        location (str): location of the University
        motto (str): University's motto
        date (tuple): The day, month, and year the University was built
    Class attributes:
        None
    '''
    
    
    def __init__(self, name = 'University', location = 'Somewhere',
                 motto = 'Something', day = 1, month = 1, year = 2023):
        '''
        (str, str, str, int, int, int) -> None
        Constructs an object in class University with instance attributes
        name, location, Motto, and date (which is day, month, year)
        >>> ets = University('Ecole de technologie Superieure',
            'Montreal,Canada', 'Engineering for industry', 31, 1, 1974)
        >>> ets.name
        Ecole de technologie Superieure
        >>> ets.location
        Montreal,Canada
        >>> ets.motto
        Engineering for industry
        >>> ets.date
        (31, 1, 1974)
        >>> ets = University('Ecole de technologie Superieure',
            'Montreal,Canada', 'Engineering for industry', -31, 0, 1974)
        ValueError: ('All the values for day, month
                    and year should be positive')
        >>> unknown = University('Unknown', 'Ottawa,Canada')
        >>> unknown.name
        Unknown
        >>> unknown.location
        Ottawa,Canada
        >>> unknown.motto
        Something
        >>> unknown.date
        (1, 1, 2023)          
        '''
        if day <= 0 or month <= 0 or year <= 0:
            print('test')
            raise ValueError('All the values for day, month ' +
                            'and year should be positive')
        self.name = name
        self.location = location
        self.motto = motto
        self.date = (day, month, year)
        
        
    def __str__(self):
        '''
        () -> str
        Returns a string describing the University
        >>> mcGill = University('McGill', 'Montreal,Canada','By work, ' +
            'all things increase and grow', 31, 3, 1921)
        >>> print(mcGill)
        University of McGill was founded in (31, 3, 1921)
        Its main campus is located in Montreal,Canada
        Its Motto is: By work, all things increase and grow
        >>> unknown = University()
        >>> print(unknown)
        University of University was founded in (1, 1, 2023)
        Its main campus is located in Somewhere
        Its Motto is: Something
        >>> UOttawa = University('UOttawa', Ottawa,Canada', 'God is the
            lord of knowledge', 26, 9, 1848)
        >>> print(UOttawa)
        University of UOttawa was founded in (26, 9, 1848)
        Its main campus is located in Ottawa,Canada
        Its Motto is: God is the lord of knowledge
        
        '''
        return ('University of ' + self.name + ' was founded in '
        + str(self.date) + '\n' + 'Its main campus is located in '
        + self.location + '\n' + 'Its Motto is: ' + self.motto)
    

class JobPosition:
    '''
    Describes a JobPosition with a job_id and description of the position
    Instance attributes:
        job_id (int): stores identification number of the job
        description (str): a description of the job position
    Class attributes:
        id_description_dict (dict): a dictionary of id matching to the
        corresponding job description
    '''
    id_description_dict = {'Teaching Assistant': [0, 99],
                           'Professor': [100, 499],
                           'Faculty Lecturer': [500, 999],
                           'Department Chair': [1000, 1999],
                           'Dean': [2000, 2999],
                           'Vice Principal': [3000, 3999],
                           'Principal': [4000, 4000]}
    
    
    def id_to_description(self):
        '''
        () -> str
        Returns description based on job_ID following the class attribute
        dictionary id_description_dict
        >>> TA = JobPosition(80)
        >>> print(TA.description)
        Teaching Assistant
        >>> Faculty_Lecturer_A = JobPosition(999)
        >>> print(Faculty_Lecturer_A.description)
        Faculty Lecturer
        >>> the_principal = JobPosition(4000)
        >>> print(the_principal)
        Principal
        '''
        # Iterates through id_description_dict dictionary, if the job id is
        # in the key's list (between min and max values), then it will return
        # the corresponding key (job description string)
        for key in JobPosition.id_description_dict:
            if (self.job_id >= JobPosition.id_description_dict[key][0] and
                self.job_id <= JobPosition.id_description_dict[key][1]):
                return key
            
            
    def __init__(self, job_id):
        '''
        (int) -> None
        Constructs an object belonging to class JobPosition with a job_id and
        description
        >>> positionA = JobPosition(70)
        >>> print(positionA.job_id)
        70
        >>> print(positionA.description)
        Teaching Assistant
        >>> positionB = JobPosition(3999)
        >>> print(positionB.job_id)
        3999
        >>> print(positionB.description)
        Vice Principal
        >>> positionC = JobPosition(4000)
        >>> print(positionC.job_id)
        4000
        >>> print(positionC.description)
        Principal
        '''
        self.job_id = job_id
        self.description = self.id_to_description()
        
        
    def __str__(self):
        '''
        () -> str
        Returns the job description string of the job position
        >>> position1 = JobPosition(100)
        >>> print(position1)
        Professor
        >>> position2 = JobPosition(2567)
        >>> print(position2)
        Dean
        >>> position3 = JobPosition(1999)
        >>> print(position3)
        Department Chair
        '''
        return self.description
    
    
    def get_id(self):
        '''
        () -> int
        Returns job id of the job position
        >>> position1 = JobPosition(0)
        >>> position1.get_id()
        0
        >>> position2 = JobPosition(2566)
        >>> position2.get_id()
        2566
        >>> position3 = JobPosition(3999)
        >>> position3.get_id()
        3999
        '''
        return self.job_id
    
    
    def set_id(self, new_job_id):
        '''
        (int) -> None
        Modifies the job id and sets the corresponding description to the
        new job id
        >>> position1 = JobPosition(10)
        >>> position1.set_id(4000)
        >>> print(position1.job_id)
        4000
        >>> print(position1.description)
        Principal
        >>> position2 = JobPosition(3675)
        >>> position2.set_id(0)
        >>> print(position2.job_id)
        0
        >>> print(position2.description)
        Teaching Assistant
        >>> position3 = JobPosition(55)
        >>> position3.set_id(2500)
        >>> print(position3.job_id)
        2500
        >>> print(position3.description)
        Dean
        '''
        self.job_id = new_job_id
        self.description = self.id_to_description()
        
        
class Employee:
    '''
    Describes an Employee with a full name, unique ID, job position,
    and supervisor's reference number
    Instance attributes:
        first_name (str): stores employee's first name
        last_name (str): stores employee's last name
        ref (int): stores employee's unique ID number
        position (JobPosition): stores employee's job description & job id
        supervisor (int): stores supervisor's reference number
    Class attributes:
        nb_employee (int): stores the number of employees in the company
    '''
    nb_employee = 0


    def __init__(self, first_name = 'Employee', last_name = 'Employee',
                 reference = 0, job_id = 4000, sup_ref = -1):
        '''
        (str, str, int, int, int) -> None
        Constructs an object of class Employee with a first name, last name,
        reference number, job position, and supervisor reference number
        >>> e = Employee('Jack', 'Smith', 102, 4000, -1)
        >>> print(e.first_name)
        Jack
        >>> print(e.last_name)
        Smith
        >>> print(e.ref)
        102
        >>> print(e.position)
        Principal
        >>> print(e.supervisor)
        -1
        >>> e2 = Employee('Natasha', 'Armstrong', 56, 0, 7)
        >>> print(e2.first_name)
        Natasha
        >>> print(e2.last_name)
        Armstrong
        >>> print(e2.ref)
        56
        >>> print(e2.position)
        Teaching Assistant
        >>> print(e2.supervisor)
        7
        >>> e3 = Employee('Jill')
        >>> print(e3.first_name)
        Jill
        >>> print(e3.last_name)
        Employee
        >>> print(e3.ref)
        0
        >>> print(e3.position)
        Principal
        >>> print(e3.supervisor)
        -1
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.ref = reference
        self.position = JobPosition(job_id)
        self.supervisor = sup_ref
        Employee.nb_employee += 1
        
        
    def __str__(self):
        '''
        () -> str
        Returns a string containing employee's first and last name, with their
        job description
        >>> e = Employee('Jack', 'Jones', 50, 0, 5)
        >>> print(e)
        Jack Jones - Teaching Assistant
        >>> e2 = Employee()
        >>> print(e2)
        Employee Employee - Principal
        >>> e3 = Employee('Ian', 'Smith', 44, 2500, 4)
        >>> print(e3)
        Ian Smith - Dean
        '''
        return (self.first_name + ' ' + self.last_name + ' - '
        + self.position.description)
    
    
    def find_supervisor(self, employee_list):
        '''
        (list) -> Employee
        Finds and returns the employee's supervisor in employee_list, if
        the employee has no supervisor, it returns itself
        >>> e = Employee('Diana', 'Prince', 1127, 870, 3)
        >>> e1 = Employee('Guilia','Albertini',9,870,5)
        >>> e2 = Employee('Mathieu','Blanchette',3,1200,7)
        >>> e_list = [e1, e2]
        >>> supervisor = e.find_supervisor(e_list)
        >>> print(supervisor)
        Mathieu Blanchette - Department Chair
        >>> e = Employee('Jack', 'Smith', 599, 800, -1)
        >>> e1 = Employee('Jade', 'Ron', 34, 123, 6)
        >>> e2 = Employee('Hussaine', 'Bigen', 22, 11, 3)
        >>> e_list = [e1, e2]
        >>> supervisor = e.find_supervisor(e_list)
        >>> print(supervisor)
        Jack Smith - Faculty Lecturer
        >>> e = Employee('Lionel', 'Messi', 10, 200, 2)
        >>> e1 = Employee('Bruce', 'Wayne', 2, 145, 9)
        >>> e2 = Employee('Christiano', 'Ronaldo', 11, 588, 4)
        >>> e_list = [e1, e2]
        >>> supervisor = e.find_supervisor(e_list)
        >>> print(supervisor)
        Bruce Wayne - Professor
        '''
        if self.supervisor == -1:
            return self
        # If the employee's reference number in employee_list is the same as the
        # self employee's supervisor number, it will return that employee
        for employee in employee_list:
            if self.supervisor == employee.ref:
                return employee
            
            
    def __eq__(self, other_employee):
        '''
        (Employee) -> bool
        Returns True if both employees have the same first name, last name,
        and reference ID number. Returns False if any of the three parameters
        are not matching.
        >>> e = Employee('Jack', 'Smith', 10, 500, 1)
        >>> e2 = Employee('Jack', 'Smith', 10, 33, -1)
        >>> print(e == e2)
        True
        >>> e = Employee()
        >>> e2 = Employee('Employee', 'Employee', 0, 33, 5)
        >>> print(e == e2)
        True
        >>> e = Employee('Jill', 'Jones', 5, 500, -1)
        >>> e2 = Employee('Jill', 'Jones', 3, 500, -1)
        >>> print(e == e2)
        False
        
        '''
        if (self.first_name == other_employee.first_name and
            self.last_name == other_employee.last_name and
            self.ref == other_employee.ref):
            return True
        return False


class OrganizationalChart:
    '''
    Describes a university and its list of employees read from a file
    Instance attributes:
        university (University): stores university information
        employee_list (list): stores a list of employees
    Class attributes:
        None
    '''
    def load_chart(self, filename):
        '''
        (str) -> tuple
        Takes a filename and reads from it to return a tuple of a university
        object and list of employee objects
        >>> fobj = open('Mcgill_OrgChart.csv', 'r')
        >>> print(fobj.read())
        Name:,McGill
        Location:,Montreal,Canada
        Date :   ,31,3,1821
        Motto:,By work all things increase and grow
        Link:,https://www.mcgill.ca/orgchart/

        ID ,Title,Name,Supervisor
        1,4000,H.Deep Saini,-1,Principal 
        2,3500,Angela Campbell,1,Vice Principal
        3,2440,Bruce Lennox,2,Dean
        4,1100,Gregor Fussmann,3,Department Chair
        5,1200,Mathieu Blanchette,3,Department Chair
        6,150,Oana Balmau,5,Professor
        7,151,Jin Guo,5,Professor
        8,151,Christophe Dubach,5,Professor
        9,800,Guilia Albertini,5,Faculty Lecturer
        10,570,Faten Mhiri,5,Faculty Lecturer
        11,900,Joseph Vybihall,5,Faculty Lecturer
        12,870,Jacob Errington,5,Faculty Lecturer
        13,80,Saad Yousaf,10,Teaching Assistant
        14,50,MirHamed JafarzadehAsl,10,Teaching Assistant
        15,20,Neil Rahman,10,Teaching Assistant
        >>> test = OrganizationalChart('Mcgill_OrgChart.csv')
        >>> print(test.university)
        University of McGill was founded in (31, 3, 1821)
        Its main campus is located in Montreal,Canada
        Its Motto is: By work all things increase and grow
        >>> print(test.employee_list[0])
        H.Deep Saini - Principal
        >>> fobj = open('TestFile', 'r')
        >>> print(fobj.read())
        Traceback (most recent call last):
        File "/home/organizational_chart.py", line 523, in <module>
        fobj = open('Mcgill_OrgChart.cs', 'r')
        FileNotFoundError: [Errno 2] No such file or directory:
        'Mcgill_OrgChart.cs'
        >>> test = OrganizationalChart('Mcgill_OrgChart.cs')
        >>> print(test.university)
        File does not exist
        File does not exist
        University of University was founded in (1, 1, 2023)
        Its main campus is located in Somewhere
        Its Motto is: Something
        >>> print(test.employee_list[0])
        File does not exist
        File does not exist
        Employee Employee - Principal
        >>> fobj = open('OttawaU.csv', 'r')
        >>> print(fobj.read())
        Name:,OttawaU
        Location:,Ottawa,Canada
        Date :   ,21,4,1848
        Motto:,God is the lord of knowledge
        Link:,https://www.uottawa.ca/en

        ID ,Title,Name,Supervisor
        1,4000,Jacques Fremont,-1,Principal 
        2,3500,Jack Hughes,1,Vice Principal
        3,2440,Jerry Louie,2,Dean
        >>> OttawaU = OrganizationalChart('OttawaU.csv')
        >>> print(OttawaU.university)
        University of OttawaU was founded in (21, 4, 1848)
        Its main campus is located in Ottawa,Canada
        Its Motto is: God is the lord of knowledge
        >>> print(OttawaU.employee_list[0])
        Jacques Fremont - Principal
        '''
        try:
            fobj = open(filename, 'r')
            university_info = []
            employee_list = []

            # Reads from lines 1 to 4
            for i in range(4):
                line = fobj.readline()
                # Removes \n from the line, and makes a list for each word
                # between commas, then removes the first term and joins 
                # everything else into one string separated by commas.
                # This string is then added to the university_info list
                temp_list = line.strip('\n').split(',')
                temp_string = ','.join(temp_list[1:])
                university_info.append(temp_string)
            
            #Separates the date string into day, month, and year
            date = university_info[2].split(',')
            university = University(university_info[0], university_info[1],
                                    university_info[3], int(date[0]), 
                                    int(date[1]), int(date[2]))

            # Skips lines 5,6, and 7
            for i in range(3):
                fobj.readline()
            
            # Reads lines 8 to the end of the file
            for line in fobj:
                # The temp_list contains each variable (previously separated
                # by commas) in a list.
                # To construct an employee, ref number, job_id, and supervisor
                # number are converted to integers, and first_name and
                # last_name is split up (by the space) into two variables
                temp_list = line.strip('\n').split(',')
                employee = Employee(temp_list[2].split()[0],
                                    temp_list[2].split()[1], int(temp_list[0]),
                                    int(temp_list[1]), int(temp_list[3]))
                employee_list.append(employee)
            
            fobj.close()
            return university, employee_list
        
        except FileNotFoundError:
            print("File does not exist")
            return University(), [Employee()]
        
        except:
            print("There was an error with the file")
            return University(), [Employee()]
    
    
    def __init__(self, filename):
        '''
        (str) -> None
        Constructs an object of class OrganizationalChart with a university
        and list of employess
        >>> fobj = open('Mcgill_OrgChart.csv', 'r')
        >>> print(fobj.read())
        Name:,McGill
        Location:,Montreal,Canada
        Date :   ,31,3,1821
        Motto:,By work all things increase and grow
        Link:,https://www.mcgill.ca/orgchart/

        ID ,Title,Name,Supervisor
        1,4000,H.Deep Saini,-1,Principal 
        2,3500,Angela Campbell,1,Vice Principal
        3,2440,Bruce Lennox,2,Dean
        4,1100,Gregor Fussmann,3,Department Chair
        5,1200,Mathieu Blanchette,3,Department Chair
        6,150,Oana Balmau,5,Professor
        7,151,Jin Guo,5,Professor
        8,151,Christophe Dubach,5,Professor
        9,800,Guilia Albertini,5,Faculty Lecturer
        10,570,Faten Mhiri,5,Faculty Lecturer
        11,900,Joseph Vybihall,5,Faculty Lecturer
        12,870,Jacob Errington,5,Faculty Lecturer
        13,80,Saad Yousaf,10,Teaching Assistant
        14,50,MirHamed JafarzadehAsl,10,Teaching Assistant
        15,20,Neil Rahman,10,Teaching Assistant
        >>> test = OrganizationalChart('Mcgill_OrgChart.csv')
        >>> print(test.university)
        University of McGill was founded in (31, 3, 1821)
        Its main campus is located in Montreal,Canada
        Its Motto is: By work all things increase and grow
        >>> print(test.employee_list[10])
        Joseph Vybihall - Faculty Lecturer
        >>> fobj = open('OttawaU.csv', 'r')
        >>> print(fobj.read())
        Name:,OttawaU
        Location:,Ottawa,Canada
        Date :   ,21,4,1848
        Motto:,God is the lord of knowledge
        Link:,https://www.uottawa.ca/en

        ID ,Title,Name,Supervisor
        1,4000,Jacques Fremont,-1,Principal 
        2,3500,Jack Hughes,1,Vice Principal
        3,2440,Jerry Louie,2,Dean
        >>> OttawaU = OrganizationalChart('OttawaU.csv')
        >>> print(OttawaU.university)
        University of OttawaU was founded in (21, 4, 1848)
        Its main campus is located in Ottawa,Canada
        Its Motto is: God is the lord of knowledge
        >>> print(OttawaU.employee_list[2])
        Jerry Louie - Dean
        >>> fobj = open('Carleton.csv', 'r')
        >>> print(fobj.read())
        Name:,Carleton
        Location:,Ottawa,Canada
        Date :   ,11,6,1942
        Motto:,Ours the task eternal
        Link:,https://carleton.ca/

        ID ,Title,Name,Supervisor
        1,4000,Benoit Bacon,-1,Principal 
        2,3500,Joe Raunch,1,Vice Principal
        3,2440,Annabelle Groue,2,Teaching Assistant
        >>> Carleton = OrganizationalChart('Carleton.csv')
        >>> print(Carleton.university)
        University of Carleton was founded in (11, 6, 1942)
        Its main campus is located in Ottawa,Canada
        Its Motto is: Ours the task eternal
        >>> print(OttawaU.employee_list[2])
        Annabelle Groue - Teaching Assistant
        '''
        self.university = self.load_chart(filename)[0]
        self.employee_list = self.load_chart(filename)[1]
        
        
    def __str__(self):
        '''
        () -> str
        Returns a string of all the employees' info in the employee_list
        >>> fobj = open('OttawaU.csv', 'r')
        >>> print(fobj.read())
        Name:,OttawaU
        Location:,Ottawa,Canada
        Date :   ,21,4,1848
        Motto:,God is the lord of knowledge
        Link:,https://www.uottawa.ca/en

        ID ,Title,Name,Supervisor
        1,4000,Jacques Fremont,-1,Principal 
        2,3500,Jack Hughes,1,Vice Principal
        3,2440,Jerry Louie,2,Dean
        >>> OttawaU = OrganizationalChart('OttawaU.csv')
        >>> print(OttawaU)
        Jacques Fremont - Principal
        Jack Hughes - Vice Principal
        Jerry Louie - Dean
        '''
        employee_list_info = ''
        for employee in self.employee_list:
            employee_list_info += '\n' + employee.__str__()
        return employee_list_info
    
    
    def is_in_list(self, employee):
        '''
        (Employee) -> bool
        Returns True if employee is found in the employee_list, and False if not
        >>> fobj = open('Mcgill_OrgChart.csv', 'r')
        >>> print(fobj.read())
        Name:,McGill
        Location:,Montreal,Canada
        Date :   ,31,3,1821
        Motto:,By work all things increase and grow
        Link:,https://www.mcgill.ca/orgchart/

        ID ,Title,Name,Supervisor
        1,4000,H.Deep Saini,-1,Principal 
        2,3500,Angela Campbell,1,Vice Principal
        3,2440,Bruce Lennox,2,Dean
        4,1100,Gregor Fussmann,3,Department Chair
        5,1200,Mathieu Blanchette,3,Department Chair
        6,150,Oana Balmau,5,Professor
        7,151,Jin Guo,5,Professor
        8,151,Christophe Dubach,5,Professor
        9,800,Guilia Albertini,5,Faculty Lecturer
        10,570,Faten Mhiri,5,Faculty Lecturer
        11,900,Joseph Vybihall,5,Faculty Lecturer
        12,870,Jacob Errington,5,Faculty Lecturer
        13,80,Saad Yousaf,10,Teaching Assistant
        14,50,MirHamed JafarzadehAsl,10,Teaching Assistant
        15,20,Neil Rahman,10,Teaching Assistant
        >>> mcgill = OrganizationalChart('Mcgill_OrgChart.csv')
        >>> e1 = Employee('Gregor', 'Fussmann', 4, 1100, 3)
        >>> print(mcgill.is_in_list(e1))
        True
        >>> e2 = Employee('Gregor', 'Smith', 4, 1100, 3)
        >>> print(mcgill.is_in_list(e2))
        False
        >>> e3 = Employee('Gregor', 'Smith', 2, 1100, 3)
        >>> print(mcgill.is_in_list(e3))
        False
        '''
        for match_employee in self.employee_list:
            if employee == match_employee:
                return True
        return False
    
    
    def find_hierarchical_line(self, employee):
        '''
        (employee) -> list
        Returns a list of the hierarchical order of the employee in
        employee_list. Returns an empty list if employee is not in the
        employee_list
        >>> fobj = open('Mcgill_OrgChart.csv', 'r')
        >>> print(fobj.read())
        Name:,McGill
        Location:,Montreal,Canada
        Date :   ,31,3,1821
        Motto:,By work all things increase and grow
        Link:,https://www.mcgill.ca/orgchart/

        ID ,Title,Name,Supervisor
        1,4000,H.Deep Saini,-1,Principal 
        2,3500,Angela Campbell,1,Vice Principal
        3,2440,Bruce Lennox,2,Dean
        4,1100,Gregor Fussmann,3,Department Chair
        5,1200,Mathieu Blanchette,3,Department Chair
        6,150,Oana Balmau,5,Professor
        7,151,Jin Guo,5,Professor
        8,151,Christophe Dubach,5,Professor
        9,800,Guilia Albertini,5,Faculty Lecturer
        10,570,Faten Mhiri,5,Faculty Lecturer
        11,900,Joseph Vybihall,5,Faculty Lecturer
        12,870,Jacob Errington,5,Faculty Lecturer
        13,80,Saad Yousaf,10,Teaching Assistant
        14,50,MirHamed JafarzadehAsl,10,Teaching Assistant
        15,20,Neil Rahman,10,Teaching Assistant
        >>> mcgill = OrganizationalChart('Mcgill_OrgChart.csv')
        >>> e1 = Employee('Gregor', 'Fussmann', 4, 1100, 3)
        >>> print(mcgill.find_hierarchical_line(e1)[0])
        H.Deep Saini - Principal
        >>> print(mcgill.find_hierarchical_line(e1)[1])
        Angela Campbell - Vice Principal
        >>> print(mcgill.find_hierarchical_line(e1)[2])
        Bruce Lennox - Dean
        >>> print(mcgill.find_hierarchical_line(e1)[3])
        Gregor Fussmann - Department Chair
        '''
        hierarchical_line = [employee]
        supervisor = ''
        if not self.is_in_list(employee):
            return []
        # While the supervisor isn't the principal, it will keep adding the 
        # supervisors up the hierarchy to hierarchical_line
        while employee.supervisor != -1:
            supervisor = employee.find_supervisor(self.employee_list)
            hierarchical_line = [supervisor] + hierarchical_line
            employee = supervisor
        return hierarchical_line
    

    def print_hierarchical_line(self, employee):
        '''
        (Employee) -> None
        Prints the hierarchical_line of employees from the principal supervisor
        to the original input employee
        >>> fobj = open('Mcgill_OrgChart.csv', 'r')
        >>> print(fobj.read())
        Name:,McGill
        Location:,Montreal,Canada
        Date :   ,31,3,1821
        Motto:,By work all things increase and grow
        Link:,https://www.mcgill.ca/orgchart/

        ID ,Title,Name,Supervisor
        1,4000,H.Deep Saini,-1,Principal 
        2,3500,Angela Campbell,1,Vice Principal
        3,2440,Bruce Lennox,2,Dean
        4,1100,Gregor Fussmann,3,Department Chair
        5,1200,Mathieu Blanchette,3,Department Chair
        6,150,Oana Balmau,5,Professor
        7,151,Jin Guo,5,Professor
        8,151,Christophe Dubach,5,Professor
        9,800,Guilia Albertini,5,Faculty Lecturer
        10,570,Faten Mhiri,5,Faculty Lecturer
        11,900,Joseph Vybihall,5,Faculty Lecturer
        12,870,Jacob Errington,5,Faculty Lecturer
        13,80,Saad Yousaf,10,Teaching Assistant
        14,50,MirHamed JafarzadehAsl,10,Teaching Assistant
        15,20,Neil Rahman,10,Teaching Assistant
        >>> mcgill = OrganizationalChart('Mcgill_OrgChart.csv')
        >>> e1 = Employee('Gregor', 'Fussmann', 4, 1100, 3)
        >>> mcgill.print_hierarchical_line(e1)
        +-> H.Deep Saini - Principal
        | +-> Angela Campbell - Vice Principal
        | | +-> Bruce Lennox - Dean
        | | | +-> Gregor Fussmann - Department Chair
        '''
        hierarchical_line = self.find_hierarchical_line(employee)
        # The first employee in the hierarchy will only have the + -> to the 
        # left, and for the next employees, additional | will be added to the
        # + -> (based on index)
        for index in range(len(hierarchical_line)):
            print('| ' * index + '+->', hierarchical_line[index])
