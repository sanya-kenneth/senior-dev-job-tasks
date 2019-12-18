import uuid
import pprint


teachers = [] # list to store teacher data
students = [] # list to store student data
questions = [] # list to store question data
quizes = [] # list to store quiz data
answers = [] # list to store answers provided by students

class BaseUser:
    """
    Base class for creating users in the system
    """
    def __init__(self, name, subject, user_class):
        self.id = 'usr'+str(uuid.uuid4())[24:]
        self.name = name
        self.subject = subject
        self.user_class = user_class


    def __str__(self):
        """
        Method returns a string representation of this class
        """
        return f'{self.name} obj'

    def save(self):
        """
        Method saves new user data to either the students list or
        teachers list depending on the type of user being created
        """
        if self.user_type == 'teacher':
            teachers.append(self.__dict__)
        else:
            students.append(self.__dict__)

class Teachers(BaseUser):
    """
    Class for adding teachers and managing teacher actions in
    the system
    """
    def __init__(self, name, subject, user_class):
        self.user_type = 'teacher'
        super().__init__(name, subject, user_class)

    def assign_quiz(self, student_id, quiz_id):
        """
        Method enables teachers to assign quizes to students
        """
        for student in students:
            if student["id"] == student_id:
                for quiz in quizes:
                    if quiz["quiz_id"] == quiz_id:
                        student["quizes_assigned"].append(quiz)

    @staticmethod
    def iterate_quiz_questions(quiz_id):
        """
        Method loops through a quiz and questions in that quiz
        
        return:
            A list of questions for a particular quiz
        """
        selected_quiz = [quiz for quiz in quizes if quiz["quiz_id"] == quiz_id]
        quiz_questions = [question["questions"] for question in selected_quiz]
        return quiz_questions[0]

    def grade_student(self, student_id, quiz_id):
        """
        Method enables teachers to grade students
        
        args:
            student_id : id of the student to be graded
            quiz_id : id of the quiz assigned to the student
        """
        correct_attempts = 0
        all_attempts = 0
        for attempt in answers:
            if attempt["student_id"] == student_id and\
                attempt["quiz_id"] == quiz_id:
                all_attempts += 1
                if attempt["is_correct"]:
                    correct_attempts += 1
        failed = all_attempts - correct_attempts
        total_quiz_qtns = Teachers.iterate_quiz_questions(quiz_id)
        unanswered = len(total_quiz_qtns) - all_attempts
        return {
            "passed": correct_attempts,
            "failed": failed,
            "unanswered_questions": unanswered,
            "final_grade": f"{correct_attempts}/{len(total_quiz_qtns)}"}


class Students(BaseUser):
    """
    Class for adding students in the system
    """
    def __init__(self, name, subject, user_class):
        self.user_type = 'student'
        self.quizes_assigned = []
        super().__init__(name, subject, user_class)


class Quizes:
    """
    Class for creating quizes in the system
    """
    def __init__(self, name, instructions, teacher_id):
        self.quiz_id = 'qz'+str(uuid.uuid4())[24:]
        self.name = name
        self.questions = []
        self.instructions = instructions
        self.teacher_id = teacher_id
        
    def save(self):
        """
        Method for adding a quiz to the quizes list store
        """
        quizes.append(self.__dict__)
        
    def add_question(self, question_id):
        """
        Method enables a teacher to add a question to a quiz
        """
        for question in questions:
            if question["question_id"] == question_id:
                self.questions.append(question)


class Questions:
    """
    class for creating questions in the system
    """
    def __init__(self, question, answer, teacher_id):
        self.question_id = 'qn'+str(uuid.uuid4())[24:]
        self.question = question
        self.answer = answer
        self.teacher_id = teacher_id
    
    def save(self):
        """
        Method for adding a question to the questions list
        """
        questions.append(self.__dict__)


class Answers:
    """
    class for creating answers to questions
    """

    @classmethod    
    def answer_qtn(cls, answer, quiz_id, question_id,
                   student_id):
        """
        Method enables students to answer a question
        """
        cls.answer_id = 'ans'+str(uuid.uuid4())[24:]
        for question in questions:
            if question["question_id"] == question_id:
                if question["answer"] == answer:
                    cls.is_correct = True
                else:
                    cls.is_correct = False
        answers.append({
            "answer_id": cls.answer_id,
            "answer": answer,
            "quiz_id": quiz_id,
            "question_id": question_id,
            "student_id": student_id,
            "is_correct": cls.is_correct
            })

   
def prt(input):
    """
    function for printing to the terminal using pprint
    """
    return pprint.pprint(input)

# t = Teachers('sanya', 'english', 'p2')
# t.save()
# s = Students("freshkid", "English", "p2")
# s.save()
# q = Questions("what is science", "b", t.id)
# q.save()
# q2 = Questions("Do you code?", "c", t.id)
# q2.save()
# q3 = Questions("Who are you?", "c", t.id)
# q3.save()
# prt(f"question::::   {q.question_id}  ")
# qz = Quizes("hide and seek", "play once", t.id)
# qz.save()
# # pprint.pprint(quizes)
# qz.add_question(q.question_id)
# qz.add_question(q2.question_id)
# qz.add_question(q3.question_id)
# prt(" ")
# # pprint.pprint(quizes)
# # pprint.pprint(teachers)
# # pprint.pprint(questions)
# # pprint.pprint(students)
# prt(" ")
# t.assign_quiz(s.id, qz.quiz_id)
# prt(students)
# prt(" ")
# Answers.answer_qtn("c", qz.quiz_id, q.question_id, s.id)
# Answers.answer_qtn("c", qz.quiz_id, q2.question_id, s.id)
# prt(answers)
# t.grade_student(s.id, qz.quiz_id)
# prt(t.grade_student(s.id, qz.quiz_id))
