
from tkinter import *
import time

counter=0
userdata=[]
def addToken(listbox,tokenName):
    listbox.insert(END, tokenName)

def clearTokenList(listbox):
    listbox.delete(0, END)

def setToken(entry):
    token="BandobastArea"
    tokenID = time.strftime("%Y%m%d-%H%M%S")
    token=token+tokenID
    entry.insert(0,token)
    entry.clipboard_get()

def setPersonToken():
    global counter
    token="PersonID_"
    tokenID = time.strftime("%Y%m%d-%H%M%S")
    token=token+tokenID+"_"+str(counter)
    counter=counter+1
    return token

def getSelectedItems(event):
    
    try:
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            
            for x in userdata:
                if x[0]==data:
                    # detailLabel.config(text="Person Details",fg="red")
                    # personId.config(text="Person Id:"+x[0])
                    # personName.config(text="Person Name:"+x[1])
                    # personContact.config(text="Person Contact:"+x[3])
                    # personRank.config(text="Person Rank:"+x[2]) 
                    pass
    except(Exception):print(Exception)    
        

def submitform():
    pass 
    # token_username=tokenvariable.get()
    # bandobast_ID=Bandobast_Tokenvariable.get()
    # Password=tokenPassword.get()
    # dataAdapter.uploadfilesToRuntime(token_username,bandobast_ID,Password,userdata)




def addGroundPerson():

    def personDetailsDoneBtn():
        global userdata ,PersonList
        personid=personId.get()
        personName=nameEntry.get()
        personRank=rankEntry.get()
        personContact=contactEntry.get()
        userdata.append([personid,personName,personRank,personContact])
        PersonList.insert(END,personid)
        person.destroy()
        


    person=Toplevel()
    person.title("Ground Personnel")
    person.geometry("300x500+780+200")
    person.maxsize("300","500")
    person.minsize("300","500")

    userCenterFrame=Frame(person , background="white")
    userCenterFrame.pack(padx=10,pady=10,side=TOP,fill=Y,expand=True)

    userImage= Image.open('Icons/user.png')
    userImageResize=image.ImageResize(userImage,150,150)
    imageLabeluser=Label(userCenterFrame , image=userImageResize)
    imageLabeluser.pack()


    personIdFrame=Frame(userCenterFrame , background="white")
    personIdFrame.pack(padx=10,pady=5,side=TOP)
    Label(personIdFrame,text="Person Id").pack()
    idValue=setPersonToken()
    personId=Entry(personIdFrame,textvariable=idValue,width=25)
    personId.insert(0,idValue)
    personId.pack()


    nameFrame=Frame(userCenterFrame , background="white")
    nameFrame.pack(padx=10,pady=5,side=TOP)
    Label(nameFrame,text="Person Name").pack()
    nameEntry=Entry(nameFrame)
    nameEntry.pack()

    rankFrame=Frame(userCenterFrame , background="white")
    rankFrame.pack(padx=10,pady=5,side=TOP)
    Label(rankFrame,text="Person Rank").pack()
    rankEntry=Entry(rankFrame)
    rankEntry.insert(0,"NA")
    rankEntry.pack()

    contactFrame=Frame(userCenterFrame , background="white")
    contactFrame.pack(padx=10,pady=5,side=TOP)
    Label(contactFrame,text="Person Contact").pack()
    contactEntry=Entry(contactFrame)
    contactEntry.pack()
    
    confirmPersonBtn=Button(userCenterFrame,text="Done",command=personDetailsDoneBtn)
    confirmPersonBtn.pack()


    person.mainloop()
