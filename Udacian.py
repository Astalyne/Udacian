class Udacian:
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name=name 
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    def print_udacian(self):
        print(self.name+" Is enrolled in"+self.city+" studying "+self.nanodegree+" with Ms"+self.enrollment+" he/she is "+self.status)

u1 = Udacian("Sultan","Dammam","Elham 9am","fstack","ontrack")
u1.print_udacian()