class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rec = []
        for i in range(len(ops)):
            if ops[i] not in ["C", 'D', "+"]:
                rec.append(int(ops[i]))
            elif ops[i] == 'D':
                rec.append(2*rec[len(rec)-1])
            elif ops[i] == '+':
                rec.append(rec[len(rec)-1] + rec[len(rec)-2])
            else:
                del rec[len(rec)-1]
        return sum(rec)
