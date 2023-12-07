def Ask_Input(message:str, sAuthorized: list[str],Movement:list[str]=[]):
    
    while True:
        Verif:str = input(message)
        
        if (Verif.upper() in sAuthorized):

            Where:int = sAuthorized.index(Verif.upper())
            if Movement == []:
                return Verif
            return Movement[Where]
        
        print('Invalid enter')
