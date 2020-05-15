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

acc = account("balance.txt")
print(acc.balance)
acc.deposit(300)
acc.commit()
print(acc.balance)