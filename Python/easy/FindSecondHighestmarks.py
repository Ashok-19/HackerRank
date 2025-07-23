if __name__ == '__main__':
    stud = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stud.update({name:score})
        
    sorted_stud = sorted(set(stud.values()))
    
    for i in sorted(stud):
        if stud[i] == sorted_stud[1]:
            print(i)
