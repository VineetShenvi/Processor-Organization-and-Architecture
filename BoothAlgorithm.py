def one_complement(s):
    ans = []
    for bit in s:
        if bit == '0':
            ans.append("1")
        else:
            ans.append("0")
    return ''.join(ans)    

def shift(s):
    ans= []
    ans.append(s[0])
    for bit in range(len(s)-1):
        ans.append(s[bit])
    Q_1 = ans[len(ans)-1]
    nbits = int((len(ans)-1)/2)
    A = ans[0:nbits]
    Q = ans[nbits: len(ans)-1]
    return ''.join(Q_1), ''.join(A), ''.join(Q)

def single_bit_addition(b0, b1, carry):
    sum = "0"
    if b0 == "0" and b1 == "0" and carry == "0":
        sum = "0"
        carry = "0"
    elif b0 == "0" and b1 == "1" and carry == "0":
        sum = "1"
        carry = "0"
    elif b0 == "1" and b1 == "0" and carry == "0":
        sum = "1"
        carry = "0"
    elif b0 == "1" and b1 == "1" and carry == "0":
        sum = "0"
        carry = "1"
    elif b0 == "0" and b1 == "0" and carry == "1":
        sum = "1"
        carry = "0"
    elif b0 == "0" and b1 == "1" and carry == "1":
        sum = "0"
        carry = "1"
    elif b0 == "1" and b1 == "0" and carry == "1":
        sum = "0"
        carry = "1"
    elif b0 == "1" and b1 == "1" and carry == "1":
        sum = "1"
        carry = "1"
    return sum, carry

def binaryaddition(a, b):
    carry = "0"
    ans = []

    for i in range(len(b)):
        ans.append("0")

    for i in reversed(range(len(b))):
        sum, carry = single_bit_addition(a[i], b[i], carry)
        ans[i] = sum
    return (''.join(ans))
        
def two_complement(s):
    one = []
    for i in range(len(s)-1):
        one.append("0")
    one.append("1")
    s = one_complement(s) 
    ans = binaryaddition(s, one)
    return ''.join(ans)

def boothalgorithm(M, Q):
    count = len(M)
    Q_1 = "0"
    A = []

    for i in range(len(M)):
        A.append("0")
    #print(A)
    for i in range(count):
        Q0 = str(Q[-1])
        if Q0 == "0" and Q_1 == "1":
            A = binaryaddition(A, M)
            Q_1, A, Q = shift(str(A)+str(Q)+str(Q_1))
        elif Q0 == "1" and Q_1 == "0":
            print(two_complement(M))
            A = binaryaddition(A, two_complement(M))
            Q_1, A, Q = shift(str(A)+str(Q)+str(Q_1))
        elif Q0 == "0" and Q_1 == "0":
            Q_1, A, Q = shift(str(A)+str(Q)+str(Q_1))
        elif Q0 == "1" and Q_1 == "1":
            Q_1, A, Q = shift(str(A)+str(Q)+str(Q_1))
    
    ans = ''.join(A) + ''.join(Q)
    #print(A)
    #print(Q)
    print(ans)
    return ans

def result(M, Q):
    s = boothalgorithm(M, Q)
    flag = 0
    if s[0] == "1":
        flag = 1
        s = two_complement(s)
    if flag == 1:
        return binary_to_decimal(s)*-1
    else:
        return binary_to_decimal(s)

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += (pow(2, (len(binary)-1)-i)*int(binary[i]))
    return decimal

def decimal_to_binary(decimal):
    binary = []
    flag = 0

    if decimal<0:
        flag = 1
        decimal = abs(decimal)
    while decimal>0:
        binary.append(str(decimal%2))
        decimal = decimal//2
    binary.append('0')
    print(binary)
    binary.reverse()
    if flag==1:
        binary = two_complement(binary)
    return list(binary)

def preprocessing(a,b):
    tup = (a, b) if (len(a)>len(b)) else (b, a)
    larger = tup[0]
    smaller = tup[1]
    diff = len(larger)-len(smaller)
    for i in range(diff):
        smaller.insert(1, '0')
    smaller = ''.join(smaller)
    larger = ''.join(larger)
    return smaller, larger

if __name__ == '__main__':
    print("Enter two numbers:")
    a = input()
    b = input()
    print(result(a, b))
