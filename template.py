#####################################################################
################## Import necessary libraries #######################
#####################################################################
import os
from os import system
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import datetime
import sqlite3
from pyglet import font
font.add_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\fonts\\UbuntuMono-BoldItalic.ttf"))


#####################################################################
################## Path Specifications ##############################
#####################################################################
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("..\\assets\\loginPage")


#####################################################################
################## Functions ########################################
#####################################################################
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def log(text):
    with open('..\\logs\\log.txt','a') as f:
            f.write(f"{datetime.datetime.now()}: {text}: login.py\n")

def submit():
    username = entry_1.get()
    password = entry_2.get()
    if username == "" or password=="":
        messagebox.showerror("Error", "Please fill all the fields")
    elif username != "" and password!="":
        conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\database\\mainDb.db"))
        c = conn.cursor()
        c.execute(f"select password from users where username=\"{username}\"")
        out = c.fetchall()
        conn.commit()
        realPass = str(out)[3:-4]
        if password==realPass:
            log("Logged in as "+ username)
            print("Logged in as "+ username)
            with open('..\\logs\\currentUser.txt','w') as f:
                f.write(username)
            window.destroy()
            windowDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainPage.py")
            system(f"py \"{windowDIR}\"")
            exit()
    else:
        messagebox.showerror("Error", "Incorrect Username or Password")
        log("Attempted to login as "+ username)
        print("Attempted to login as "+ username)

def register():
    log("Entered register page")
    print("Entered register page")
    window.destroy()
    windowDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "register.py")
    system(f"py \"{windowDIR}\"")
    exit()

def about():
    log("Entered about page")
    print("Entered about page")
    window.destroy()
    windowDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "about.py")
    system(f"py \"{windowDIR}\"")
    exit()

def program():
    log("Entered program page")
    print("Entered program page")
    window.destroy()
    windowDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "program.py")
    system(f"py \"{windowDIR}\"")
    exit()

def donate():
    log("Entered donate page")
    print("Entered donate page")
    window.destroy()
    windowDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "donate.py")
    system(f"py \"{windowDIR}\"")
    exit()

def team():
    log("Entered team page")
    print("Entered team page")
    window.destroy()
    windowDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "team.py")
    system(f"py \"{windowDIR}\"")
    exit()


#####################################################################
################## Window Instance ##################################
#####################################################################
window = Tk()
window.geometry("1270x720")
window.resizable(False, False)
window.configure(bg = "#FEDFB1")


#####################################################################
################## Design Canvas ####################################
#####################################################################
canvas = Canvas(
    window,
    bg = "#FEDFB1",
    height = 720,
    width = 1270,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    155.0,
    41.0,
    image=image_image_1
)

#username entry
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    606.0,
    341.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FEDFB1",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=407.0,
    y=314.0,
    width=398.0,
    height=53.0
)

#password entry
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    606.0,
    483.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FEDFB1",
    fg="#000716",
    highlightthickness=0,
    show = "*"
)
entry_2.place(
    x=407.0,
    y=456.0,
    width=398.0,
    height=53.0
)




button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
DonateButton = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: donate(), #donate button
    relief="flat"
)
DonateButton.place(
    x=1084.0,
    y=16.0,
    width=142.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
TeamButton = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: team(), #team button
    relief="flat"
)
TeamButton.place(
    x=861.0,
    y=16.0,
    width=142.0,
    height=51.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
ProgramButton = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: program(), #program button
    relief="flat"
)
ProgramButton.place(
    x=719.0,
    y=16.0,
    width=142.0,
    height=51.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
AboutButton = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: about(), #about button
    relief="flat"
)
AboutButton.place(
    x=577.0,
    y=16.0,
    width=142.0,
    height=51.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    634.0,
    360.0,
    image=image_image_2
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
SubmitButton = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit(), #submit button
    relief="flat"
)
SubmitButton.place(
    x=435.0,
    y=526.0,
    width=142.0,
    height=51.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
RegisterButton = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: register(), #register button
    relief="flat"
)
RegisterButton.place(
    x=648.0,
    y=526.0,
    width=157.0,
    height=51.0
)

canvas.create_text(
    555.0,
    168.0,
    anchor="nw",
    text="Login",
    fill="#61351C",
    font=("UbuntuMono BoldItalic", 64 * -1)
)

canvas.create_text(
    404.0,
    270.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("UbuntuMono Bold", 24 * -1)
)

canvas.create_text(
    404.0,
    412.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("UbuntuMono Bold", 24 * -1)
)




#####################################################################
################### Driver ##########################################
#####################################################################
window.mainloop()