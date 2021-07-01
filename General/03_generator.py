
'''What is generator ? Explain Advantages. Write a generator for fibonacci series'''

'''
Python provides a generator to create your own iterator function. A generator is a special type of function
which does not return a single value, instead, it returns an iterator object with a sequence of values. 
In a generator function, a yield statement is used rather than a return statement.
'''

   ## Advantages
'''
1. Very easy to use
2. Memory utilization improved
3. Performance will be improved
4. Best suitables for reading data from large number of file
5. web scraping and crawling

'''

    #### WAP for fabonacci series using generator ####

def fab():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

f=fab()
for x in f:
    if x>100:
        break
    print(x)