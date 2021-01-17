# EX1 เอา banana ออก remove
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

# EX2 เอา banana ออกไป
thisset = {"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

# EX3 pop ของ set คือจะสุ่มเอาตัวใดตัวหนึ่งออกไป
thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(thisset)

# EX4 clear set ให้เป็นค่าว่าง
thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)