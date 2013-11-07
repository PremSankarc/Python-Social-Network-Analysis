def parse_message(s):
    prefix   = ''
    trailing = ''
    if s.startswith(':'):
        prefix, s = s[1:].split(' ', 1)
    if ' :' in s:
        s, trailing = s.split(' :', 1)
    args = s.split()
    return prefix, args.pop(0), args, trailing

# 2nd try
filename = "sample.txt"
f = open(filename,'r')
lines = f.readlines()
for line in lines:
    print parse_message(line)
