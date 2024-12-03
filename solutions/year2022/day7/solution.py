from FileSystem import FileSystem

fs = FileSystem()
with open('input.txt', 'r') as f:
    for line in f:
        fs.interpretLine(line.rstrip())

solution1 = sum([f.size for f in fs.traverseFolders() if f.size < 100000])

needed = fs.rootFolder.size - 40000000 # we need 30000000 free space on a total space of 70000000
solution2 = sorted([f.size for f in fs.traverseFolders() if f.size > needed])[0]

print(solution1, solution2)