class Device:
    def __init__(self):
        self.__vid=''
        self.__ystroystvo=''
        self.__pamiat=0
        self.__god=0
    def set_vid(self,vid):
        self.__vid=vid
    def set_ystroystvo(self,ystroystvo):
        self.__ystroystvo=ystroystvo
    def set_pamiat(self,pamiat):
        self.__pamiat=pamiat
    def set_god(self,god):
        self.__god=god
    
    def get_vid(self):
        return self.__vid
    def get_ystroystvo(self):
        return self.__ystroystvo
    def get_pamiat(self):
        return self.__pamiat
    def get_god(self):
        return self.__god
    
    def info(self):
        print("Вид",self.__vid,"\n","Устройство",self.__ystroystvo,"\n","Память",self.__pamiat,"\n","Год",self.__god,"\n")
    
    
    
class Phone(Device):
    def __init__(self):
        super().__init__()
        self.__marka=''
        self.__model=''
        
    def set_marka(self,marka):
        self.__marka=marka
    def set_model(self,model):
        self.__model=model
    
    def get_marka(self):
        return self.__marka
    def get_model(self):
        return self.__model
    def info(self):
        super().info()
        print("Марка",self.__marka,"\n","Модель",self.__model)
        
h=Phone()
h.set_vid('Вид')
h.set_god(2022)
h.set_marka('Сяоми')
h.set_model('Сяоми 10сы')
h.set_pamiat(128)
h.set_ystroystvo('Телефон')
h.info()