'''
-------------------------------------------------------------------------------
Name: Alexander Farouz
Assignment: PA 3
Due Date: 9/26/22
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
-------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions about the #
meaning of the specification. You can write in N/A if you don’t have any
comments/assumptions.
-------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
10 20 30 40 50 60 70 80
-------------------------------------------------------------------------------
'''

'''
The following block of code determines the amount of factors for a specific
number, and divides said number by the amount of factors the number has.
'''
def composite_ratio(the_num):
    
    factors = 0
    i = 1
    '''
    The while loop determines whether the variable 'i' is less or equal
    to the given number, and as long as it is, the following if statement
    commences. The if statement asks if the given number divided by 'i' can
    be divided with no remainder. If the statement is true, 1 is added to
    the variable 'factors'.
    '''
    while i <= the_num:
        
        if the_num % i == 0:
            
            '''
            After the if statement (still in the while loop) there is a
            counter, which adds 1 to 'i', and gets tested in the while loop
            again.
            '''
            factors += 1
        '''
        After the if statement (still in the while loop) there is a counter,
        which adds 1 to 'i', and gets tested in the while loop again.
        '''
        i += 1     
    '''
    The final value returns the original given number by the amount of
    factors
    '''
    return float(the_num/factors)

'''
The following block of code takes 2 numbers, a starting point (bottom) and
a maximum value (top). Along with these two numbers, there is a counter
(initially = 1). This counter is initially added to the staring point,
and stored in the variable 'b'. Variable 'b' is then added to the counter
which increments by 1 each time, and each time the counter adds to 'b',
it is stored in 'b' again.
'''
def add_em_up(bottom, top):
    
    
    b = bottom
    t = top
    count = 1

    '''
    The while loop is essential because it stops once 'b' exceeds the maximum
    value. The if statement is there to determine whether to add 1 to the
    counter. This if statement also has the same condition as the while
    statement, but since it is in the while statement it repeats as long as
    the while statement is true.
    '''
    while b <= t:
        b += count
      
        if b <= t:
            count += 1
    '''
    The value returned is the count - 1 because the initial value of count
    is 1. This is the case because in the initial addition to the
    starting value, the counter always adds 1 rather than 0, so it  must be
    accounted for when returned at the end.
    '''
    return count - 1

'''
The following block of code determines the vowel which repeats the most
in a given list of strings, regardless of the letter case.
'''
def vowels_count(letters):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    '''
    The for loop takes the range of the length of the given list and
    stores each string in the variable 'v_check' which goes through each
    string in the given list. The first if statement in the for loop
    checks if 'v_check' is in the 'vowel' list which is defined above.
    the 'vowel' list contains all vowels, upper and lower case, in
    order for the program to be case insensitive.
    '''
    for x in range(len(letters)):
        v_check = letters[x]
        
        if v_check in vowel:
            
            '''
            The if/elifs under the if statement in the for loop only
            executes when 'v_check' is a vowel. there are 5 if/elifs,
            one for each vowel. For example, if 'v_check' is 'a' or 'A',
            1 is added to the counter for the vowel 'a'. The same is
            done for the rest of the vowels.
            '''
            if v_check == 'a' or v_check == 'A':
                a += 1
            
            elif v_check == 'e' or v_check == 'E':
                e += 1
                
            elif v_check == 'i' or v_check == 'I':
                i += 1
                
            elif v_check == 'o' or v_check == 'O':
                o += 1
            
            elif v_check == 'u' or v_check == 'U':
                u += 1
    '''
    After the for loop, there is another set of 5 if/elifs. Each one
    represents a different vowel, which tests them against each other.
    If a certian vowel counter is determined to be the most, the vowel
    gets printed along with the amount of times the vowel appears in the
    initial list
    '''
    if a > e and a > i and a > o and a > u:
        return 'Most Frequent: \'a\' Count: ' + str(a)
    elif e > a and e > i and e > o and e > u:
        return 'Most Frequent: \'e\' Count: ' + str(e)
    elif i > a and i > e and i > o and i > u:
        return 'Most Frequent: \'i\' Count: ' + str(i)
    elif o > a and o > e and o > i and o > u:
        return 'Most Frequent: \'o\' Count: ' + str(o)
    elif u > a and u > e and u > i and u > o:
        return 'Most Frequent: \'u\' Count: ' + str(u)

'''
The following block of code takes two lists, f_list which contains
factors, and big_list, the numbers which potentially contain the
factors.
'''
def wacky_factors(f_list, big_list):
    
    total_factors = 0
    
    '''
    The first for loop takes the numbers in big_list and goes through
    each one. The for loop inside the first for loop takes the numbers
    from f_list and goes through each number in the first for
    loop (numbers in big_list) and checks if the number contains the
    number in f_list as a factor.
    '''
    for i in range(len(big_list)):
        num = big_list[i]
        
        for j in range(len(f_list)):
            factor = f_list[j]
            
            '''
            The if statement checks if the number in big_list (num)
            can be divided by the number in f_list (factor) without
            any remainder. If this statement is true, 1 is added to the
            total amount of factors.
            '''
            if num % factor == 0:
                total_factors += 1
    
    return total_factors
    
    
    