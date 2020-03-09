n = 10
cars = 2
start = [3,8]
end = [4,9]


cars_array = []
for i in range(len(start)):
    cars_array.append([start[i],end[i]])
#merge intervals

intervals = cars_array
intervals.sort(key=lambda x: x[0])
merged = []
for i in intervals:
    if not merged or merged[-1][-1]<i[0]:
        merged.append(i)
    else:
        merged[-1][-1] = max(i[-1],merged[-1][-1])
print(merged)

maxx = max(0,merged[0][0]-0,n-merged[-1][1])
for index in range(len(merged)-1):
    if merged[index+1][0]-merged[index][1]>maxx:
        maxx = merged[index+1][0]-merged[index][1]
print(maxx)
