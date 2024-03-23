# step 1 for bfs is graph

graph= {
    'A':['B','D'],
    'B':['C','E'],
    'D':['E','G','H'],
    'E':['F'],
    'G':['H'],
}
#empty list bnegi visited nodes ke lie
VN=[]
#ek or list bnegi queue ke lie (bfs me queue hti ha)
q=[]
#function define hoga jisme parameters ayengy vn,graph, starting node , goal node 
def bfs( VN, graph, starting_node, goal_node):
    # ab start jis node se kr rhe hen use visited node me add krden. ab zahir ye chez q me bhi ayegi
    VN.append(starting_node)
    q.append(starting_node)
    # ab ek loop chlega jab tak q khali na hojae or ek ek element usme pop hota rhega 
    while q:
        m=q.pop(0)
    #ab jis node pe hen wo bhi print krni ha ya save krni ha 
    print (m, end="") # yaha m jaga pakar ke rkh rha ha current node ki 
    #ab ye bhi dekhna ha ke m esa to nh goal node hai.
    if m==goal_node :
       return
   #ager esa nh ha to uske jo neighbours hen unko check krega 
   
    for neighbours in graph[m]:
        #Loop ke har padosi ke liye, yeh dekhta hai ke kya yeh padosi pehle se visited nodes ki list (VN) mein shamil hai ya nahi.
        if neighbours not in VN :
            VN.append(neighbours) 
            q.append(neighbours)
            
print("here is the bfs")
# ye print ka syntax ha
print(VN, graph,'A','G')
            
        
   