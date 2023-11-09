def show_employee(name,employee=9000):
    print("姓名:{},工資:{}".format(name,employee))

def main():
    show_employee("Ben",12000)
    show_employee("Jessa")

if __name__=="__main__":
    main()
