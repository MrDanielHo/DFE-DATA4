class Special():

    def __init__(self, value):
        self._value = str(value)

    def __add__(self, other):
        return self._value + other._value

    def __mul__(self, num):
        return ''.join((self._value for i in range(num)))

    def __str__(self):
        return self._value.upper()

    def __eq__(self, other):
        return self._value == other._value

if __name__ == '__main__':
    s = Special('spam')
    t = Special('eggs')
    u = Special\
    ('spam')
    v = Special(5)
    w = Special(22)

print("s + s", s + s)
print("s + t", s + t)
print("t + t", t + t)
print("s & 10", s * 10)
print("t * 3", t * 3)
print("str(s)={}  str(t)={}".format(str(s), str(t)))
print("id(s)={} id(t)={} id(u)={}".format(id(s), id(t), id(u)))
print("s == s", s == s)
print("s == t", s == t)
print("s == t", s == u)
print("v + v", v + v)
print("v + w", v + w)
print("w + w", w + w)
print("v * 10", v * 10)
print("w * 3", w * 3)