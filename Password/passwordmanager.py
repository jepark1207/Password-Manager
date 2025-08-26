from cryptography.fernet import Fernet

class PasswordManager:
    
    def __init__(self):
        self.key = None
        self.passwordfile = None
        self.passworddict = {}

    def createkey(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def loadkey(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def createpasswordfile(self, path, initialvalues = None):
        self.passwordfile = path

        if initialvalues is not None:
            for key, values in initialvalues.items():
                self.addpassword(key, values)
        with open(self.passwordfile, "w") as f:
            pass


    def loadpasswordfile(self, path):
        self.passwordfile = path
        with open(path, "r") as f:
            for line in f:
                site, encrypted = line.split(":")
                self.passworddict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def addpassword(self, site, password):
        self.passworddict[site] = password

        if self.passwordfile is not None:
            with open(self.passwordfile, "a") as f:
                encrypted = Fernet(self.key).encrypt(password.encode()).decode()
                f.write(site + ":" + encrypted + "\n")

    def deletepassword(self, site):
        del self.passworddict[site]

        with open(self.passwordfile, "w") as f:
                pass
                
        for key, values in self.passworddict.items():
            self.addpassword(key, values)


    def getpassword(self, site):
        return self.passworddict[site]
 









