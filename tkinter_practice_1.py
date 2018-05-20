import tkinter
import sys

root = tkinter.Tk()
root.title("DENTAKU")
root.geometry("400x300")

#ボタン処理
def DeleteEntryValue(event):
    EditBox.delete(0,tkinter.END)
#

#ラベル
Static1 = tkinter.Label(text="test")
Static1.pack()

#入力ボックス
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"挿入する文字列")
EditBox.pack()

value = EditBox.get()


#ボタン
Button = tkinter.Button(text="ボタン")
Button.pack()

Button.bind("<Button-1>",DeleteEntryValue)

#チェックボックス

Val1=tkinter.BooleanVar()
Val1.set(True)

CheckBox = tkinter.Checkbutton(text="項目１",variable=Val1)
CheckBox.pack()

#チェック値取得
if Val1.get() == True:
    
else:


root.mainloop()