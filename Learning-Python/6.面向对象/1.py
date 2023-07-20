class fClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

    z = 10


x = fClass()

y = fClass()

print(x.setdata('Yang'))
print(y.setdata(3.1415))

x.display()
y.display()

print(x.z)


x.data = 'HH'
x.display()