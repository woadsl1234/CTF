import requests
import re
from bs4 import BeautifulSoup
maze=[]
maze_1=[]
maze_2=[]

se=requests.session()
url='http://111.230.105.104:5000/login'
leve1='http://111.230.105.104:5000/level{}'
ht=se.get(url)
url_1=url+'?username=dsafa'
temp=0
h = se.get(url_1)
while(temp<5):
    maze=[]
    maze_1=[]
    maze_2=[]
    reg=r'<li>(.*?)</li>'
    content=re.findall(reg,h.text)

    for i in range(len(content)):
        maze.append(list(content[i]))
    for i in range(len(maze)):
        maze_1=[]
        for j in range(len(maze[i])):
            if maze[i][j]=='1':
                maze_1.append(0)
            if maze[i][j]=='0':
                maze_1.append(1)
        maze_2.append(maze_1)
    print(maze_2)


    route_stack = [[0, 0]]
    route_history = [[0, 0]]
    source = maze_2
    length=len(maze_2)-1
    def up(location):
        # 横坐标为0，无法再向上走
        if location[1] == 0:
            return False
        else:
            new_location = [location[0], location[1] - 1]
            # 已经尝试过的点不会尝试第二次
            if new_location in route_history:
                return False
                # 碰到墙不走
            elif source[new_location[0]][new_location[1]] == 1:
                return False
            else:
                route_stack.append(new_location)
                route_history.append(new_location)
                return True

    def down(location):
        if location[1] == length:
            return False
        else:
            new_location = [location[0], location[1] + 1]
            if new_location in route_history:
                return False
            elif source[new_location[0]][new_location[1]] == 1:
                return False
            else:
                route_stack.append(new_location)
                route_history.append(new_location)
                return True

    def left(location):
        if location[0] == 0:
            return False
        else:
            new_location = [location[0] - 1, location[1]]
            if new_location in route_history:
                return False
            elif source[new_location[0]][new_location[1]] == 1:
                return False
            else:
                route_stack.append(new_location)
                route_history.append(new_location)
                return True

    def right(location):
        if location[0] == length:
            return False
        else:
            new_location = [location[0] + 1, location[1]]
            if new_location in route_history:
                return False
            elif source[new_location[0]][new_location[1]] == 1:
                return False
            else:
                route_stack.append(new_location)
                route_history.append(new_location)
                return True

    lo = [0, 0]
    while route_stack[-1] != [length, length]:
        if up(lo):
            lo = route_stack[-1]
            continue
        if down(lo):
            lo = route_stack[-1]
            continue
        if left(lo):
            lo = route_stack[-1]
            continue
        if right(lo):
            lo = route_stack[-1]
            continue
        route_stack.pop()
        lo = route_stack[-1]
    print(route_stack)
    payload='?solve='
    for z in route_stack:
        payload+='{},{}|'.format(z[0],z[1])
    print(payload[:-1])
    temp+=1
    xml=leve1.format(temp)+payload[:-1]
    h=se.get(xml)
    print(xml,h.text)
    print(h.url)
