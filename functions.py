# def Afunction():
#     return "THis is a function"

# # New_function()
# # print('This is not a function')
# print(Afunction())
# print('Not a function')
#recursive function for fibonacci series
# def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1,10):
#     print(fibonacci(n))
# recursive infinite loop solution for fibonacci series

#using cache
cache_fibo={}
def fibonacci(n):
    #if we have a cache value then return it
    if n in cache_fibo:
        return cache_fibo[n]
    #compute the nth term
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        value=fibonacci(n-1) + fibonacci(n-2)
    #first of all cache the value and return 
    cache_fibo[n]=value
    return value 

for n in range(1,2000):
    print(fibonacci(n))