class Solution(object):
    operators = ["+", "-", "*", "/"]
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        firstOperator = tokens.pop()
        return self.evalOneOperation(firstOperator, tokens)
        
    def evalOneOperation(self, operator, tokens):
        if len(tokens) == 0:
            return int(operator)
            
        operand1 = tokens.pop()
        if operand1 in Solution.operators:
            operand1 = self.evalOneOperation(operand1, tokens)
        else:
            operand1 = int(operand1)
        
        operand2 = tokens.pop()
        if operand2 in Solution.operators:
            operand2 = self.evalOneOperation(operand2, tokens)
        else:
            operand2 = int(operand2)
        
        if operator == "+":
            print operand2 + operand1
            return operand2 + operand1
        elif operator == "-":
            print operand2 - operand1
            return operand2 - operand1
        elif operator == "*":
            print operand2 * operand1
            return operand2 * operand1
        elif operator == "/":
            print operand2 / operand1
            return operand2 / operand1
        else:
            print "operator parsing error"
