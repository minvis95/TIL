class Stack():
    stack = []
    def push(self, data):
        self.stack.append(data)
        return self.stack
    def pop(self):
        if len(self.stack) == 0:
            return -1
        data = self.stack.pop()
        return data

str1 = '()()((()))'
str2 = '((()((((()()((()())((())))))'
