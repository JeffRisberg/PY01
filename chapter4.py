def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After:  ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After:  ', arg)


a = 4

double(a)

print(a)

b = ['Alpha']

change(b)

print(b)