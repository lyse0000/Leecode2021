class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing = 3
        if any('a'<=char<='z' for char in password): missing -= 1    
        if any('A'<=char<='Z' for char in password): missing -= 1    
        if any(char.isdigit() for char in password): missing -= 1
               
        one, two = 0, 0   
        i = 1
        fix = 0 # number to fix for aaa
        while i < len(password):
            if password[i] == password[i-1]:
                count = 1
                while i < len(password) and password[i] == password[i-1]:
                    count+=1
                    i+=1
                fix += count//3
                if count%3 == 0: one+=1
                elif count%3 == 1: two+=1
                
            else:
                i+=1
        
        
        """
        aaabbb aaaBBB 111111 0
        """
        if len(password)<=6:
            return max(6-len(password), missing, fix)
        """
        aaaababaa  aaaaabbbbb aaaaaaaaaBbbbabaa
        """
        if len(password)<=20:
            return max(missing, fix)
        
        """
        比如limit是12
        [333 555 55777 777 7Bb]bbbabaa
        
        333555557777777babababababavaadsada change = 4, missing type
        11111111111111111111222222222222222 delete 15 - 1 3 5
        """
        
        toomuch = len(password)-20
        
        fix -= min(toomuch, one)
        delete = max(0, toomuch-one)
        
        fix -= min(delete, two*2)//2
        delete = max(0, delete-two*2)
        
        fix -= min(delete, fix*3)//3
        
        
        return toomuch + max(fix, missing)
        
