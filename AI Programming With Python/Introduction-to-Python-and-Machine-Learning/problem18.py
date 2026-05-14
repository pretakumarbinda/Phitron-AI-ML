# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J

# S = input()
# S = sorted(S)


# memory = S[0]
# count = 0

# for i in range(len(S)):
#     if memory == S[i]:
#         count+=1
#     else:
#         print(f"{memory} : {count}")
#         memory = S[i]
#         count = 1
    
# if memory == S[-1]:
#     print(f"{memory} : {count}")
        


s = input()
dic = {}
count = 0
for i in range(len(s)):
    if s[i] in dic:
        count= dic[s[i]]
        count += 1
        dic[s[i]] = count
    else:
        dic[s[i]] = 1
        count = 1



sorted_dict = dict(sorted(dic.items()))
for key, value in sorted_dict.items():
    print(f"{key} : {value}")