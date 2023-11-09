def func1(*inf):
    for i in inf:
        print(i)

def main():
    func1(20,40,60)
    func1(80,100)

if __name__=="__main__":
    main()