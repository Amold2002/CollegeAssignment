graph = {
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['G','I'],
    'D':['I'],
    'E':[],
    'F':[], 
    'G':[], 
    'I':[]  
}

def bfs(visit_completed,graph,current_node):
    visit_completed.append(current_node)
    queue=[]
    queue.append(current_node)
    
    while queue : 
        s= queue.pop(0)
        print(s)
        
        for neighbour in graph[s]:
            if neighbour not in visit_completed:
                visit_completed.append(neighbour)
                queue.append(neighbour)

bfs([],graph,'A')


