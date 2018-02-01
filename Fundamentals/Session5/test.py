# person = ["tuan anh", 22, 2, "ha noi", 5, 4, "Maria", "pingpong"]

tc = {
    #key  : value
    "ng": "người",
    "j": "gì",
    "vk": "vợ",
    "ko" : "không",
    "mk" : "mẹ kiếp",
    "ngta": "người ta",

}
key = input("nhập code: ")
if key in tc:
    print(tc[key])
else:
    print("chưa có trong từ điển")
    value = input("mời nhập nghĩa của từ: ")
    tc[key] = value

print(tc)

# for v in tc.values():
#  print (v)

# for key, v in tc.items():
#     print(key, v)
