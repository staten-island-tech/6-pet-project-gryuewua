def tree(heights):
    greater = 1
    less = 1
    greaterf = 0
    lessf = 0
    for i in range(1,len(heights)):
        if (heights)[i] < (heights)[i-1]:
            greater += 1
            if less > lessf:
                lessf = less
            less = 0
        elif (heights)[i] < (heights)[i-1]:
            less += 1
            if greater > greaterf:
                greaterf = greater
            greater = 0
        else:
            if greater > greaterf:
                greaterf = greater
            elif less > lessf:
                lessf = less
            greater = 0
            less = 0

    print (greaterf)
    print (lessf)

tree([1,3,4,2])

