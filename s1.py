# txt = "I Love Python"
# txt = txt.split()
# print("[ Susseccfully ]") if txt[1] == "Love1" else print("[ Error ]")
# print(txt)

# print("<>" * 25)

# number =  [90,95]
# number2 = [90,95]
# x = []
# for mynum in number:
#     for mynum2 in number2:
#         if mynum == mynum2:
#             x.append(mynum)
#             x.append(mynum2)



# from typing import List
# def getBiggestShared(a: List[int], b: List[int]) -> int:
#     # write your code here ^_^
#     x = []
#     for mynum in a:
#         for mynum2 in b:
#             if mynum == mynum2:
#                 x.append(mynum)
#                 x.append(mynum2) if mynum == mynum2 else None
#     if a == b and len(a:
#         return (x[0]) if x[0] > x[1] else  (x[2])
#     else:
#          return (x[0]) if x[0] > x[1] else (x[1])


# print(getBiggestShared([0] , [0]))


# from typing import List
# def isEmail(email: str) -> bool:
#     # write your code here ^_^
#     if "@" and "." in email:
#         if email.startswith(email.__str__()):
#             if len(email[0:email.index("@")]) > 0:
#                 if email.count("@") == 1:
#                     if len(email[email.index("@"):email.index(".")]) > 0:
#                         if len(email[email.index("."):]) > 2:
#                             return True
#                         else:
#                             return False
#                     else:
#                         return False
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False


# print(isEmail('@example.com'))



# from typing import List
# def arrowDuplicates(word: str) -> str:
#     # write your code here ^_^
#     x = word.lower()
#     xres = ""
#     for i in word.lower():
#         if x.count(i)  > 1:
#             xres = xres + "<"
#         else:
#             xres = xres + ">"
#     return xres


# print(arrowDuplicates('Ahmad'))

# from typing import List
# def sub_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
#     # write your code here ^_^
#     for ar1 in arr1:
#         print(ar1)
#         for ar2 in arr2:
#             print(ar2)

# print(sub_arrays([2,4,88], [4,2,88]))

# from typing import List
# def namesSort(namesArray: List[str], order: str) -> List[str]:
#     # write your code here ^_^
#     if order == "ASC":
#         namesArray.sort(reverse = False)
#         return namesArray
#     elif order == "DESC":
#         namesArray.sort(reverse = True)
#         return namesArray
# print(namesSort([], 'ASC'))


# li = 'Ahmed OmarYousef Abdullah'
# print(li.s)

# words = ["Geeks", "For", "Geeks"]
 
# # Sorting list of strings
# words.sort(reverse=True)
 
# print(words)

# from typing import List
# def kSumSubset(numArray: List[int], k: int) -> bool:
#     # write your code here ^_^
#     listnum = []
#     for i in numArray:
#         for x in numArray:
#             result = i + x
#             listnum.append(result)
#     for res in listnum:
#         if res == k:
#             res2 = res
#             listnum.remove(res)
#         else:
#             res2 = 0
#             print(res2)
#     return True if res2 == k else False
#     # if res == k:
#     #     return True
#     # else:
#     #     return False
# print(kSumSubset([7,3,2,5,8], 14))


# from typing import List
# def sortByLength(txt: str) -> str:
#     # write your code here ^_^
#     x = txt.split()
#     x.sort()
#     return x




# print(sortByLength('I see you Ahmed'))


# from typing import List
# def removeSpecialCharacters(strParam: str) -> str:
#     # write your code here ^_^
#     a = ""
#     for i in strParam:
#         if "$" == i:
#             continue
#         elif "!" == i:
#             continue
#         elif "@" == i:
#             continue
#         elif "#" == i:
#             continue
#         elif "," == i:
#             continue
#         elif "." == i:
#             continue
#         elif "%" == i:
#             continue
#         elif "^" == i:
#             continue
#         elif "?" == i:
#             continue
#         else:
#             a = a + i
#     return a
    # "$" or "!" or "،" or "@" or "#" or "," or "."

# print(removeSpecialCharacters( 'Hi-How-are-you?'))

# from typing import List
# def kSumSubset(numArray: List[int], k: int) -> bool:
#     # write your code here ^_^
#     Count = 1
#     for i in numArray:
#         for x in numArray:
#             for y in numArray:
#                 print(f"{i} + {x} + {y} =>>> {i + x + y}")
#                 print("\n")
#         else:
#             print(f"Finished This Listcv\n")
        


                





# print(kSumSubset([1,2,3] , 1))




#     xlist = []
#     for i in numArray:
#         for x in numArray:
#             xlist.append(i + x)
#     return k in xlist


# from typing import List
# def word_length(arr: List[str]) -> List[int]:
#     # write your code here ^_^
#     xlist = []
#     for i in arr:
#         xlist.append(len(i))
#     return xlist
        

# print(word_length(['Code','hub']))

# from typing import List
# def unique(arr: List[int]) -> List[int]:
#     # write your code here ^_^
#     xlist = []
#     for i in arr:
#         if arr.count(i) > 1:
#             continue
#         else:
#             xlist.append(i)
#     return xlist
# print(unique([3,2,6,2]))

# from typing import List
# def max_element(arr: List[int]) -> int:
#     # write your code here ^_^
#     return max(arr)
# print(max_element([1,2,3,4,5,1000]))



# from typing import List
# def cumulative_sum(arr: List[int]) -> List[int]:
#     # write your code here ^_^
#     for i in arr:
#         for x in arr:
#             print(i,x)

# print(cumulative_sum())

# from typing import List
# def hasSpace(strParam: str) -> str:
#     # write your code here ^_^
#     return strParam.replace(" ", "#")

# print(hasSpace('Ahmed   '))

# from typing import List
# def date_formating(date: str) -> str:
#     # write your code here ^_^
#     data = date.split("-")
#     return f"{data[2]}-{data[1]}-{data[0]}"

# print(date_formating( '2020-01-01'))

# from typing import List
# def longestZero(strParam: str) -> str:
#     # write your code here ^_^
#     str1 = ''
#     for i in strParam:
#         str1 = str1 + i if strParam.count('0') > 1 else None
#     return str1
# print(longestZero("1010000"))

# from typing import List
# def kS(arr1: List[int],arr2: List[int]) -> int:
#     res = []
#     for x in arr1:
#         res.append(x) if arr2.count(x) > 0 else None
#     return max(res)

# print(kS([10,2,3,12,3],  [10,2,3,12,3]))

# from typing import List
# def kSumSubset(dateString: str) -> bool:
#     # write your code here ^_^
#     return True if int(dateString.split("-")[0]) > 1882 and int(dateString.split("-")[0]) < 2019 and dateString.split("-")[2] != 1 else False
# print(kSumSubset('3020-01-01T00:00:00'))

# from typing import List
# def numbers_range(number: int) -> str:
#     s = ''
#     for x in range(number + 1):
#         s = s + str(x) + '  '
#     s = s[:-2]
#     print(s)
#     s = s.split("  ").sort()
#     return (s)
#     return s[::-1]
# print(numbers_range(10))

# from typing import List
# def match_arrays(array1: List[str], array2: List[str]) -> bool:
#     # write your code here ^_^
#     xlist = []
#     for i in array1:
#         xlist.append(i) if array2.count(i) > 0 else None
#     return True if len(xlist) == len(array2) else False
# print(match_arrays(['word2','there','hello'], ['hello','there','word2']))

# from typing import List
# def replaceThe(txt: str) -> str:
#     # write your code here ^_^
#     return txt.replace("the" , "an") if txt[txt.index('the') + 4] == 'a' or txt[txt.index('the') + 4] == 'e' or txt[txt.index('the') + 4] == 'i' or txt[txt.index('the') + 4] == 'o' else txt.replace('the', 'a')
# print(replaceThe('I want the orange'))

# import random

# Q1 = ['5 x 6', '30']
# Q2 = ['9 x 9', '81']
# Q3 = ['7 x 8', '56']
# All_Q = [Q1, Q2, Q3]
# Count = 0
# def Check(Q):
#     print(Q[0])
#     user_a = input('Enter The Answer >> ').strip()
#     if user_a == Q[1]:
#         global Count
#         Count += 1

# for i in range(len(All_Q)):
#     QQ = random.choice(All_Q)
#     Check(QQ)
#     All_Q.remove(QQ)

# if len(All_Q) == 0:

#     print(f'Your Points is [{Count}]')


# import random

# SlS = ['stone', 'leaf', 'scissors']

# while True:
#     Game = random.choice(SlS)
#     Start = input('Choice [stone , leaf , scissors] >> ')
#     if Start == Game:
#         print(f'{Start} == {Game}')
#     elif Game == 'stone' and Start == 'scissors':
#         print(f'{Game} > {Start }\n Your Lose')
#     elif Start == 'stone' and Game == 'scissors':
#         print(f'{Start} > {Game}\n Your Win')
#     elif Game == 'leaf' and Start == 'stone':
#         print(f'{Game} > {Start }\n Your Lose')
#     elif Start == 'leaf' and Game == 'stone':
#         print(f'{Start} > {Game}\n Your Win')
#     elif Game == 'scissors' and Start == 'leaf':
#         print(f'{Game} > {Start }\n Your Lose')
#     elif Start == 'scissors' and Game == 'leaf':
#         print(f'{Start} > {Game}\n Your Win')
#     else:
#         print('Error Choise !')


# user = input('Enter To Tranlate To My Languege >> ')

# WordTrans = ''
# #  a b c d e f g h i j k l m n o p q r s t u v w x y z
# for i in user:
#     i = i.lower()
#     if i == 'a':
#         WordTrans += 'N9'
#     elif i == 'b':
#         WordTrans += 'b2'
#     elif i == 'c':
#         WordTrans += 'OC'
#     elif i == 'd':
#         WordTrans += 'Q1'
#     elif i == 'e':
#         WordTrans += '33'
#     elif i == 'f':
#         WordTrans += 'G1'
#     elif i == 'g':
#         WordTrans += '81'
#     elif i == 'h':
#         WordTrans += 'Z8'
#     elif i == 'i':
#         WordTrans += 'A0'
#     elif i == 'j':
#         WordTrans += 'AE'
#     elif i == 'k':
#         WordTrans += 'EN'
#     elif i == 'l':
#         WordTrans += 'QO'
#     elif i == 'm':
#         WordTrans += 'VP'
#     elif i == 'n':
#         WordTrans += 'X6'
#     elif i == 'o':
#         WordTrans += 'FU'
#     elif i == 'p':
#         WordTrans += 'D2'
#     elif i == 'q':
#         WordTrans += 'ST'
#     elif i == 'r':
#         WordTrans += 'K6'
#     elif i == 's':
#         WordTrans += 'L2'
#     elif i == 't':
#         WordTrans += 'W8'
#     elif i == 'u':
#         WordTrans += 'V4'
#     elif i == 'v':
#         WordTrans += 'YI'
#     elif i == 'w':
#         WordTrans += 'D6'
#     elif i == 'x':
#         WordTrans += 'K9'
#     elif i == 'y':
#         WordTrans += 'MC'
#     elif i == 'z':
#         WordTrans += 'XX'
#     elif i == ' ':
#         WordTrans += 'GH4NX'

# print(WordTrans)

# # # # # #
# WordTrans = ''
# user_a = input('Enter >> ')

# us = ''
# c = 0 
# for _ in user_a:
#     us += _
#     if c == 1:
#         us += '\n'
#         c -= 1
#     else:
#         c += 1
# print(us)
# for i in us.split('\n'):
#     i = i.upper()
#     if i == 'N9':
#         WordTrans += 'a'
#     elif i == 'b2':
#         WordTrans += 'b'
#     elif i == 'OC':
#         WordTrans += 'c'
#     elif i == 'Q1':
#         WordTrans += 'd'
#     elif i == '33':
#         WordTrans += 'e'
#     elif i == 'G1':
#         WordTrans += 'f'
#     elif i == '81':
#         WordTrans += 'g'
#     elif i == 'Z8':
#         WordTrans += 'h'
#     elif i == 'A0':
#         WordTrans += 'i'
#     elif i == 'AE':
#         WordTrans += 'j'
#     elif i == 'EN':
#         WordTrans += 'k'
#     elif i == 'QO':
#         WordTrans += 'l'
#     elif i == 'VP':
#         WordTrans += 'm'
#     elif i == 'X6':
#         WordTrans += 'n'
#     elif i == 'FU':
#         WordTrans += 'o'
#     elif i == 'D2':
#         WordTrans += 'p'
#     elif i == 'ST':
#         WordTrans += 'q'
#     elif i == 'K6':
#         WordTrans += 'r'
#     elif i == 'L2':
#         WordTrans += 's'
#     elif i == 'W8':
#         WordTrans += 't'
#     elif i == 'V4':
#         WordTrans += 'u'
#     elif i == 'YI':
#         WordTrans += 'v'
#     elif i == 'D6':
#         WordTrans += 'w'
#     elif i == 'K9':
#         WordTrans += 'x'
#     elif i == 'MC':
#         WordTrans += 'y'
#     elif i == 'XX':
#         WordTrans += 'z'
#     else:
#         WordTrans += ' '
# print(WordTrans)



'''

a = 1













'''