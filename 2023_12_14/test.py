import json
class Student:
    def __init__(self,id,name='',major=''):
        self.name=name
        self.id=id
        self.major=major
        self.classes=[]

    def add_class(self,class_name):
        self.classes.append(class_name)

    def delete_class(self,class_name):
        self.classes.remove(class_name)

    def check_class(self):
        return self.classes

    def save_to_file(self):
        with open(self.id,'w') as file:
            data={}
            data["student_id"]=self.id
            data["name"]=self.name
            data["major"]=self.major
            data["classes"]=self.classes
            json.dump(data,file,indent=2)
    
    def load_to_file(self):
        jsonFile=open(self.id,'r')
        a=json.load(jsonFile)
        self.name=a['name']
        self.major=a['major']
        self.classes=a["classes"]



def main():
    student_1=Student("S001","A","資工")
    student_2=Student("D012","B","電機")
    student_1.add_class("資料庫")
    student_1.add_class("人工智慧")
    student_1.save_to_file()
    print(student_1.check_class())
    student_2.add_class("微處理機")
    student_2.add_class("工程數學")
    print(student_2.check_class())
    student_2.delete_class("微處理機")
    print(student_2.check_class())
    student_2.save_to_file()
    student_3=Student("D012")
    student_3.load_to_file()
    print(student_3.check_class())

if __name__=="__main__":
    main()
