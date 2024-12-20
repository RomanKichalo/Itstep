class ClassA:
    def __init__(self, a):
        self.a = a

    def method_a(self):
        return f"Method A: {self.a}"


class ClassB:
    def __init__(self, b):
        self.b = b

    def method_b(self):
        return f"Method B: {self.b}"


class ResultClass(ClassA, ClassB):
    def __init__(self, a, b, c):
        ClassA.__init__(self, a)
        ClassB.__init__(self, b)
        self.c = c

    def method_c(self):
        return f"Method C: {self.c}"


result = ResultClass(10, 20, 30)

print(result.method_a())
print(result.method_b())
print(result.method_c())