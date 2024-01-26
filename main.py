from array import *
num_days_temp=int(input("How many day's temperature?"))
# temp_days=[]
# for i in range(num_days_temp):
#     temp=float(input(f"Day {i+1}'s temp: "))
#     temp_days.append(temp)
# average=sum(temp_days)/len(temp_days)
# print(f"\nAverage = {average}")
# count=0
# for temp in temp_days:
#     if temp>average:
#         count+=1
# print(f"{count} day(s) above average")

temp_days=array('f')
for i in range(num_days_temp):                                  
    temp=float(input(f"Day {i+1}'s temp: "))
    temp_days.append(temp)
average=sum(temp_days)/len(temp_days)
print(f"\nAverage = {average}")

count=0
for temp in temp_days:
    if temp>average:
        count+=1
print(f"{count} day(s) above average")