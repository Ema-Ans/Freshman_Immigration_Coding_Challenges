def sizeof(n): #this function given an integer, returns the number of digits in that integer
    counter = 1
    n = abs(n)
    while (n//10 != 0):

        y = n//10
        n = y
        counter +=1

    return counter









def longestDigitRun(x):

    x = abs(x)
    copy = x
    if ( x - 10 < 0):
        return x
    maximum = 1
    counter = 1
    while (sizeof(x))>1:
        mod1 = x%10 #7 #3 #3
        x = x//10 #233 #23
        mod2 = x%10 #3 #3
        difference = mod1 - mod2

        if difference == 0:
            counter += 1
            if counter > maximum:
                maximum = counter
        else:
            counter = 1

    L = []
    x = copy
    counter = 1
    while (sizeof(x))>1:
        mod1 = x%10 #7 #3 #3
        x = x//10 #233 #23
        mod2 = x%10 #3 #3
        difference = mod1 - mod2

        if difference == 0:
            counter += 1
            if counter == maximum:
                L.append(mod1)
                print(L)
                L.sort()
        else:
            counter = 1
    if(L != []):
        return L[0]
    return ""


def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed.')

testLongestDigitRun()
