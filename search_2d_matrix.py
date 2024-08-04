matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 10

def searchMatrix(matrix, target):
        for i, row in enumerate(matrix):
            l = 0
            r = len(matrix[0]) - 1
            mid = 0
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] < target:
                     l = mid + 1
                elif matrix[i][mid] > target:
                     r = mid - 1
                else:
                     return True
        return False

print(searchMatrix(matrix, target))