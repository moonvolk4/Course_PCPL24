# departments.py
class Department:
    def __init__(self, id: int, name: str, salary: int, faculty_id: int):
        self.id = id
        self.name = name
        self.salary = salary
        self.faculty_id = faculty_id


class Faculty:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class FacultyDepartment:
    def __init__(self, department_id: int, faculty_id: int):
        self.department_id = department_id
        self.faculty_id = faculty_id


class DepartmentManager:
    def __init__(self, departments, faculties, faculty_departments):
        self.departments = departments
        self.faculties = faculties
        self.faculty_departments = faculty_departments

    def get_departments_starting_with_i(self):
        one_to_many = self._create_one_to_many()
        res = list(filter(lambda x: x[0].startswith('И'), one_to_many))
        return [(name, faculty) for name, _, faculty in res]

    def get_min_salary_by_faculty(self):
        one_to_many = self._create_one_to_many()
        result = []
        for fac in self.faculties:
            deps = list(filter(lambda x: x[2] == fac.name, one_to_many))
            if deps:
                min_salary = min(salary for _, salary, _ in deps)
                result.append((fac.name, min_salary))
        return sorted(result, key=lambda x: x[1])

    def get_sorted_departments_faculties(self):
        many_to_many = self._create_many_to_many()
        return sorted([(dep, fac) for dep, _, fac in many_to_many], key=lambda x: x[0])

    def _create_one_to_many(self):
        return [(dep.name, dep.salary, fac.name)
                for fac in self.faculties
                for dep in self.departments
                if dep.faculty_id == fac.id]

    def _create_many_to_many(self):
        many_to_many_temp = [(fac.name, fd.department_id)
                            for fac in self.faculties
                            for fd in self.faculty_departments
                            if fac.id == fd.faculty_id]

        return [(dep.name, dep.salary, fac_name)
                for fac_name, department_id in many_to_many_temp
                for dep in self.departments if dep.id == department_id]
