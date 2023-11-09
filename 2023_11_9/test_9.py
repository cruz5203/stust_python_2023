def max_num(arr):
    max=0
    for i in arr:
        if max<i:
            max=i
    return max

def main():
    arr= [4, 6, 8, 24, 12, 2]
    print(max_num(arr))

if __name__=="__main__":
    main()