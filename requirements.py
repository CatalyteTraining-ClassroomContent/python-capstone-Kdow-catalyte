# learning management system


class Submission:

    def __init__(
        self, quizName, quizModule, quizScore, studentId, studentName, submissionDate
    ):
        self.quizName = quizName
        self.quizModule = quizModule
        self.quizScore = quizScore
        self.studentId = studentId
        self.studentName = studentName
        self.submissionDate = submissionDate


submission_list = [
    Submission("quiz1", "algebra", 100, 123, "Kendrick", "9/15"),
    Submission("quiz2", "algebra", 80, 300, "John", "9/15"),
    Submission("quiz1", "physics", 90, 129, "Mary", "9/14"),
    Submission("quiz3", "algebra", 85, 220, "Henry", "9/12"),
    Submission("quiz2", "calculus", 95, 290, "Karen", "9/13"),
    Submission("quiz2", "algebra", 100, 123, "Kendrick", "9/12"),
]


def filter_by_date(submissionDate, submissionList):
    """Filters submissions by specified date

    Parameters: submissionDate(string), submissionList (list of submission objects)

    Returns: date_list(list of objects with specified submissionDate)

    """
    date_list = []
    for date in submissionList:
        if date.submissionDate == submissionDate:
            date_list.append(date)

    return date_list


def filter_by_student_id(studentId, submissionList):
    """Filters submissions by specified student Id

    Parameters: StudentId(int), submissionList(list of submission objects)

    Returns: id_list(list of objects with matching student ID)


    """
    id_list = []
    for id in submissionList:
        if id.studentId == studentId:
            id_list.append(id)

    return id_list


def find_unsubmitted(submissionDate, nameList, submissionList):
    """Finds names of students who didnt submit on a specified day

    Parameters: submissionDate(string), nameList(list of student names),
                submissionList(list of submission objects)

    Returns: list of names of student that have
         not completed any quiz on that date

    """
    unsubmitted_list = nameList

    for name in submissionList:
        if name.studentName in nameList:
            if name.submissionDate == submissionDate:
                if name.studentName in unsubmitted_list:
                    unsubmitted_list.remove(name.studentName)

    return unsubmitted_list


def get_average_score(submission_list):
    """Returns average score of the list of submissions

    Parameters: submission_list(list of submission objects)

    Returns: (float) average of all quiz scores

    """
    total = 0
    for scores in submission_list:
        total += scores.quizScore

    return format(total / len(submission_list), ".1f")


def get_average_score_by_module(submission_list):
    """Gets average score of submissions by module name

    Parameters: submissions_list(list of submission objects)

    Returns:  module_dict (dictionary of module names with
            corresponding average score)

    """
    module_dict = {}

    for module in submission_list:
        if module.quizModule not in module_dict:
            module_list = []
            for match in submission_list:
                if match.quizModule == module.quizModule:
                    module_list.append(match)
            module_dict[module.quizModule] = get_average_score(module_list)

    return module_dict
