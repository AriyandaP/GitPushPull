x=''
y=' * '
z='\n'
xx=' '

# print('Solve It! #1')

# for a in range(0,5,1):
#     for b in range(0,5-4+a,1):
#         x+=y
#     x+=z
# print(x)

# print('Solve It! #2')

# for a in range(0,5,1):
#     for b in range(0,5-a,1):
#         x+=y
#     x+=z
# for c in range(0,5,1):
#     for d in range(0,5-4+c,1):
#         x+=y
#     x+=z
# print(x)

print('Solve it #3')

for a in range(0,19,2):
    for b in range(0,19-a,1):
        x+=' '
    for c in range(0,a+1,1):
        x+=' *'
    x+='\n'
print(x)

# print('Solve It! #4')

# for a in range(0,19,2):
#     for b in range(0,a+1,1):
#         x+=' '
#     for c in range(0,19-a,1):
#         x+=' *'
#     x+='\n'
# print(x)

# print('Solve it! #5')

# for a in range(0,10,2):
#     for b in range(0,9-a,1):
#         x+=' '
#     for c in range(0,a+1,1):
#         x+='* '
#     x+='\n'
# for a in range(0,10,2):
#     for b in range(0,a,1):
#         x+=' '
#     for c in range(0,9-a,1):
#         x+=' *'
#     x+='\n'
# print(x)