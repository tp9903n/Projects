from CandidateList import CandidateList

vote_file = open("txt_files/Votes.txt", "r")


for line in vote_file:
    name, position, preference = line.split(",")
    preference = preference.strip('\n')

    for n in CandidateList.candidate_list:
        if n.name == name:
            if preference == "first":
                n.increase_first()
            if preference == "second":
                n.increase_second()
            if preference == "third":
                n.increase_third()
            if preference == "fourth":
                n.increase_fourth()


def win_count(role, department=None):
    """Method determines who the winner is for each role"""
    pres_list = []
    gsu_list = []
    flas_list = []
    bus_list = []
    feh_list = []
    fes_list = []
    current_list = []

    for candidate in CandidateList.candidate_list:
        if candidate.position == "President":
            pres_list.append(candidate)
        elif candidate.position == "GSU Officer":
            gsu_list.append(candidate)
        elif "Faculty" in candidate.position:
            if "FLAS" in candidate.faculty:
                flas_list.append(candidate)
            elif "BUS" in candidate.faculty:
                bus_list.append(candidate)
            elif "FEH" in candidate.faculty:
                feh_list.append(candidate)
            elif "FES" in candidate.faculty:
                fes_list.append(candidate)

    if department is not None:
        if "FLAS" in department:
            current_list = flas_list
        elif "BUS" in department:
            current_list = bus_list
        elif "FEH" in department:
            current_list = feh_list
        elif "FES" in department:
            current_list = fes_list
    else:
        if role == "President":
            current_list = pres_list
        elif role == "GSU Officer":
            current_list = gsu_list

    sorted_can_first = sorted(current_list, key=lambda candidates: candidates.firstcount, reverse=True)
    sorted_can_second = sorted(current_list, key=lambda candidates: candidates.secondcount, reverse=True)
    sorted_can_third = sorted(current_list, key=lambda candidates: candidates.thirdcount, reverse=True)
    sorted_can_fourth = sorted(current_list, key=lambda candidates: candidates.fourthcount, reverse=True)
    print(sorted_can_first[0].name, sorted_can_first[0].firstcount)

    if sorted_can_first[0].firstcount == sorted_can_first[1].firstcount:
        if sorted_can_second[0].secondcount == sorted_can_second[1].secondcount and sorted_can_second[0].name == sorted_can_first[0].name:

            if sorted_can_third[0].thirdcount == sorted_can_third[1].thirdcount:
                if sorted_can_fourth[0].fourthcount == sorted_can_fourth[1]:
                    print("No winner")
    else:
        winning_candidate = sorted_can_first[0].name
        print(winning_candidate)
        return winning_candidate


win_count("President")
win_count("GSU Officer")
win_count("Faculty Officer", "FLAS")
win_count("Faculty Officer", "BUS")
#win_count("Faculty Officer", "FEH")
#win_count("Faculty Officer", "FES")