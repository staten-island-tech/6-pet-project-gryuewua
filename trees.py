def tree(heights):
    greater = 1
    less = 1
    greaterf = 0
    lessf = 0
    for i in range(1,len(heights)):
        if heights[i] > heights[i-1]:
            greater += 1
        else:
            if greater > greaterf:
                greaterf = greater
            greater = 1

        if heights[i] < heights[i-1]:
            less += 1
            if less > lessf:
                lessf = less
            less = 1

    print (greaterf)
    print (lessf)

tree([2,1,4,6,8,2,9,5,2,3])


