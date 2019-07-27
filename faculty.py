class FacultyClass:
    faculty_list = []

    def __init__(self,faculty_name,faculty_id):
        self.faculty_name=faculty_name
        self.faculty_id=faculty_id
        self.books=[]

    def display(self):
        print(f"Faculty Name={self.faculty_name}.\nFaculty ID={self.faculty_id}.")
        for x in self.books:
            print("Book Issued is:-")
            print(x[0].title)