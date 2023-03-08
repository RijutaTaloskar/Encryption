from tkinter import*

root=Tk()
root.title("Encryption")

root.geometry("400x400")
root.configure(background = 'snow')

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely=0.4, anchor=CENTER)

label_ascii = Label(root, text = "Type the word : ", bg = "light blue", fg = "black")
label_encrypt = Label(root, text = "Generated encrypted", bg = "light yellow", fg="green")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        
        def encrypt():
            ascii = int(ord(letter))
            encrypted = ascii - 1
            label_encrypt["text"] += str(chr(encrypted))
            
btn=Button(root, text="Show name in Ascii and excrypted" , command=asciiConverter, bg='gold', fg="green")
btn.place(relx=0.5, rely=0.6,anchor=CENTER)

label_ascii.pack()
label_encrypt.pack()
btn.pack()

root.mainloop()