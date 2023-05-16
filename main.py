import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkTextbox, CTkEntry
from assets.libs import defVar, imageModulation
from tkinter import *
from PIL import Image, ImageTk
import tkintermapview

# firebase
import firebase_admin
from firebase_admin import credentials, initialize_app, storage, db
cred = credentials.Certificate(
    "./Screens/monitoring-ground-personnel-51b9f97f5da1.json")
bucketPath = "https://monitoring-ground-personnel-default-rtdb.firebaseio.com/"
firebase_admin.initialize_app(cred, {'databaseURL': bucketPath})
ref = db.reference("/")

# loading Default predefined variables
appWidth = defVar.Variables.appWidth
appHeight = defVar.Variables.appHeight
apkBackground = defVar.Variables.appBackgroundTheme
apkBackgroundCompliment = defVar.Variables.appBackgroundCompliment


class PMS_Window(CTk):

    def __init__(self, *args, **kwargs):

        CTk.__init__(self, *args, **kwargs)

        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Agreement_Licence_Page, Login_Page, Sub_Bandobast_Area_Page, All_Bandobast_Area_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Agreement_Licence_Page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Agreement_Licence_Page(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color=apkBackground)

        pageTitle = CTkLabel(self, text="Agreement And Licence", font=(
            defVar.fontstyle.fontText, defVar.fontstyle.titleFontSize))
        pageTitle.pack(pady=10)

        textFrame = CTkFrame(self)
        textFrame.pack(expand=True)

        agreementText = CTkTextbox(textFrame, width=appWidth-400, height=appHeight -
                                   300, corner_radius=20, bg_color=apkBackground)
        agreementText.pack()
        agreementText.insert('end', '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum''')
        agreementText.configure(state="disabled")

        bottomFrame = CTkFrame(self, corner_radius=50)
        bottomFrame.pack(side='bottom', expand=True)

        button1 = CTkButton(bottomFrame, text="Next",
                            command=lambda: controller.show_frame(Sub_Bandobast_Area_Page))
        button1.pack(anchor='nw', pady=10, padx=10)


class Sub_Bandobast_Area_Page(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color=apkBackground)

        pageTitle = CTkLabel(self, text="Multi-Monitoring Page",
                             font=(defVar.fontstyle.fontText, defVar.fontstyle.titleFontSize))
        pageTitle.pack(pady=10)
        topFrame = CTkFrame(self)
        topFrame.pack(expand=True)
        search = customtkinter.CTkEntry(
            topFrame, placeholder_text="Search Bandobast Area", width=appWidth-200, text_color="black", height=40)
        searchButton = CTkButton(
            topFrame, width=200, height=40, corner_radius=10, bg_color=apkBackground)
        search.grid(row=0, column=0)
        searchButton.grid(row=0, column=1)
        textFrame = CTkFrame(self)
        textFrame.pack(expand=True)
        for id in ref.get()['Username1'].keys():
            print(id, ref.get()['Username1'].keys())
            bandobastArea = CTkButton(
                textFrame, text=id, width=appWidth - 100, height=40, fg_color=apkBackgroundCompliment)
            bandobastArea.pack(pady=(0, 10))
        bottomFrame = CTkFrame(self, corner_radius=50)
        bottomFrame.pack(side='bottom', expand=True)

        button1 = CTkButton(bottomFrame, text="Monitor All Sub-Bandobast Areas",
                            command=lambda: controller.show_frame(All_Bandobast_Area_Page), width=appWidth-1000)
        button1.pack(anchor='nw', pady=10, padx=10)


class All_Bandobast_Area_Page(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color=apkBackground)

        pageTitle = CTkLabel(self, text="Sub-Bandobast Area Screen",
                             font=(defVar.fontstyle.fontText, defVar.fontstyle.titleFontSize))
        pageTitle.pack(pady=10)
        topFrame = CTkFrame(self)
        topFrame.pack(expand=True)
        search = customtkinter.CTkEntry(
            topFrame, placeholder_text="Search Bandobast Area", width=appWidth-200, text_color="black", height=40)
        searchButton = CTkButton(
            topFrame, width=200, height=40, corner_radius=20, bg_color=apkBackground)
        search.grid(row=0, column=0)
        searchButton.grid(row=0, column=1)
        textFrame = CTkFrame(self)
        textFrame.pack(expand=True)

        def marker_click(marker):
            print(
                f"marker clicked - text: {marker.text}  position: {marker.position}")
        for key, data in ref.get()['Username1'].items():
            if type(data) == dict:
                map_widget = tkintermapview.TkinterMapView(
                    textFrame, width=300, height=300, corner_radius=15)
                map_widget.pack(fill="both", expand=True)
                for value in data.values():
                    print(value, 'Value', 'Hi', type(value))
                    if type(value) == dict:
                        map_widget.set_marker(
                            value['lat'], value['log'], text=value['Name'], command=marker_click)
        bottomFrame = CTkFrame(self, corner_radius=50)
        bottomFrame.pack(side='bottom', expand=True)

        button1 = CTkButton(bottomFrame, text="Monitor All Sub-Bandobast Areas",
                            command=lambda: controller.show_frame(Login_Page), width=appWidth-1000)
        button1.pack(anchor='nw', pady=10, padx=10)


class Login_Page(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color=apkBackground)

        pageTitle = CTkLabel(self, text="Login", font=(
            defVar.fontstyle.fontText, defVar.fontstyle.titleFontSize))
        pageTitle.pack(pady=10)

        centerFrame = CTkFrame(self)
        centerFrame.pack(padx=10, pady=10, fill='both', expand=True)

        erathImage = Image.open('./assets/Icons/earthlogo.png')
        erathImageResize = imageModulation.ImageResize(erathImage, 150, 150)
        imageLabelEarth = CTkLabel(
            centerFrame, image=erathImageResize, text="")
        imageLabelEarth.pack(pady=10)

        tokenFrame = CTkFrame(centerFrame)
        tokenFrame.pack()
        CTkLabel(tokenFrame, text="TokenId:").pack()

        tokenValue = StringVar()
        enterToken = CTkEntry(tokenFrame, textvariable=tokenValue)
        enterToken.pack(side="top")

        passwordFrame = CTkFrame(centerFrame)
        passwordFrame.pack(pady=20)
        CTkLabel(passwordFrame, text="Password").pack()
        password = StringVar()
        enterpassword = CTkEntry(
            passwordFrame, show='*', textvariable=password)
        enterpassword.pack(side="top")

        errorLabel = CTkLabel(centerFrame, text="")
        errorLabel.pack()

        logInBtn = CTkButton(centerFrame, text=" LogIn ")
        logInBtn.pack(side="top")

        CTkLabel(centerFrame, text="or").pack(pady=10)

        createBandobastArea = CTkButton(centerFrame, text=" Create new Token ")
        createBandobastArea.pack(side="top")

        button1 = CTkButton(self, text="Back", command=lambda: controller.show_frame(
            Agreement_Licence_Page))
        button1.pack(anchor='nw', pady=10, padx=10)


# Main Window Settings
# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")

app = PMS_Window()  # create CTk window like you do with the Tk window
app.geometry(f'{appWidth}x{appHeight}')
app.maxsize(appWidth, appHeight)
app.minsize(appWidth-200, appHeight-100)

app.title('PMS')

app.mainloop()
