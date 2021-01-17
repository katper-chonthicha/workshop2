# EX1 union คือเอามารวมกันทั้งหมด ก็จะได้เป็น set3
set1 = {"a","b","c"}
set2 = {"d","e","f"}
set3 = set1.union(set2)
print(set3)

# EX2 การเอา set2 มาอัพเดพเข้า set1 และทำการ print set1 ออกมา
set1 = {"a","b","c"}
set2 = {"d","e","f"}
set1.update(set2)
print(set1)

# EX3 หาว่า 2เซตนี้มีอะไรที่เหมือนกัน คือการ intersection
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.intersection_update(set2)
print(set1)

# EX4
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set1)
