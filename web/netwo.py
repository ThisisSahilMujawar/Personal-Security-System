n = 2
roads = [[1,0]]

list_count = [0 for i in range(n)]


x= 0
while x<n:
    for i in range(len(roads)):
        j = 0
        while j<2:
            if roads[i][j] == x:
                list_count[x] = list_count[x] + 1
                break
            j = j + 1
    x = x + 1


common_roads = [[0]*n for _ in range(n)]
k = 0

for i in range(len(roads)):
    k = roads[i][0]
    l = roads[i][1]
    common_roads[k][l] = 1
    common_roads[l][k] = 1
    print(common_roads)
        
count = 0

for i in range(len(list_count)):
    j= i + 1
    while j<len(list_count):
        count =max(count, list_count[i] + list_count[j] - common_roads[i][j])
        j = j + 1
print(list_count)      
print (count)