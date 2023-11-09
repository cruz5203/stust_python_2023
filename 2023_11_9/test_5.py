def sum_add_5(a,b):
    def add(a,b):
        return a+b
    return add(a,b)+5

def main():
    print(sum_add_5(1,2))

if __name__=="__main__":
    main()