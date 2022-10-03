import math
# import turtle

print(abs(-2), '\t', abs(2))
print(max(12, 34, 56, -12))
print(min(12, 34, 56, -12))
print(pow(12, 4))
print(round(4.4), '\t', round(4.5), '\t', round(4.6), '\t', round(5.5))    # 四舍五入：返回最接近的整数，优先偶数
print(round(4.44444, 3))

print(round(math.tan(math.pi/6), 5))
print(round(math.exp(2), 5))

# turtle.write("\u03b1\u03b2\u03b3\u03b4\u03b5")
# turtle.done()

print(ord('a'))
print(chr(45))
d = True
c = str(23)
print(c, c+'34')
c += ' wild'
print(c)

i = 1
while i < 10:
    print("point", str(i), ':', end=' ')
    i += 1
print('\n', id(i))
print('\n', type(c), ' ', type(d))

e = "\tdefine\t"
f = e.upper()
print(e, ' ', f)
ee = e.strip()
print(ee)

a = 12.34455
b = 136778.20001
print(format(a, ".2f"), '\t', format(b, '.2e'), '\n', format(a, '<3.3%'))
