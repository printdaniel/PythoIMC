class MyMiCorporal(type):
    def __call__(cls,*args,**kwargs):
        height,weight = args
        print(f"Con una altura de {height} m. Y un peso de {weight} kg. ")
        print("Tú indice de masa corporal es: ")
        
        return type.__call__(cls,*args,**kwargs)

class IMC(metaclass=MyMiCorporal):
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def formula(self):
        return round(self.weight/(self.height**2),1)

    def __str__(self):
        return str(self.formula())

if __name__ == "__main__":
    print(IMC(1.80,84))
