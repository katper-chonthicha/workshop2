# EXAMPLE 1 remove สามารถเลือกได้เลยต้องการเอาอะไรออก
thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

# EXAMPLE 2 pop คือส่งตำแหน่งที่อยากลบเข้าไป
thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# EXAMPLE 3 popถ้าไม่ระบุตะแหน่งที่ต้องการลบเข้าไป pop จะไปลบที่ตำแหน่งสุดท้าย
thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)

# EXAMPLE 4 del ลบ และสามารถระบุตำแหน่งที่ต้องการลบได้
thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

# EXAMPLE 5 clear list ให้เหลือแต่ list เปล่า
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)