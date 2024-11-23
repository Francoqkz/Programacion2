import tkinter as tk

app= tk.Tk()

app.geometry("600x300")
app.configure(background="lightblue")
tk.Wm.wm_title(app, "App de prueba")
entrada=tk.StringVar(app)

def saludar():
    print("HOLAAAAAAA " + entrada.get())

tk.Label(
    app,
    text="Ola soy una etiqueta",
    font=("Verdana", 20),
    fg="gray",
    bg="lightblue",
).pack()

tk.Button(
    app,
    text="Click aqui!!!",
    font=("Courier", 14),
    bg="purple",
    fg="black",
    command=saludar
).pack(
    fill=tk.BOTH,
    expand=True    
)
    
tk.Entry(
    app,
    textvariable=entrada,
    font=("Courier", 14),
    bg="white",
    fg="black"
).pack(
   expand=True 
)
app.mainloop()