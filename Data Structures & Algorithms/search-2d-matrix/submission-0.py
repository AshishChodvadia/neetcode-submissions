class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[mid // cols][mid % cols]

            if target < val:
                r = mid - 1
            elif target > val:
                l = mid + 1
            else:
                return True

        return False

        '''
        for m in matrix:
            l = m[0]
            r = len(m) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if target < m[mid]:
                    r = mid - 1
                elif target > m[mid]:
                    l = mid + 1
                else:
                    return True
            return False
            '''
