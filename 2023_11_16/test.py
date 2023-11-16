class My_Shap:
    side=0
    length=0
    eidth=0
    radius=0
    def __init__(self,side=0,length=0,eidth=0,radius=0):
        self.side=side
        self.length=length
        self.eidth=eidth
        self.radius=radius
    def square_area(self):
        return self.side*self.side
    def rectangle_area(self):
        return self.eidth*self.length
    def circle_area(self):
        return self.radius*self.radius*3.14

def main():
    shap=My_Shap(1,2,3,4)
    print(shap.square_area())
    print(shap.rectangle_area())
    print(shap.circle_area())

if __name__=="__main__":
    main()

