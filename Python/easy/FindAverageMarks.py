if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    target_person_list = student_marks[query_name]
    avg = sum(target_person_list) / len(target_person_list)
    
    print(f'{avg:.2f}')
    