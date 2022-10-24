# Nhập số bất kì và in ra số đã nhập vào một mảng

def inputNumber():
    global n
    n= int (input( "Nhập số phần tử của mảng: "))

def appendNumber():
    lst = []
    for i in range(1,n+1):
        ele = int(input('Nhập phần tử thứ '+str(i)+':\n'))
        lst.append(ele)
    print (lst)

def main():
    inputNumber()
    appendNumber()
main()

# Nhập 2
# Input number 1: 3
# Input number 2: 5
# [ 3, 5]
