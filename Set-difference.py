# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n_eng=input()
    eng_stu=set(list(map(int, input().split())))
    n_french=input()
    french_stu=set(list(map(int, input().split())))
    diff=eng_stu.difference(french_stu)
    print(len(diff))
    
