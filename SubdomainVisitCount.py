class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpd = []
        visitCount = []
        domains = defaultdict(int)

        for cpdomain in cpdomains:
            cpd = cpdomain.split()
            cpd[1] = cpd[1].split(".")

            n = len(cpd[1]) - 1
            while n >= 0:
                key = ".".join(cpd[1][n:])
                domains[key] += int(cpd[0])
                n -= 1
        
        for domain,numberOfVisits in domains.items():
            visitCount.append(" ".join([str(numberOfVisits),domain]))

        return visitCount
