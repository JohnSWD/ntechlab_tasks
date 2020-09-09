def findMaxSubArray(A):
    if len(A)==1:
        return A[0]
    curr_sum, result = A[0], A[0] # в curr_sum хранится текующая сумма подмассива, в result - наибольшая сумма подмассива
    for num in A[1:]: # начальные значения переменных учитывают первый элемент массива
        curr_sum += num
        if curr_sum < num: # если следующее число превышает имеющуюся сумму, начинаем считать сумму элементов нового подмассива
            curr_sum = num
        if result < curr_sum:
            result = curr_sum
    return result



if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(findMaxSubArray(A))