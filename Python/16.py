# List.....
sub = ["C", "C++", "JAVA", "PYTHON"]
print(sub)
print(sub[0])
print(sub[-1])
print(sub[2:])
print("python" in sub)
print("PYTHON" not in sub)
print(sub + ["SQL, 2024"])
print(sub , ["SQL, 2024"])
print(sub * 4)

print(len(sub))
sub.append ("PHP")
print(sub)
sub.insert(2, "OS")
print(sub)
sub.remove("OS")
print(sub)

sub = [20,30,40,2,3,5,8,50,]
sub.sort()
print(sub)
sub.reverse()
print(sub)
sub.pop()
print(sub)
sub.clear()
print(sub)
sub1 = sub.copy()
print(sub1)

sub = [20,30,40,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,8,50,]
pos = sub.index(2)
print(pos)

pos1 = sub . count(3)
print(pos1)