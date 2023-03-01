from collections import deque, defaultdict

def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1] == True:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
print(task_manager(tasks))
