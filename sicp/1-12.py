
def pascal(row, column):
    if column > row:
        return 0
    elif column == 1:
        return 1
    else:
      return (pascal(row-1, column-1)) + pascal(row-1, column)


print pascal(1,1)
print pascal(3,2)
print pascal(5,3)
print pascal(5,4)
print pascal(4,4)
