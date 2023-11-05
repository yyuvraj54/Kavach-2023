import customtkinter
from customtkinter import CTk ,CTkFrame ,CTkButton ,CTkLabel ,CTkTextbox ,CTkEntry ,CTkImage,CTkToplevel,CTkComboBox
from assets.libs import defVar , imageModulation 
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from assets.libs import dataAdapter


# loading Default predefined variables
appWidth=defVar.Variables.appWidth
appHeight=defVar.Variables.appHeight
apkBackground=defVar.Variables.appBackgroundTheme
appForeground=defVar.Variables.appForegroundTheme
cornerRad=defVar.Variables.corner_radius


class PMS_Window(CTk):  
  
    def __init__(self, *args, **kwargs):  
          
        CTk.__init__(self, *args, **kwargs)  
        
        container = customtkinter.CTkFrame(self)  
        container.pack(side="top", fill="both", expand = True)  
        container.grid_rowconfigure(0, weight=1)  
        container.grid_columnconfigure(0, weight=1)  
  
        self.frames = {}  
  
        for F in (Agreement_Licence_Page, Login_Page,CreateBandobastArea):  
            frame = F(container, self)  
            self.frames[F] = frame  
            frame.grid(row=0, column=0, sticky="nsew")  
        self.show_frame(Agreement_Licence_Page)  
  
    def show_frame(self, cont):  
        frame = self.frames[cont]  
        frame.tkraise()  




class Agreement_Licence_Page(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent ,fg_color=apkBackground)
         
    
        pageTitle = CTkLabel(self, text ="Agreement And Licence",font=(defVar.fontstyle.fontText,defVar.fontstyle.titleFontSize))
        pageTitle.pack(pady=10)


        textFrame=CTkFrame(self,fg_color=appForeground,corner_radius=cornerRad)
        textFrame.pack(expand=True)


        agreementText=CTkTextbox(textFrame,width=appWidth-400,height=appHeight-300,fg_color=appForeground,corner_radius=20,bg_color=apkBackground, wrap='word')
        agreementText.pack()
        agreementText.insert('end','''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum 
                             
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum''')
        agreementText.configure(state= "disabled")
        
        bottomFrame=CTkFrame(self,corner_radius=50)
        bottomFrame.pack(side='bottom',expand=True)

        nextarrow=CTkImage(light_image=Image.open("assets/Icons/nextArrow.png"),
                                  dark_image=Image.open("assets/Icons/nextArrow.png"),
                                  size=(40, 25))
        button1 = CTkButton(bottomFrame, text ="Agree" ,compound='right',image=nextarrow,command = lambda : controller.show_frame(Login_Page))
        button1.pack(anchor='nw', pady=10 ,padx=10)



class Login_Page(customtkinter.CTkFrame):
     
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent ,fg_color=apkBackground)
        
        
        mainFrame=CTkFrame(self,fg_color="white")
        mainFrame.pack(padx=10,pady=10,expand=True,fill='both')
        
        InfoFrame=CTkFrame(mainFrame,corner_radius=cornerRad,fg_color='transparent')
        InfoFrame.pack(padx=20 ,side='left',expand=True,fill='both')

        loginImage=CTkImage(light_image=Image.open("assets/Icons/loginimage.png"),
                                  dark_image=Image.open("assets/Icons/loginimage.png"),
                                  size=(507, 360))
        
        imageLabelLogin=CTkLabel(InfoFrame , image=loginImage,text="")
        imageLabelLogin.pack(pady=30,anchor=N)

        CTkLabel(InfoFrame,text="Don't let anyone else in. Keep your login information private.").pack()


        backBtn = CTkButton(InfoFrame, text ="Show More",text_color='#E86B6E',hover=False,fg_color='transparent',command = lambda : controller.show_frame(Agreement_Licence_Page))
        backBtn.pack(padx=10 )

        
        centerFrame=CTkFrame(mainFrame,fg_color=appForeground,corner_radius=cornerRad,width=defVar.loginScreenVariables.screenFrameWidth)
        centerFrame.pack(padx=20)

        pageTitle = CTkLabel(centerFrame, text ="Login",font=(defVar.fontstyle.fontText,defVar.fontstyle.titleFontSize))
        pageTitle.pack(pady=10)


   
        erathImageResize=CTkImage(light_image=Image.open("assets/Icons/earthlogo.png"),
                                  dark_image=Image.open("assets/Icons/earthlogo.png"),
                                  size=(150, 150))
        imageLabelEarth=CTkLabel(centerFrame , image=erathImageResize,text="")
        imageLabelEarth.pack(pady=10)


        tokenFrame=CTkFrame(centerFrame,fg_color=appForeground)
        tokenFrame.pack()
        enterToken=CTkEntry(tokenFrame,placeholder_text="TokenID",height=defVar.loginScreenVariables.EntryHeight,width=defVar.loginScreenVariables.EntryWidth)
        enterToken.pack(side="top",padx=30)

        passwordFrame=CTkFrame(centerFrame,fg_color=appForeground)
        passwordFrame.pack(pady=20)
    
        enterpassword=CTkEntry(passwordFrame,show = '*',placeholder_text="Password",height=defVar.loginScreenVariables.EntryHeight,width=defVar.loginScreenVariables.EntryWidth)
        enterpassword.pack(side="top",padx=30)

        errorLabel=CTkLabel(centerFrame,text="")
        errorLabel.pack()

        logInBtn=CTkButton(centerFrame,text=" LogIn ")
        logInBtn.pack(side="top")

        CTkLabel(centerFrame,text="or").pack(pady=10)

        createBandobastArea=CTkButton(centerFrame,text=" Create new Token ",command=lambda : controller.show_frame(CreateBandobastArea))
        createBandobastArea.pack(side="top",pady=10)


class CreateBandobastArea(customtkinter.CTkFrame):
     
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent ,fg_color=apkBackground)
        def addGroundPerson():
            addGroundPersonWindow()
            


        def addGroundPersonWindow():

            def savePersonData():
                pId=personId.get()
                nameId=nameEntry.get()
                rankId=rankEntry.get() 
                contackId=contactEntry.get()
                personData=[pId,nameId,rankId,contackId]
            
                dataAdapter.setPersonInfo(PersonList,personData,subBandobastList.get())
                dataAdapter.updateFrmae(PersonList,subBandobastList.get())
                person.destroy()
                

            person=CTkToplevel()
            person.title("Ground Personnel")
            person.geometry("300x500")
            
        
        
            userCenterFrame=CTkFrame(person, fg_color="white")
            userCenterFrame.pack(padx=10,pady=10,side=TOP,fill=Y,expand=True)

            userlogo=CTkImage(light_image=Image.open("assets/Icons/user.png"),
                                    dark_image=Image.open("assets/Icons/user.png"),
                                    size=(200, 200))
            imageLabeluser=CTkLabel(userCenterFrame,image=userlogo,text="" )
            imageLabeluser.pack()


            personIdFrame=CTkFrame(userCenterFrame , fg_color="white")
            personIdFrame.pack(padx=10,pady=5,side=TOP)
            personId=CTkEntry(personIdFrame,placeholder_text="Person Id")
            personId.insert(END,dataAdapter.genratePersonToken())
            personId.pack()


            nameFrame=CTkFrame(userCenterFrame , fg_color="white")
            nameFrame.pack(padx=10,pady=5,side=TOP)
            nameEntry=CTkEntry(nameFrame,placeholder_text="Person Name")
            nameEntry.pack()

            rankFrame=CTkFrame(userCenterFrame , fg_color="white")
            rankFrame.pack(padx=10,pady=5,side=TOP)
            rankEntry=CTkEntry(rankFrame,placeholder_text="Person Rank")
            rankEntry.insert(0,"NA")
            rankEntry.pack()

            contactFrame=CTkFrame(userCenterFrame , fg_color="white")
            contactFrame.pack(padx=10,pady=5,side=TOP)
            contactEntry=CTkEntry(contactFrame,placeholder_text="Person Contact")
            contactEntry.pack()
            
            confirmPersonBtn=CTkButton(userCenterFrame,text="Done",command=savePersonData)
            confirmPersonBtn.pack()

            # loginPageBtn=CTkButton(self,text=" Login ",command=lambda : controller.show_frame(Login_Page))
            # loginPageBtn.pack(side="top",pady=10)
            person.mainloop()


        centerFrame=CTkFrame(self, width=appWidth-100,height=appHeight-100)
        centerFrame.pack(padx=10,pady=10,side=TOP,fill=BOTH,expand=True)

        # erathImage= Image.open('Icons/earthlogo.png')
        # erathImageResize=image.ImageResize(erathImage,150,150)
        # imageLabelEarth=CTkLabel(centerFrame , image=erathImageResize)
        # imageLabelEarth.pack(pady=10)



        bandobastTokenFrame=CTkFrame(centerFrame)
        bandobastTokenFrame.pack()

        CTkLabel(bandobastTokenFrame,text="BandoBast Area ID").pack()
        
        basdobast_enterToken=CTkEntry(bandobastTokenFrame,placeholder_text="Bandobast Id:",width=defVar.SignupScreenVariables.EntryWidth,height=defVar.SignupScreenVariables.EntryHeight)
        basdobast_enterToken.insert(END,dataAdapter.genrateBandobastAreaToken())
        basdobast_enterToken.pack(side="top",pady=10,padx=5)


        tokenFrame=CTkFrame(centerFrame)
        tokenFrame.pack()
        enterToken=CTkEntry(tokenFrame,placeholder_text="TokenId/Username")
        enterToken.pack(side="top")



        passwordFrame=CTkFrame(centerFrame)
        passwordFrame.pack(pady=10)
        enterpassword=CTkEntry(passwordFrame,placeholder_text="Password",show = '*')
        enterpassword.pack(side="top")

        # coordinateLatitude=CTkFrame(centerFrame)
        # coordinateLatitude.pack(pady=10)
        # CTkLabel(coordinateLatitude,text="Latitude Coordinate").pack(side=LEFT)
        # enterCoordinateLatitude=CTkEntry(coordinateLatitude)
        # enterCoordinateLatitude.pack(side="top")

        # coordinateLongitude=CTkFrame(centerFrame)
        # coordinateLongitude.pack(pady=20)
        # CTkLabel(coordinateLongitude,text="Longitude Coordinate").pack(side=LEFT)
        # enterCoordinateLongitude=CTkEntry(coordinateLongitude)
        # enterCoordinateLongitude.pack(side="top")

        frameBandobastArea = CTkFrame(centerFrame)
        frameBandobastArea.pack()

        # frameSubBandobastArea=CTkFrame(frameBandobastArea)
        # frameSubBandobastArea.pack(side=LEFT,padx=10)
        # CTkLabel(frameSubBandobastArea,text="All sub-bandobast area").pack()
        # subBandobastList = CTkComboBox(frameSubBandobastArea)
        # subBandobastList.pack()
        # addSubBandobastAreaBtn=Button(frameSubBandobastArea,text="Add Sub-bandobast")
        # addSubBandobastAreaBtn.pack()

        def updateDataset(e):
            PersonList.set("")
            dataAdapter.updateFrmae(PersonList,subBandobastList.get())


        sub_bandobastlst=CTkFrame(frameBandobastArea)
        sub_bandobastlst.pack(side=LEFT,expand=True,fill=BOTH)
        CTkLabel(sub_bandobastlst,text="Sub-Bandobast Area").pack()
        subBandobastList = CTkComboBox(sub_bandobastlst,command=updateDataset,values=[],width=defVar.SignupScreenVariables.CTkComboBoxWidth,height=defVar.SignupScreenVariables.CTkComboBoxHeight)
        subBandobastList.pack(pady=10)
        subBandobastList.set('select a sub-bandobast')
        
        addSubBandobastAreaBtn=CTkButton(sub_bandobastlst,text="Create Sub-Bandobast",command=lambda: dataAdapter.setSub_bandobastArea(subBandobastList,PersonList))
        addSubBandobastAreaBtn.pack()


        def selected(e):
            details=dataAdapter.showPersonDetails(e,subBandobastList.get())

    
            detailLabelvar.set("Person Details")
            personIdvar.set("Person Id: "+details[0])
            personNamevar.set("Person Name: "+details[1])
            personRankvar.set("Person Rank: "+details[2])
            personContactvar.set("Person Contact:"+details[3])

        frameBandobastAreaPerson=CTkFrame(frameBandobastArea)
        frameBandobastAreaPerson.pack(side=LEFT,expand=True,fill=BOTH,padx=10)
        CTkLabel(frameBandobastAreaPerson,text="All ground personnels").pack()
        PersonList = CTkComboBox(frameBandobastAreaPerson,values=[],command=selected,width=defVar.SignupScreenVariables.CTkComboBoxWidth,height=defVar.SignupScreenVariables.CTkComboBoxHeight)
        PersonList.pack(pady=10)
        PersonList.set('Select a person')
        
        

        addPersonBandobastAreaBtn=CTkButton(frameBandobastAreaPerson,text="Add more person",command=addGroundPerson)
        addPersonBandobastAreaBtn.pack()




        frameBandobastAreaPersonDetails=CTkFrame(frameBandobastArea)
        frameBandobastAreaPersonDetails.pack(pady=5,expand=True,fill=BOTH)

        detailLabelvar= tkinter.StringVar(value="")
        detailLabel=CTkLabel(frameBandobastAreaPersonDetails,textvariable=detailLabelvar)
        detailLabel.pack()

        personIdvar= tkinter.StringVar(value="")
        personId=CTkLabel(frameBandobastAreaPersonDetails,textvariable=personIdvar)
        personId.pack(anchor=NW)

        personNamevar= tkinter.StringVar(value="")
        personName=CTkLabel(frameBandobastAreaPersonDetails,textvariable=personNamevar)
        personName.pack(anchor=NW)

        personRankvar= tkinter.StringVar(value="")
        personRank=CTkLabel(frameBandobastAreaPersonDetails,textvariable=personRankvar)
        personRank.pack(anchor=NW)

        personContactvar= tkinter.StringVar(value="")
        personContact=CTkLabel(frameBandobastAreaPersonDetails,textvariable=personContactvar)
        personContact.pack(anchor=NW)


        submitBtn=CTkButton(centerFrame,text="Submit")
        submitBtn.pack(pady=10)



# Main Window Settings
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = PMS_Window()  # create CTk window like you do with the Tk window
app.geometry(f'{appWidth}x{appHeight}')
app.maxsize(appWidth,appHeight)
app.minsize(appWidth-200,appHeight)
app.title('PMS')    
print("App Running") #indication
app.mainloop()