class Ron:
    def __init__(self,f,h):
        self.f = f
        self.h = h

    def __str__(self):
        return "[{},{}]".format(self.f,self.h)

if __name__ == '__main__':
    open=[Ron(1,2),Ron(1, 3),Ron(2, 0),Ron(1, 4)]
    print(open[0])

    open.sort(key=lambda x: (x.f, x.h), reverse=False)
    print(open[0])