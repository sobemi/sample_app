import tkinter
import sys

root = tkinter.Tk()
root.title("DENTAKU")
root.geometry("400x300")

#�{�^������
def DeleteEntryValue(event):
    EditBox.delete(0,tkinter.END)
#

#���x��
Static1 = tkinter.Label(text="test")
Static1.pack()

#���̓{�b�N�X
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"�}�����镶����")
EditBox.pack()

value = EditBox.get()


#�{�^��
Button = tkinter.Button(text="�{�^��")
Button.pack()

Button.bind("<Button-1>",DeleteEntryValue)

#�`�F�b�N�{�b�N�X

Val1=tkinter.BooleanVar()
Val1.set(True)

CheckBox = tkinter.Checkbutton(text="���ڂP",variable=Val1)
CheckBox.pack()

#�`�F�b�N�l�擾
if Val1.get() == True:
    
else:


root.mainloop()