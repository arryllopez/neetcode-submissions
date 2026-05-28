class Solution:
    def isValid(self, s: str) -> bool:
        # stack as LIFO behaviour
        stack_bracket = [] 
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        # edge case, if string starts with a closing bracket it is wrong
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        
        # now we can iterate over every char in string
        for i in range (len(s)): 
            # if har is opening, append it
            # stack_bracket.append(char)
            # we can skip this by just using a guard clause
            # if char is a key inpairs, meaning its a closing bracket
            if s[i] in pairs:
                # if the char is closing bnracket but stackis empty, this is immediate false
                if len(stack_bracket) == 0: 
                    return False
                
                # if top of stack is equal to value of the key s[i]
                if stack_bracket[-1] == pairs[s[i]]:
                    stack_bracket.pop() 
                else: 
                    return False

            else: 
                stack_bracket.append(s[i])

        return (len(stack_bracket) == 0)

                
            