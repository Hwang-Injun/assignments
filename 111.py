def assign1():
    a =list(map(int, input().split()))
    sum = 0
    avg = 0
    for i in a:
        sum = i + sum
        avg = sum/len(a)

    print(avg)


assign1()

def assign2():
    Word_list = ['scramble', 'kindly', 'do', 'learn']
    for i in range(len(Word_list)):
        Word_list[i] = 'un-' + Word_list[i]
    print(Word_list)

assign2()

def assign3():
    a =list(map(int, input().split()))
    sum = 0
    avg = 0
    for i in a:
        sum = i + sum
        avg = sum/len(a)
    if avg >= 60:
        print('Pass')
    else:
        print('Fail')

assign3()