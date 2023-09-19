class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        
        stack = []
        
        for item in s:
            if len(stack) == 0:
                stack.append(item)
                continue
            
            if item in p_map:
                pop_item = stack.pop()
                if pop_item == p_map[item]:
                    continue
                else:
                    return False
            else:
                stack.append(item)
            
        if len(stack) != 0:
            return False
        
        return True
            
        