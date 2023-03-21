#Create the graph
graph={
    'A':[('B',2),('C',3)],
    'B':[('A',2),('C',1),('G',9)],
    'C':[('B',1)],
    'D':[('E',6),('G',1)],
    'E':[('A',3),('D',6)],
    'G':[('B',9),('D',1)]
    
}

#define the all node with its corresponding heuristic value it return the value 
def heuristic(n):
    H_dist={
        'A':11,
        'B':6,
        'C':99,
        'D':1,
        'E':7,
        'G':0,
        
    }
    return H_dist[n]

#define a function for start alogorithm 
def AStarAlgo(start_node,stop_node):
    #store the first node in open_set
    open_set= set(start_node)
    #We take one empty set
    closed_set = set()
    #Store a distance from starting node 
    g={}
    #Parents contain an adjacency map of all nodes  
    parents={}
    #start_node is root node. i.e it has no parent nodes 
    g[start_node]=0
     # so start_node is set to its own parent node
    parents[start_node]=start_node
    while len(open_set) > 0:
        n=None
        #node with lowest f() found 
        for v in open_set:
            if n==None or g[v] +heuristic(v) < g[n] + heuristic(n):
                n=v
        if n== stop_node or graph[n]==None:
            pass
        
        else:
            for(m,weight) in get_neighbors(n):
                 #nodes 'm' not in first and last set are added to first
                #n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                #for each node m,compare its distance from start i.e g(m) to the
                 #from start through n node 
                else:
                    if g[m]>g[n]+weight:
                        #update g(m)
                        g[m]=g[n]+weight
                         #change parent of m to n
                        parents[m]=n
                        if m in closed_set:
                            #if m in closed set,remove and add to open
                            closed_set.remove(m)
                            open_set.add(m)
        if n==None:
            print('Path dose not exist!')
            return None
        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n== stop_node:
            path=[]
            
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
         # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    print('Path dose not exist')
    return None

# fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None
    
AStarAlgo('A','G')
                    
