def twoSum(numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            else:
                left += 1
