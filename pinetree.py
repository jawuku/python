# print pinetree

# use spaces and # to display tree
# and # trunk at the bottom


rows = input("How tall is your tree ? ")
rows = int (rows)

foliage = '#'
space = ' '

if (rows >= 1):
    for n in range(1, rows+1):
        left_space = rows - n
        tree = 2 * n - 1
        print((space*left_space)+(foliage*tree))

    # print trunk at the bottom
    print(((rows-1)*space)+foliage)

else:
    print('You have planted a seed.')