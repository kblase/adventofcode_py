# with open('measurements') as my_file:
go_deeper= []
measurements=open('measurements').readlines()
measurements=[line.rstrip() for line in measurements]

print(len(measurements))
for i in range(0,len(measurements)):
  if measurements[i] > measurements[i-1]:
    go_deeper.append(1)

print('The Water depth increases', len(go_deeper), 'times!')
