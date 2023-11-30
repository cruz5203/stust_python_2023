# 學生類別
class Student:
    #建構子
    def __init__(self,school,department,departmentChair,grade,name,ID,mailingAddress,credits,scoreGPA):
        self.school=school # 學校
        self.department=department # 科系 
        self.grade=grade # 年級
        self.departmentChair=departmentChair # 系主任
        self.name=name #姓名
        self.ID=ID # 學號
        self.mailingAddress=mailingAddress #通訊地址
        self.credits=credits # 學分數(已取得)
        self.scoreGPA=scoreGPA # 成績GPA
    #儲存學校
    def set_school(self,school):
        self.school=school
    #取得學校
    def getschool(self):
        return self.school
    #儲存科系
    def set_department(self,department):
        self.department=department
    #取得科系
    def get_department(self):
        return self.department
    #儲存系主任
    def set_departmentChair(self,departmentChair):
        self.departmentChair=departmentChair
    #取得系主任
    def get_departmentChaird(self):
        return self.departmentChair
    #儲存姓名
    def set_name(self,name):
        self.name=name
    #取得姓名
    def get_name(self):
        return self.name
    #儲存ID
    def set_ID(self,ID):
        self.ID=ID
    #取得ID
    def get_ID(self):
        return self.ID
    #儲存通訊地址
    def set_mailingAddress(self,mailingAddress):
        self.mailingAddress=mailingAddress
    #取得通訊地址
    def get_mailingAddress(self):
        return self.mailingAddress
    #儲存年級
    def set_grade(self,grade):
        self.grade=grade
    #取得年級
    def get_grade(self):
        return self.grade
    #儲存學分數(已取得)
    def set_credits(self,credits):
        self.credits=credits
    #取得學分數
    def get_credits(self):
        return self.credits
    #儲存成績GPA
    def set_soreGPA(self,scoreGPA):
        self.scoreGPA=scoreGPA
    #取得成績GPA
    def get_scoreGPA(self):
        return self.scoreGPA
    #印出
    def show(self):
        print("學校名稱:{}".format(self.school))
        print("科系:{}".format(self.department))
        print("系主任:{}".format(self.departmentChair))
        print("年級:{}".format(self.grade))
        print("姓名:{}".format(self.name))
        print("學號:{}".format(self.ID))
        print("通訊地址:{}".format(self.mailingAddress))
        print("已取得學分數:{}".format(self.credits))
        print("成績GPA:{}".format(self.scoreGPA))

def main():
    student=Student("南台科大","資訊工程系","洪國鈞","四年級","陳冠霖","4A9G0122","台南市",100,4.0)
    student.show()
    student.set_credits(110)
    print("修改學分數為{}".format(student.get_credits()))
    student.show()
if __name__=="__main__":
    main()