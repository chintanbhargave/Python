class account():

    def __init__(self,fpath):
        self.filepath = fpath
        with open(fpath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amt):
        self.balance = self.balance - amt

    def deposit(self,amt):
        self.balance = self.balance + amt

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))         


class sub(account):

    def __init__(self,fpath,fee):
        account.__init__(self,fpath)
        self.fee = fee

    def transfer(self,amt):
        self.balance = self.balance - amt - self.fee

s1 = sub("balance.txt",1)
s1.deposit(250)        
s1.commit()
print(s1.balance)