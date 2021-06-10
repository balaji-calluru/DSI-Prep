"""
txt = '''
multi
line
text'''
print(txt)

txt = "Balaji's"
print(txt)

txt = 'Balaji\'s'
print(txt)

txt = 'Hello'
txt += 'World!'
print(txt)

txt = "Hello "
print(txt + "World!")
print(txt*5)

a = 3
print(a)
print(type(a))
print(str(a))

b = 3.14
print(b)
print(type(b))
print(str(b))

c = [1,1,2,3,5,8]
print(c)
print(type(c))
print(str(c))

d = None
print(d)
print(type(d))
print(str(d))

e = True
print(e)
print(type(e))
print(str(e))

f = False
print(f)
print(type(f))
print(str(f))

a = "10"
print(a)

b = int(a)
print(b)

a = "10.4"
print(a)

b = float(a)
print(b)

print(bool("hello"))
print(bool(""))
print(bool(" "))
"""

lorem = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum
'''

for char in lorem:
    print(char)

for word in lorem.split():
    print(word)

print(lorem.split())
