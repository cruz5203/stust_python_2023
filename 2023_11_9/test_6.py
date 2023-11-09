def sum_1_to_n(n):
    if n==1:
        return 1
    else:
        return sum_1_to_n(n-1)+n

def main():
    print(sum_1_to_n(10))

if __name__=="__main__":
    main()