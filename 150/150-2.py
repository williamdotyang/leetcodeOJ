class Solution(object):
    operators = ["+", "-", "*", "/"]
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in Solution.operators:
                stack.append(int(token))
            else:
                stack.append(self.evalOperation(token, stack))
        if len(stack) == 1:
            return stack.pop()
        else:
            print "too many tokens"

    def evalOperation(self, token, stack):
        if token == "+":
            operand1 = stack.pop()
            operand2 = stack.pop()
            return operand2 + operand1
        elif token == "-":
            operand1 = stack.pop()
            operand2 = stack.pop()
            return operand2 - operand1
        elif token == "*":
            operand1 = stack.pop()
            operand2 = stack.pop()
            return operand2 * operand1
        elif token == "/":
            operand1 = stack.pop()
            operand2 = stack.pop()
            return int(float(operand2) / float(operand1))
        else:
            print "unrecognized operator"
