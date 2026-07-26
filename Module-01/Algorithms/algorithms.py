# #qation No1
# #aste one 
# def getOnlyEvens(numbers):
#     result = []

#     for index, number in enumerate(numbers):
#         if index % 2 == 0 and number % 2 == 0:
#             result.append(number)

#     print(result)
# #test 1
# getOnlyEvens([1, 2, 3, 6, 4, 8])

# #Test 2
# getOnlyEvens([0, 1, 2, 3, 4])


#qation No2
# def reverseCompare(number):
#     tens = number // 10
#     ones = number % 10

#     reversed_number = ones * 10 + tens

#     if number > reversed_number:
#         print("Ok")
#     else:
#         print("Not ok")
#     #test    
# reverseCompare(72)
# reverseCompare(22)


#qation No3

def returnFactorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial
#Test 
print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))
                    

#qation No4
