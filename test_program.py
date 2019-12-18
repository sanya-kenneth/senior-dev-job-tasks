from main import *
import unittest


class ProgramTestCase(unittest.TestCase):
    """
    Testcase class for the program
    """
    def setUp(self):
        """
        Method to setup object instances at the beginning of each test
        """
        self.tr = Teachers("John", "english", "p3")
        self.std = Students("Ben", "english", "p3")
        self.quiz = Quizes("programing tested", "chose one answer",
                           self.tr.id)
        self.qn = Questions("Who is a developer?", "b", self.tr)

    def test_program_can_create_a_teacher(self):
        self.tr.save()
        self.assertIsInstance(teachers[0], dict)
        self.assertEqual(teachers[0]["name"], "John")
        self.assertEqual(teachers[0]["subject"], "english")

    def test_program_can_create_a_student(self):
        self.std.save()
        self.assertIsInstance(students[0], dict)
        self.assertEqual(students[0]["name"], "Ben")
    
    def test_teacher_can_create_quiz(self):
        self.quiz.save()
        self.assertEqual(quizes[0]["name"], "programing tested")
    
    def test_teacher_can_create_question(self):
        self.qn.save()
        self.assertIsInstance(questions[0], dict)
        self.assertEqual(questions[0]["question"], "Who is a developer?")
    
    def test_teacher_can_add_question_to_quiz(self):
        self.quiz.save()
        self.qn.save()
        self.quiz.add_question(self.qn.question_id)
        self.assertEqual(quizes[0]["questions"][0]["question"], "Who is a developer?")
    
    def test_teacher_can_assign_quiz(self):
        students.clear()
        self.std.save()
        self.tr.save()
        self.quiz.save()
        self.qn.save()
        self.tr.assign_quiz(self.std.id, self.quiz.quiz_id)
        self.assertEqual(students[0]["quizes_assigned"][0]["name"], "programing tested")

    def test_student_can_answer_quiz_question(self):
        self.qn.save()
        __args = ("b", self.quiz.quiz_id, self.qn.question_id,
                  self.std.id)
        Answers.answer_qtn(*__args)
        self.assertEqual(answers[0]["quiz_id"], self.quiz.quiz_id)
        self.assertEqual(answers[0]["answer"], "b")
        self.assertEqual(answers[0]["is_correct"], True)

    def test_teacher_can_grade_student(self):
        students.clear()
        questions.clear()
        answers.clear()
        quizes.clear()
        self.std.save()
        self.tr.save()
        self.qn.save()
        self.quiz.save()
        self.quiz.add_question(self.qn.question_id)
        __args = ("b", self.quiz.quiz_id, self.qn.question_id,
                  self.std.id)
        Answers.answer_qtn(*__args)
        grade_student = self.tr.grade_student(self.std.id, self.quiz.quiz_id)
        self.assertIsInstance(grade_student, dict)
        self.assertEqual(grade_student["failed"], 0)
        self.assertEqual(grade_student["passed"], 1)
        self.assertEqual(grade_student["final_grade"], "1/1")
        self.assertEqual(grade_student["unanswered_questions"], 0)
