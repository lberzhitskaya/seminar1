from myclass import index
from myclass import index_child

x = index(2,3)
y = index(7,8)
x.print_i1i2()
x.change_att()
print(x.sum_i1i2())
print(y.mult_i1i2())


#child class
z = index_child(5, 7, 9)
z.print_i1i2()
print(z.mult_i1i2())
print(z.i3_square())

