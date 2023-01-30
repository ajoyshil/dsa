
def sub_array_index(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            print([i, j] )


def sub_array_index_k_len(A, k):
    for i in range(len(A)-k+1):
        print(i, i+k-1)


arr = [1,6,7,-2,0,-1,5]
# sub_array_index(arr)
sub_array_index_k_len(arr,3)
