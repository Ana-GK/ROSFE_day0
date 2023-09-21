class Kvader():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ploscina(self):
        return self.a * self.b
    
    def mojafunkcija(*args, **kwargs):
        print(repr(args[1:]))
        print(repr(kwargs))

# class Kvadrat(Kvader):
#     def __init__(self,a):
#         super(Kvadrat, self).__init__(a,a)

def main():
    kv = Kvader(1.0, 2.0)
    kv.ploscina()
    # kvadrat = Kvadrat(2.0)
    print(kv.ploscina())
    # print(kvadrat.ploscina())
    kv.mojafunkcija("ieri","kk","kwnjakir",arg1="oerko",arg2="oflero")


if __name__ == "__main__":
    main()