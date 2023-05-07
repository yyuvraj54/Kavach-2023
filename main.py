import customtkinter
from customtkinter import CTk ,CTkFrame ,CTkButton ,CTkLabel ,CTkTextbox
from assets import defVar


# loading Default predefined variables
appWidth=defVar.Variables.appWidth
appHeight=defVar.Variables.appHeight
apkBackground=defVar.Variables.appBackgroundTheme

class PMS_Window(CTk):  
  
    def __init__(self, *args, **kwargs):  
          
        CTk.__init__(self, *args, **kwargs)  
        
        container = customtkinter.CTkFrame(self)  
        container.pack(side="top", fill="both", expand = True)  
        container.grid_rowconfigure(0, weight=1)  
        container.grid_columnconfigure(0, weight=1)  
  
        self.frames = {}  
  
        for F in (Agreement_Licence_Page, Login_Page):  
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
         
    
        pageTitle = CTkLabel(self, text ="Agreement And Licence",)
        pageTitle.pack(pady=10)


        textFrame=CTkFrame(self)
        textFrame.pack(expand=True)


        agreementText=CTkTextbox(textFrame,width=appWidth-400,height=appHeight-300,corner_radius=20,bg_color=apkBackground, wrap='word')
        agreementText.pack()
        agreementText.insert('end','''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum 
                             
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum''')
        agreementText.configure(state= "disabled")
        
        bottomFrame=CTkFrame(self,corner_radius=50)
        bottomFrame.pack(side='bottom',expand=True)

        button1 = CTkButton(bottomFrame, text ="Next" ,command = lambda : controller.show_frame(Login_Page))
        button1.pack(anchor='nw', pady=10 ,padx=10)



class Login_Page(customtkinter.CTkFrame):
     
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        pageTitle = CTkLabel(self, text ="Login")
        pageTitle.pack(pady=10)

        button1 = CTkButton(self, text ="Back",command = lambda : controller.show_frame(Agreement_Licence_Page))
        button1.pack(anchor='nw', pady=10 ,padx=10 )






# Main Window Settings
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = PMS_Window()  # create CTk window like you do with the Tk window
app.geometry(f'{appWidth}x{appHeight}')
app.title('PMS')    

app.mainloop()