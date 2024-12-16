# test_departments.py
import unittest
from departments import Department, Faculty, FacultyDepartment, DepartmentManager

class TestDepartmentManager(unittest.TestCase):
    def setUp(self):
        # Тестовые данные
        self.faculties = [
            Faculty(1, 'ИУ'),
            Faculty(2, 'МТ'),
            Faculty(3, 'ФН'),
        ]

        self.departments = [
            Department(1, 'ИУ-5', 90000, 1),
            Department(2, 'ИУ-7', 75000, 1),
            Department(3, 'МТ-3', 60000, 2),
            Department(4, 'ФН-4', 82000, 3),
        ]

        self.faculty_departments = [
            FacultyDepartment(1,1),
            FacultyDepartment(2,1),
            FacultyDepartment(3,2),
            FacultyDepartment(4,3),
        ]

        self.manager = DepartmentManager(self.departments, self.faculties, self.faculty_departments)

    def test_departments_starting_with_i(self):
        result = self.manager.get_departments_starting_with_i()
        expected = [('ИУ-5', 'ИУ'), ('ИУ-7', 'ИУ')]
        self.assertEqual(result, expected)

    def test_min_salary_by_faculty(self):
        result = self.manager.get_min_salary_by_faculty()
        expected = [('МТ', 60000), ('ИУ', 75000), ('ФН', 82000)]
        self.assertEqual(result, expected)

    def test_sorted_departments_faculties(self):
        result = self.manager.get_sorted_departments_faculties()
        expected = [('ИУ-5', 'ИУ'), ('ИУ-7', 'ИУ'), ('МТ-3', 'МТ'), ('ФН-4', 'ФН')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
