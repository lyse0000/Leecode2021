class Solution:
    def expand(self, s: str) -> List[str]:
        ret, char, loop = [""], [], False
        for c in s:
            if c == '{':
                loop = True
            elif c=='}':
                loop = False
                temp = ret
                ret = []
                for ch in char:
                    ret.extend(t+ch for t in temp)
                char = []
            elif c==',':
                continue
            else:
                if loop:
                    char.append(c)
                else:
                    ret = [i+c for i in ret]
        return sorted(ret)
