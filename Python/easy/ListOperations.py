def main(n):
    l = []
    
    for i in range(n):
        inp = input()
        input_list = [val for val in inp.split()]
        if input_list[0] == 'insert':
            l.insert(int(input_list[1]),int(input_list[2]))
        elif input_list[0] == 'print':
            print(l)
        elif input_list[0] == 'remove':
            l.remove(int(input_list[1]))
        elif input_list[0] == 'append':
            l.append(int(input_list[1]))
        elif input_list[0] == 'sort':
            l.sort()
        elif input_list[0] == 'pop':
            l.pop()
        elif input_list[0] == 'reverse':
            l.reverse()
        else:
            pass
            
    return l



if __name__ == '__main__':
    N = int(input())
    main(N)
    
