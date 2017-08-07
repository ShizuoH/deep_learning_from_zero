# -*- conding: utf-8 -*-

# pythonの初期知識

# boolean
hungry = True
if hungry:
    print("hungry")
else:
    print("not hungry")

# for文
print("for loop test----------")
for ii in [1, 2, 3]:
    print(ii)

tmp = [10, 11, 12]
for ii in tmp:
    print(ii)
print(tmp)
print(len(tmp))

for ii in range(5):
    print(ii)

for ii in range(len(tmp)):
    print(str(ii) + "th value is " + str(tmp[ii]))
    
# 関数
print("function test ----------")
def hello():
    print("Hello World")

    str_val = "hogehoge"
    print(str_val)
    print(type(str_val))

hello()

# クラスとインスタンス
print("class test ----------")
class Man:
    def __init__(self, name):
        self.name = name
        print(name + " is initialized")

    def hello(self):
        print("Hello, my name is " + self.name + ".")

m = Man("Mario")
m.hello()

