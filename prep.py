'''
traversing the list in both directions 
left -> <- right with a while loop

traversing matrix by columns -> switch i and j matrix[j, i]
'''
from collections import defaultdict

grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

m = len(grid)
n = len(grid[0])
k = 3

for i in range(k):
    old = grid[0][0]
    last = grid[m-1][n-1]
    for i in range(m):
        for j in range(n):
            if i < m - 1:
                if j < n - 1:
                    new = grid[i][j + 1]
                    grid[i][j + 1] = old
                    old = new
                else: # element is in last column
                    new = grid[i + 1][0]
                    grid[i + 1][0] = old
                    old = new
            else: # last row
                if j < n - 1:
                    new = grid[i][j + 1]
                    grid[i][j + 1] = old
                    old = new
                else: # last element
                    grid[0][0] = last
        

# pozor

# def twoSum(nums, target):
#         already_checked = []
#         for i in range(len(nums)):
#             if i in already_checked:
#                 continue
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 if j in already_checked:
#                     continue
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#             already_checked.append(i)


heights = [1,8,6,2,5,4,8,3,7]

# distance to element = lastIndex - firstIndex

# brute force
def max_area(heigths):
    best = 0
    for i in range(len(heights)):
        for j in range(len(heights)):
            if j <= i: 
                continue

            height = min(heights[i], heights[j])
            length = abs(i - j)
            area = height * length
            
            if area > best:
                best = area

    return best

#print(max_area(heights))

def max_area_better(heigths):
    best = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        area = min(heights[left], heights[right]) * abs(left - right)

        if best < area:
            best = area
        
        if heights[left] < heights[right]:
            left += 1

        else: 
            right -= 1

    return best

#print(max_area_better(heights))

nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
        j = 0
        unique = len(seen)
        for key in seen:
            nums[j] = key
            j += 1
        
        for i in range(len(nums)):
            if i < unique: 
                continue
            else:
                nums[i] = "_"
        
        return unique, nums

#print(removeDuplicates(nums))

board =[
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

board = [[".",".","5",".",".",".",".",".","6"],
         [".",".",".",".","1","4",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".","9","2",".","."],
         ["5",".",".",".",".","2",".",".","."],
         [".",".",".",".",".",".",".","3","."],
         [".",".",".","5","4",".",".",".","."],
         ["3",".",".",".",".",".","4","2","."],
         [".",".",".","2","7",".","6",".","."]]

def isValidSudoku(board):
    
    # rows
    seen = {}
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                continue

            if board[i][j] not in seen:
                seen[board[i][j]] = True
            else:
                print("rows false")
                return False
        
        seen = {}

    # columns
    for i in range(9):
        for j in range(9):
            if board[j][i] == ".":
                continue

            if board[j][i] not in seen:
                seen[board[j][i]] = True
            else:
                print("cols false")
                return False
        seen = {}
    
    # sub-boxes
    def sub_box(start_i, end_i, start_j, end_j):
        seen = {}
        for i in range(start_i, end_i):  
            for j in range(start_j, end_j):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in seen:
                    seen[board[i][j]] = True
                else:
                    #print("box false: " + str(start_i) + " and " + str(end_i) + " / " + str(start_j) + " and " + str(end_j))
                    return False
        return True
    
    if not sub_box(0,3,0,3):
        return False

    if not sub_box(0,3,3,6):
        return False

    if not sub_box(0,3,6,9):
        return False

    if not sub_box(3,6,0,3):
        return False
    
    if not sub_box(3,6,3,6):
        return False
    
    if not sub_box(3,6,6,9):
        return False
    
    if not sub_box(6,9,0,3):
        return False
    
    if not sub_box(6,9,3,6):
        return False
    
    if not sub_box(6,9,6,9):
        return False
        
    return True

#print(isValidSudoku(board))

################################################################################################ 

# linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
        # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    
    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(elements) + " -> None"

        
        
list1 = LinkedList()
list1.insertAtEnd(1)
list1.insertAtEnd(3)
list1.insertAtEnd(5)

list2 = LinkedList()
list2.insertAtEnd(5)
list2.insertAtEnd(7)
list2.insertAtEnd(8)

#print(list1)
#print(list2)


def mergeTwoLists(list1, list2):
    dummy = Node(0)
    tail = dummy

    current_node1 = list1.head
    current_node2 = list2.head

    while current_node1 and current_node2:
        if current_node1.data < current_node2.data:
            tail.next = current_node1
            current_node1 = current_node1.next
        else:
            tail.next = current_node2
            current_node2 = current_node2.next
        tail = tail.next

    if current_node1:
        tail.next = current_node1
    elif current_node2:
        tail.next = current_node2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

#print(mergeTwoLists(list1, list2))

def longest_substring(s):
    substr_lengths = []
    substr = ""

    if len(s) == 1:
        return 1

    for i in range(len(s)):
        for char in s[i:]:
            if char not in substr:
                substr += char
            else:
                length = len(substr)
                substr_lengths.append(length)
                substr = ""
                break
    if len(substr_lengths) == 0:
        return 0

    return max(substr_lengths)


a = ""
b = "pwwkew"
#print(longest_substring(a))


s = "anagram"
t = "nagaram"

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    for char in t:
        if char in s_list:
            s_list.remove(char)
        else:
            return False
    return True


# def groupAnagrams(strs):
#     anagrams = []
#     remaining = list(strs)
#     same_anagrams = []
#     if len(strs) == 0:
#         return [[]]
    
#     if len(strs) == 1:
#         return[[strs]]

#     for i in range(len(strs)):
#         for word in strs[i:]: # + 1? 
#             print(strs[i],word)
#             if is_anagram(word, strs[i]) and word in remaining:
#                 same_anagrams.append(word)
#                 same_anagrams.append(strs[i])
#                 remaining.remove(word)
#         if same_anagrams != []:
#             anagrams.append(same_anagrams)
#         same_anagrams = []
#     final_list = []
#     for same_an in anagrams:
#         final_list.append(list(dict.fromkeys(same_an)))
#     return final_list

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
        
    return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["",""]
#print(groupAnagrams(strs))

def topKFrequent(nums, k):
    integers = {}
    for num in nums:
        if num not in integers:
            integers[num] = 1
        else:
            integers[num] += 1
    
    freq = []
    while k > 0:
        max = 0
        max_key = 0
        for key in integers:
            if integers.get(key) > max:
                max = integers.get(key)
                max_key = key
        print(max_key)
        integers.pop(max_key)
        freq.append(max_key)
        k -= 1
    return freq
    
nums = [1,1,1,2,2,3]
k = 2

#print(topKFrequent(nums, k))
strs = ["neet","code","love","you"]

# if there are no special characters like # for example
# def encode(strs):
#     single = ""
#     for s in strs:
#         single += s
#         single += "#"
#     return single

# def decode(s):
#     strs = []
#     j = 0
#     for i in range(len(s)):
#         if s[i] == "#":
#             strs.append(s[j:i])
#             j = i + 1

#     return strs

# if there can be special characters like # in the input strings

def encode(strs):
    single = ""
    for s in strs:
        single += str(len(s)) + "#" + s
    return single

def decode(s):
    strs = []
    i = 0
    while i < len(s):  
        j = i
        while s[j] != "#":
            j += 1
        
        length = int(s[i:j])
        i = j + 1 # j is at delimiter -> go past it by 1 index
        j = i + length
        strs.append(s[i:j])
        i = j
    return strs

#print(encode(strs))
#print(decode(encode(strs)))

# O(n^2)
# def product_except_self(nums):
#     product = []
#     for i in range(len(nums)):
#         single_prod = 1
#         for j in range(len(nums)):
#             if i == j:
#                 continue
#             else:
#                 if nums[j] == 0:
#                     single_prod = 0
#                     break
#                 single_prod *= nums[j]
#         product.append(single_prod)
#     return product


def product_except_self(nums):
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

nums = [0, 0]
#print(product_except_self(nums))

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

s = "Was it a car or a cat I saw?"

def isPalindrome(s):
        def remove_non_alphabetical(s):
            return ''.join([char for char in s if char.isalnum()])
        
        s = s.replace(" ", "").lower()
        s = remove_non_alphabetical(s)
        print(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

#print(isPalindrome(s))

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

numbers = [1,2,3,4]
target = 3
#print(twoSum(numbers, target))

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    res = []
    nums.sort()
    for i, n in enumerate(nums):
        
        if i > 0 and n == nums[i - 1]:
            continue

        if n > 0:
            break
                
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum = n + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else: # ==
                res.append([n, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


#print(threeSum(nums))

def trap(heights):
    area = 0
    l = 0
    r = 1

    while l < len(heights):
        
    
        
        






















