import tkinter as tk

app= tk.Tk()

app.geometry("600x300")
app.configure(background="lightblue")
tk.Wm.wm_title(app, "App de prueba")
entrada=tk.StringVar(app)
entrada2=tk.StringVar(app)
entrada3=tk.StringVar(app)

def cifCesar(mens,desp):
    res=""
    for i in mens:
        codascii= ord(i)
        ncod=codascii+desp
        if codascii>96 and codascii<123:
            if ncod>122:
                ncod-=26
            elif ncod<97:
                ncod+=26
        res+=chr(ncod)
    return res

text=entrada.get()
textvariable=entrada2.get()
textvariable2=entrada3.get()
    

tk.Label(
    app,
    text="Cifrador de cesar",
    font=("Verdana", 20),
    fg="gray",
    bg="lightblue",
).pack()

tk.Label(
    app,
    text="Ingrese el desplazamiento del cifrado",
    font=("Verdana", 20),
    fg="gray",
    bg="lightblue",
).pack()

tk.Entry(
    app,
    text=entrada,
    font=("Courier", 14),
    bg="white",
    fg="black"
).pack(
   expand=True 
)
tk.Label(
    app,
    text="Ingrese la palabra para cifrar",
    font=("Verdana", 20),
    fg="gray",
    bg="lightblue",
).pack()
    
tk.Entry(
    app,
    textvariable=entrada2,
    font=("Courier", 14),
    bg="white",
    fg="black"
).pack(
   expand=True 
)

tk.Button(
    app,
    text="cifrar",
    font=("Courier", 14),
    bg="purple",
    fg="black",
    command=cifradoCesar
).pack(
   expand=True
)

tk.Label(
    app,
    text="La palabra cifrada es : ",
    font=("Verdana", 20),
    fg="gray",
    bg="lightblue",
).pack()
    
tk.Entry(
    app,
    textvariable2=entrada3,
    font=("Courier", 14),
    bg="white",
    fg="black"
).pack(
   expand=True 
)

app.mainloop()