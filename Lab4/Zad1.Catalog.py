class NefuCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title

    def __repr__(self):
        return '{}'.format(self.title)


class CourseCatalog:
    def __init__(self, courses):
        self.courses = courses

    def courses_by_department(self, department_name):
        list_courses = []
        for course in courses:
            if course.department == department_name:
                list_courses.append(course)
        return list_courses

    def courses_by_search_term(self, search_snippet):
        list_courses = []
        for course in courses:
            if search_snippet.lower() in course.title.lower():
                list_courses.append(course)
        return list_courses


if __name__ == '__main__':
    cs106a = NefuCourse("CS", "106A", "Programming Methodology")
    cs106b = NefuCourse("CS", "106B", "Programming Abstractions")
    cs107 = NefuCourse("CjS", "107", "Computer Organzation and Systems")
    cs110 = NefuCourse("CS", "110", "Principles of Computer Systems")
    courses = [cs110, cs106a, cs107, cs106b]

    Course = CourseCatalog(courses)
    print(Course.courses_by_department("CS"))
    print(Course.courses_by_search_term("sys"))
