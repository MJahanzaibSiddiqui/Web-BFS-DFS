graph= {
    'A':['B','D'],
    'B':['C','E'],
    'D':['E','G','H'],
    'E':['F'],
    'G':['H'],
}
VN=set()
def dfs(graph, VN, starting_node,goal_node):
    if starting_node not in VN:
        print(starting_node)
        #yaha pe append islie nh kia qk set use kr rhe hen list nh.
        VN.add(starting_node)
    if goal_node==VN:
           return
    for neighbour in graph[starting_node]:
         dfs(graph,VN, neighbour,goal_node)
print("Here is the DFS")
dfs(VN,graph,'A','G')

# graph = {
#     'A': ['B', 'D'],
#     'B': ['C', 'E'],
#     'D': ['E', 'G', 'H'],
#     'E': ['F'],
#     'G': ['H'],
# }

# VN = set()

# def dfs(graph, VN, starting_node, goal_node):
#     if starting_node not in VN:
#         print(starting_node)
#         VN.add(starting_node)
#     if goal_node == VN:
#         return
#     for neighbour in graph[starting_node]:
#         dfs(graph, VN, neighbour, goal_node)

# print("Here is the DFS")
# dfs(graph, VN, 'A', 'G')

