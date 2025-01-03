from stack import Stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)

el = s.pop()
print(el)

s.push(4)
s.push(5)
s.push(6)
print(s, s.pop())
print(s.peek())
print(s, s.pop())
print(s.peek())
print(s, s.pop())
print(s.peek())
print(s, s.pop())
print(s.peek())
