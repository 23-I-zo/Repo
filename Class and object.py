class dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
x = dog("dawa", "white", 12)
y = dog("nima", "brown", 20)
z = dog("blacky", "black", 16)

print(x.name, x.color, x.age)
print(y.name, y.color, y.age)
print(z.name, z.color, z.age)
