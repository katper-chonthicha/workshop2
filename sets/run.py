# วิธี set แสดงเลขที่อยุ่ใน number_list ว่ามีเลขอะไรบ้าง 
number_list = [1,1,1,2,2,2,3,3,3]
print(set(number_list))

# EX1
result =[]
number_list = [1,1,1,2,2,2,3,3,3]
for number in number_list:
    if not number in result:
        result.append(number)

        print(list(set(number_list)))
