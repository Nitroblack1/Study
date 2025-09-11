# 조건문
##1330 / 9498 / 2753 / 14681 / 2884
## 2525
# m, s = map(int, input().split())
# c = int(input())
#
# m_p = int((s + c) / 60)
# c_p = (s + c) % 60
#
# if m + m_p >= 24:
#     print(str(m + m_p - 24) + ' ' + str(c_p))
# else:
#     print(str(m + m_p) + ' ' + str(c_p))
#
# # 2480
# nums = list(map(int, input().split()))
# nums.sort()
#
# if nums[0] == nums[1] and nums[1] == nums[2]:
#     print(10000 + nums[0]  *1000)
# elif (nums[0] == nums[1] and nums[1] != nums[2]) or (nums[1] == nums[2] and nums[1] != nums[0]):
#     print(1000 + nums[1] * 100)
# elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
#     print(nums[2] * 100)
#
# # 반복문
# ## 2739, 10950, 8393
# ## 25304
# total = int(input())
# num = int(input())
# sum = 0
#
# for i in range(num):
#     price, num = map(int, input().split())
#     sum += price * num
#
# if sum == total:
#     print('Yes')
# else:
#     print('No')
#
# ## 25314
# n = int(int(input()) / 4)
#
# for i in range(n):
#     print('long', end=" ")
#
# print('int')
#
# ## 15552
# ### Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# ### 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.





# # 1차원 배열
# ## 10807
# n = int(input())
# numbers = list(map(int, input().split()))
# finder = int(input())
# count = 0
#
# for number in numbers:
#     if number == finder:
#         count += 1
#
# print(count)
#
# ## 10818
# n = int(input())
# nums = list(map(int, input().split()))
#
# nums.sort()
# print(nums[0], nums[n-1])
#
# ## 2562
# max_num = -1
# max_id = -1
#
# for i in range(9):
#     num = int(input())
#     if num > max_num:
#         max_num = num
#         max_id = i+1
#
# print(max_num)
# print(max_id)

## 10810
# n, m = map(int, input().split())
# buckets = [0] * n
# for _ in range(m):
#     i, j, k = map(int, input().split())
#     for a in range(i, j+1):
#         buckets[a-1] = k
#
# for bucket in buckets:
#     print(bucket, end=' ')


## 10813
# n, m = map(int, input().split())
# buckets = []
#
# # 해당 바구니 공들 교환
# def swap(b1, b2):
#     temp = buckets[b1 - 1]
#     buckets[b1 - 1] = buckets[b2 - 1]
#     buckets[b2 - 1] = temp
#     return True
#
# # 각 바구니에 해당하는 번호의 공 넣기
# for ball in range(1, n+1):
#     buckets.append(ball)
#
# for _ in range(m):
#     ball_1, ball_2 = map(int, input().split())
#     swap(ball_1, ball_2)
#
# # 바구니 현황 출력
# for ball in buckets:
#     print(ball, end=" ")


## 5597
# # 출석부 생성
# name_list = []
# for num in range(1, 31):
#     name_list.append(num)
#
# # 제출한 28명의 학생 체크
# for _ in range(28):
#     name_list[int(input()) - 1] = -1
#
# for num in range(30):
#     if name_list[num] != -1:
#         print(num + 1)


## 3052
# numbers = []
#
# for _ in range(10):
#     exist = False
#     number = int(input()) % 42
#     for i in range(len(numbers)):
#         if numbers[i] == number:
#             exist = True
#             break
#     if not exist:
#         numbers.append(number)
#
# print(len(numbers))


## 10811
# n, m = map(int, input().split())
# buckets = []
#
# # 바구니 생성
# for bucket in range(1, n+1):
#     buckets.append(bucket)
#
# # 역순으로 만드는 함수
# def reverse(s, f):
#     buckets[s-1:f] = list(reversed(buckets[s-1:f]))
#
# # main
# for _ in range(m):
#     start_idx, finish_idx = map(int, input().split())
#     reverse(start_idx, finish_idx)
#
# for bucket in buckets:
#     print(bucket, end=" ")


## 1546
# courses_num = int(input())
# score_list = list(map(int, input().split()))
#
# print((sum(score_list) / max(score_list) * 100) / courses_num)


### Study
## 오름차순 정렬

# my_list = [3, 7, 2, 9, 5]
#
# # 원본을 직접 정렬 (제자리 정렬)
# my_list.sort()
# print(my_list)  # 👉 [2, 3, 5, 7, 9]
#
# # 새로운 정렬된 리스트 반환 (원본은 그대로)
# sorted_list = sorted(my_list)
# print(sorted_list)  # 👉 [2, 3, 5, 7, 9]

## 내림차순 정렬
# my_list = [3, 7, 2, 9, 5]
#
# # 제자리 내림차순 정렬
# my_list.sort(reverse=True)
# print(my_list)  # 👉 [9, 7, 5, 3, 2]
#
# # 새로운 내림차순 리스트 반환
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)  # 👉 [9, 7, 5, 3, 2]