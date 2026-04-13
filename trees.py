def tree(heights):
    greater = 1
    less = 1
    greaterf = 0
    lessf = 0
    for i in range(1,len(heights)):
        if heights[i] > heights[i-1]:
            greater += 1
            if greater > greaterf:
                greaterf = greater
        else:
            if greater > greaterf:
                greaterf = greater
            greater = 1

        if heights[i] < heights[i-1]:
            less += 1
            if less > lessf:
                lessf = less
        else:
            if less > lessf:
                lessf = less
            less = 1

    print (greaterf)
    print (lessf)

tree([1,3,4,2])