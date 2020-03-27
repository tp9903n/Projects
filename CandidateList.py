# Code by Tomas Pires
class Candidate:
    """Creates a new candidate with the position they are applying for and their name"""
    def __init__(self, position, name):
        self.position = position
        self.name = name
        self.firstcount = 0
        self.secondcount = 0
        self.thirdcount = 0
        self.fourthcount = 0

    def increase_first(self):
        self.firstcount += 1
        return self.firstcount

    def increase_second(self):
        self.secondcount += 1
        return self.secondcount

    def increase_third(self):
        self.thirdcount += 1
        return self.thirdcount

    def increase_fourth(self):
        self.fourthcount += 1
        return self.fourthcount



# Code by Benjamin Hawkins
class President(Candidate):
    def __init__(self, position, name):
        Candidate.__init__(self, position, name)


class GSUOfficer(Candidate):
    def __init__(self, position, name):
        Candidate.__init__(self, position, name)


class FacultyOfficer(Candidate):
    def __init__(self, position, name, faculty):
        Candidate.__init__(self, position, name)
        self.faculty = faculty


class CandidateList:
    candidate_file = open('txt_files/GSUCandidates.txt', 'r')
    candidate_list = []

    # For every line in the GSUCandidates file create a new Candidate object
    for line in candidate_file:
        position, name = line.split(',')
        # Remove trailing newline character from each line in file
        name = name.rstrip()
        # Create objects dependent on position being applied for
        if position == "President":
            candidate_list.append(President(position, name))
        elif position == "GSU Officer":
            candidate_list.append(GSUOfficer(position, name))
        elif "Faculty" in position:
            if "FLAS" in position:
                candidate_list.append(FacultyOfficer("Faculty Officer", name, "FLAS"))
            elif "BUS" in position:
                candidate_list.append(FacultyOfficer("Faculty Officer", name, "BUS"))
            elif "FEH" in position:
                candidate_list.append(FacultyOfficer("Faculty Officer", name, "FEH"))
            elif "FES" in position:
                candidate_list.append(FacultyOfficer("Faculty Officer", name, "FES"))
    candidate_file.close()