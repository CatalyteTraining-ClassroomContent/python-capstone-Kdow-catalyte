

#learning management system


class Submission():

    def __init__(self, quizName, quizModule, quizScore,
                 studentId, studentName, submissionDate):
        self.quizName = quizName
        self.quizModule = quizModule
        self.quizScore = quizScore
        self.studentId = studentId
        self.studentName = studentName
        self.submissionDate = submissionDate



kendrick = Submission("quiz1", "module1", 100, 123, "Kendrick","9/15" )
john = Submission("quiz2", "module1", 80, 123, "John","9/15" )
mary = Submission("quiz1", "module2", 90, 123, "Mary","9/14" )
henry = Submission("quiz3", "module1", 85, 123, "Henry","9/12" )
karen = Submission("quiz2", "module1", 95, 123, "Karen","9/13" )

submission_list = [kendrick, john, mary, henry, karen]





def filter_by_date(submissionDate, submission_list):
    """

    Parameters: Date, List of objects

    Returns: list of objects with submissionDate
             equal to parameter date //or empty list

    """
    date_list = []
    for date in submission_list:
        if date.submissionDate == submissionDate:
            date_list += date

    return date_list
        



def filter_by_student_id(studentId, submission_list):
    """

    Parameters: StudentID, list of objects

    Returns: list of objects with matching student ID


    """
    id_list = []
    for id in submission_list:
        if id.studentId == studentId:
            id_list += id
    
    return id_list



#find_unsubmitted():
"""

Parameters: Date, list of student names, 
            list of submission objects

Returns: list of names of student that have
         not completed any quiz on that date

"""



#get_average_score():
"""

Parameters: list of submission objects

Returns: (float) average of all quiz scores

"""



#get_average_score_by_module():
"""

Parameters: list of submission objects

Returns:  an object 



"""







