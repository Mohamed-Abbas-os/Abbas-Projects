details=['name','age','qualification','experience','exjob']
clients=[]
class clientserver:
    def clientform(self):
        print('(Note:your informations are to be recorded)')
        name=input('Enter your  name :')
        age=input('Enter your age :')
        qualification=input('Your Qualification :')
        exprience=input('Your job Experience (in years):')
        exjob=input('Worked companies:')   
        clients.append(name)
        clients.append(age)
        clients.append(qualification)
        clients.append(exprience)
        clients.append(exjob)
        clients.append('---Next staff---')
        print('we will catch you later...')
    def information(self):
        with open('file.txt','a') as file:
            file.write('\n')
            for detail,client in zip(details,clients):
                file.write(f'{detail} : {client} \n ')
class out:
    def stoerdinfo(self):
        with open('file.txt','r') as file1:
            content=file1.read().strip()
            print(content)
if __name__=='__main__':
    client1=clientserver()
    client1.clientform()
    client1.information()