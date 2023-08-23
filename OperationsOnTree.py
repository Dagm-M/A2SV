class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked_node = defaultdict(int)
        self.graph = defaultdict(list)

        for i, vertex in enumerate(parent):
            self.graph[vertex].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked_node:
            return False

        self.locked_node[num] = user
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked_node and self.locked_node[num] == user:
            del self.locked_node[num]
            return True

        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked_node:
            return False
        def check_ancestor(num):
            if num in self.locked_node:
                return True
            elif num == -1:
                return False
            return check_ancestor(self.parent[num])

        def check_desendant(num):
            for desend in self.graph[num]:
                if desend in self.locked_node:
                    return True
                if check_desendant(desend):
                    return True
            return False

        def dfs(num):
            for desend in self.graph[num]:
                if desend in self.locked_node:
                    del self.locked_node[desend]
                dfs(desend)

        if check_ancestor(self.parent[num]):
            return False
        if not check_desendant(num):
            return False

        dfs(num)
        self.lock(num, user)

        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
