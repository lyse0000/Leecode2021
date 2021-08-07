class Solution:
    def countOfAtoms(self, formula: str) -> str:
        data = self.helper(formula)
        ans = ""
        for k,v in sorted(data.items()):
            ans += (k + str(v)) if v>1 else k
        return ans
        
        
    def helper(self, form):
        counter = collections.Counter()
        i, element = 0, ""
        
        while i < len(form):
            if form[i] == "(":
                # check if Mg(..)2
                if len(element)>0:
                    counter[element]+=1
                    element = ""
                # get end of parameter
                paralenidx = i+self.nextVaildPara(form[i:])
                
                # recursive call 
                data = self.helper(form[i+1:paralenidx])
                
                # update i to the end ) + 1
                i = paralenidx+1
                while i<len(form) and form[i].isdigit():
                    i+=1
                multiply = int(form[paralenidx+1:i]) if i>(paralenidx+1) else 1

                # multiple the multiple and update the counter
                for key in data:
                    counter[key] += multiply*data[key]
            
            elif form[i].isdigit():
                # preserve current idx
                num = i
                
                # get num end idx
                while i<len(form) and form[i].isdigit(): 
                    i+=1
                num = int(form[num:i])
                
                # update counter
                counter[element] += num
                element = ""
                
            elif form[i].isalpha(): 
                # if upper letter, means new element
                if 'A'<=form[i]<='Z':
                    # need to clean up the prev element
                    if len(element)>0:
                        counter[element]+=1
                    element = ""
                element += form[i]
                i+=1
                
        if len(element)>0:
            counter[element]+=1
            
        return counter
            
    
    def nextVaildPara(self, s):
        count = 1
        # 01(34567)9
        #   0123456
        # return 6, 2+6 = 8
        for i in range(1, len(s)):
            if s[i] == '(':
                count+=1
            elif s[i] == ')':
                count-=1
                if count == 0:
                    return i
        return len(s)
                
