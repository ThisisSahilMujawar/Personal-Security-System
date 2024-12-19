roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

n = 4
x=0
count = 0
count_x = 0
count_y = 0

# List of roads
roads =[[0,1],[0,3],[1,2],[1,3]]

# Determine the number of nodes
num_nodes = max(max(road) for road in roads) + 1

# Create and initialize the adjacency matrix
adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

# Populate the adjacency matrix
for edge in roads:
    node1, node2 = edge
    adjacency_matrix[node1][node2] = 1
    adjacency_matrix[node2][node1] = 1

# Print the adjacency matrix


while x <=n:
    y=x+1
    while y<=n:
        count_y = 0
        count_x = 0
        for i in range(len(roads)):
            if roads[i][0] == x or roads[i][1] == x:
                count_x = count_x + 1
            if roads[i][0] == y or roads[i][1] == y:
                count_y = count_y + 1
                count = max(count,count_x + count_y - adjacency_matrix[x][y])
                print (x,y,":",count_x,count_y,count_x + count_y - adjacency_matrix[x][y])
        y=y+1
    x=x+1
print(count)
