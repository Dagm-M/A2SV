class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.map = {kingName: []}
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.map:
            self.map[parentName].append(childName)
        else:
            self.map[parentName] = [childName]
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(person=self.king):
            if person not in self.dead:
                order.append(person)

            if person in self.map:
                for child in self.map[person]:
                    dfs(child)
        dfs()
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
