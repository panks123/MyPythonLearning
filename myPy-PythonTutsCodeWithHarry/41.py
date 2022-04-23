# oops---Multilevel inheritance

class Dad:
    basketball=1

class Son(Dad):
    dance=1
    guitar=2
    def isdance(self):
        return f"Yes I dance in {self.dance} forms"

class GrandSon(Son):
    dance=6    #overriding
    def isdance(self):
        return f"Yes I dance in {self.dance} dance forms"


darry=Dad()
larry=Son()
harry=GrandSon()

print(harry.isdance())
print(harry.basketball)
print(harry.guitar)