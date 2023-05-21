
import time


Sub_BandobastList=[]
PersonnelsList=[]
PersonDetails=[]


def genrateBandobastAreaToken():
    token="BandobastArea"
    tokenID = time.strftime("%Y%m%d-%H%M%S")
    token=token+tokenID
    return token


def genrateSubBandobastAreaToken():
    token="Sub_BandobastArea"
    tokenID = time.strftime("%Y%m%d-%H%M%S")
    token=token+tokenID
    return token



def genratePersonToken():
    token="PersonID_"
    tokenID = time.strftime("%Y%m%d-%H%M%S")
    token=token+tokenID
    return token

def updateFrmae(person,selbandobast):
    index=Sub_BandobastList.index(selbandobast)
    person.configure(values=PersonnelsList[index])
    
    


def setSub_bandobastArea(ComboBox,PersonComboBox):
    token=genrateSubBandobastAreaToken()
    Sub_BandobastList.append(token)
    PersonnelsList.append([])
    PersonDetails.append([])
    ComboBox.configure(values=Sub_BandobastList)
    ComboBox.set(token)
    PersonComboBox.set("")
    updateFrmae(PersonComboBox,token)

def setPersonInfo(ComboBox,Persondata,selectedBandobastId):
    index=Sub_BandobastList.index(selectedBandobastId)
    token=Persondata[0]
    PersonnelsList[index].append(token)
    PersonDetails[index].append(Persondata)
    ComboBox.configure(values=PersonnelsList[index])
    ComboBox.set(token)

def showPersonDetails(personID,selectedBandobastId):
    selIndex=Sub_BandobastList.index(selectedBandobastId)
    realindex=-1
    lst=PersonnelsList[selIndex]
    
    print(lst)     
    realindex=lst.index(personID)
    if (realindex!=-1): 
        currentSelctedSet = PersonDetails[selIndex][realindex]
        return currentSelctedSet

    
    