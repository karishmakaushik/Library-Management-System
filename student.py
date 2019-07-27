class StudentClass:
    student_list = []

    def __init__(self,student_name,year,branch,admission_id,std_roll):
        self.student_name=student_name
        self.year=year
        self.branch=branch
        self.admission_id=admission_id
        self.std_roll=std_roll
        self.books=[]

    def display(self):
        print(f"Student Name={self.student_name}.\nAddmision Year={self.year}.\nBranch={self.branch}.\nAddmission ID={self.admission_id}.\nRoll Number={self.std_roll}.")
        for x in self.books:
            print("Book Issued are:-")
            print(x.title)