data = dict()
with open('AoC12input.txt') as f:
    line = f.readline()

    while line:
        nodes = [x for x in line.strip('\n').split('-')]
        if data.get(nodes[0]) == None:
            data[nodes[0]] = []
        if data.get(nodes[1]) == None:
            data[nodes[1]] = []
        data[nodes[0]].append(nodes[1])
        data[nodes[1]].append(nodes[0])
        line = f.readline()

paths = 0
def count_paths(startNode, endNode, curr_path):
    global paths
    if curr_path[-1] == endNode:
        paths+=1
    
    for nextNode in data[startNode]:
        if nextNode.upper() == nextNode or nextNode not in curr_path :
            curr_path.append(nextNode)
            count_paths(nextNode, endNode, curr_path)
            curr_path.pop()


count_paths("start", "end", ["start"])
print(paths)