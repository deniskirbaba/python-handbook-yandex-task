out = list()

while s := input():
    if s.strip().startswith('#'):
        continue
    
    if (com_idx := s.find('#')) == -1:
        out.append(s)
    else:
        out.append(s[:com_idx])
        
for i in out:
    print(i)
