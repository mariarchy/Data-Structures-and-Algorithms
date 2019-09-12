ADD = '+'
SUB = '-'
MULT = '*'
DIV = '/'

class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        stack, val, op = [], 0, '+'
        i = 0

        while i <= len(s):
            if i < len(s) and s[i].isdigit():
                val = val * 10 + int(s[i])
            elif i == len(s) or s[i] == ADD or s[i] == SUB or s[i] == MULT or s[i] == DIV:
                if op == ADD:
                    stack.append(val)
                elif op == SUB:
                    stack.append(-val)
                elif op == MULT:
                    stack.append(stack.pop() * val)
                elif op == DIV:
                    stack.append(int(stack.pop() / val))

                if i < len(s): op, val = s[i], 0

            i += 1

        return sum(stack)


        
