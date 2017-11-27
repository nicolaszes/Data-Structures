from collections import deque
# 广度优先搜索
def search(name) :
    # 创建一个队列
    search_queue = deque()
    # 将你的邻居都加入到这个搜索队列中
    search_queue += graph[name]
    # 用于记录检查过的人
    searched = []

    # 只要队列不为空
    while search_queue :
        # 取出其中的第一个人
        person = search_queue.popleft()

        # 仅当这个人没有被检查时，才检查
        if person not in searched :
            # 检查这个人是否是芒果经销商
            if person_is_seller(person) :
                print(person + ' is a seller')
                return True
            # 不是芒果经销商，将这个人的朋友都加入到搜索队列
            else :
                search_queue += graph[person]
                # 将这个人标记为检查过
                searched.append(person)
    # 达到这里，说明队列中没有芒果经销商
    return False

# 判断此人是否是芒果经销商
def person_is_seller(name) :
    return name[-1] == 'm'

# 初始化图的数据
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []

search('you')
