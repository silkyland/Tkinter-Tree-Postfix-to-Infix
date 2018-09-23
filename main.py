import os
import glob
import sys
import time
import tkinter
from tkinter import ttk

from pythonds.basic.stack import Stack


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            operandStack.push([token, operand1, operand2])
    return operandStack.pop()




root = tkinter.Tk()


vsb = ttk.Scrollbar(orient="vertical")
hsb = ttk.Scrollbar(orient="horizontal")

def autoscroll(sbar, first, last):
    """Hide and show scrollbar as needed."""
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)


tree = ttk.Treeview(columns=("fullpath", "type", "size"),
                    displaycolumns="size", yscrollcommand=lambda f, l: autoscroll(vsb, f, l),
                    xscrollcommand=lambda f, l: autoscroll(hsb, f, l))

vsb['command'] = tree.yview
hsb['command'] = tree.xview

tree.heading("#0", text="Directory Structure", anchor='w')
tree.heading("size", text="File Size", anchor='w')
tree.column("size", stretch=0, width=100)


def assignTree(treeList, node=""):
    loop = 0
    for item in treeList:
        if type(item) == list:
            assignTree(item, node)
            loop = 0
        else:
            if loop > 0:
                tree.insert(node, 'end', text=item)
            else:
                node = tree.insert(node, 'end', text=item)
            loop += 1
arrayList = postfixEval('2 5 3 + *')

print(arrayList)
assignTree(arrayList)

tree.pack()
root.mainloop()
