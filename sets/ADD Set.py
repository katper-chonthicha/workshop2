# EX1 การใช้ set จะไม่การันตีเรื่องของตำแหน่ง ทุกครั้งที่ run ตำแหน่งก็จะเปลี่ยนไปเรื่อยๆ
thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

# EX2
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papya"}
thisset.update(tropical)
print(thisset)