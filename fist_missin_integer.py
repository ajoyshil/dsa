# f = open("abc.txt", "w")
# f.write("test")

def firstMissingPositive(A):
    try:
        n = len(A)
        visited = [0] * n
        s = 1
        for i in range(n):

            while n > A[i] >= 1 and A[i] != i+1:
                # if A[i] != i+1 and A[i] != A[i-1]:
                if A[A[i]+1] == A[i]:
                    continue
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
                temp = A[i]
                print(temp)

                # A[A[i]-1] = temp
                # A[A[i] - 1] = temp
                # A[i], A[A[i]-1] = A[A[i]-1], A[i]
                # A[i] = 1
                # visited[A[i]-1] = 1
        print(A)
    except Exception as e:
        print(e)


x = [3, 4, 5, -1]
x2 = [2, 2, -1, 1]


firstMissingPositive(x2)
