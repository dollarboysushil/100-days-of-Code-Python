class Calculator:
    def __init__(self, fnum , snum):
        self.fnum = fnum
        self.snum = snum
        
        
    def add(self):
        return self.fnum+ self.snum
    
    def sub(self):
        return self.fnum - self.snum
    
    def mul(self):
        return self.fnum * self.snum
    
    def div(self):
        return self.fnum / self.snum
    
    
    
    
c1 = Calculator(10, 2)

print(c1.add())
print(c1.div())

