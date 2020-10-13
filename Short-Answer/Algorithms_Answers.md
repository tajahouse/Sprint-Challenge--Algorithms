#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)This algorithim is linear. It's number of operations depend on the size of the data directly. 


b) This algorithm is expential because of the nested loops which causes the function to increase as thte input size increases


c) This algorithm is also linear because it of the number of operations depending on the size of the data.

## Exercise II

Suppose you have a n-floor building and a lot of eggs. If the egg is dropped at f floor or higher, it will break. What floors can the egg be dropped from?

pivot = len(n) / 2
for f in range((pivot), len(n)):
    if at index of floor == "cracked":
    if at previous floor != "cracked":
        return f + 1
    else:
        return breaking_floor(n) - pivot
    elif at index of floor != "cracked":
    if at index of next floor == "cracked":
        return (f+1) +1
    else:
        return breaking_floor(n) - pivot
