import random
import numpy as np
import tkinter
import turtle

def readDataFromFileWithGraphAndGenerateAdjacentMatrixForColoringNodes() :
    with open("coloringNodes.in","r") as file :
        lines = file.readlines()
        elements = lines[0].split(" ")
        global nodes1
        nodes1 = int(elements[0])
        global edges1
        edges1 = int(elements[1])
        global colors1
        colors1 = int(elements[2])
        global a
        a = np.zeros((nodes1, nodes1))
        for i in range(1, edges1 + 1) :
            elements = lines[i].split(" ")
            x = int(elements[0])
            y = int(elements[1])
            a[x - 1][y - 1] = 1
            a[y - 1][x - 1] = 1

def readColorsFromFileForColoringNodes() :
    with open("colors.in", "r") as file :
        colorsText = file.readline()
        elements = colorsText.split(" ")
        global colorValue
        colorValue = elements.__len__()
        global colorsTextList1
        colorsTextList1 = []
        for color in elements :
            colorsTextList1.append(color)

def validNodes(x, k) :
    for i in range(0, k) :
        if a[i][k] >= 1 and x[i] == x[k] :
            return 0
    return 1

def displayNodes(x) :
    for i in range(0, nodes1) :
        print(x[i])
    print()

def coloringNodes(x) :
    global graphOut
    graphOut = open("coloringNodes.out", "w")
    graphOut.write("The solutions associated with the color generation algorithm are: \n")
    k = 0
    x[0] = 0
    global s
    s = np.zeros((10000, nodes1))
    global numberOfSolutions 
    numberOfSolutions = 0
    while(k >= 0) :
        if x[k] < colors1 :
            x[k] = x[k] + 1
            if validNodes(x, k) :
                if k == nodes1 - 1 :
                    for j in range(nodes1) :
                        s[numberOfSolutions][j] = x[j]
                    numberOfSolutions = numberOfSolutions + 1
                    graphOut.write(str(numberOfSolutions) + " => " + str(x) + "\n")
                else :
                    k = k + 1
                    x[k] = 0
        else :
            k = k - 1

def createNodesAndEdgesDesignForColoringNodes() :
    global p
    p = np.zeros((nodes1, 2))
    global colorsChosen
    colorsChosen = []
    if numberOfSolutions > 0 and colors1 == edges1 - nodes1 - 1 :
        value = random.randint(1, numberOfSolutions)
        print("The arbitrarily chosen list for coloring the graph has the value: " + str(value + 1))
        for i in range(nodes1) :
            colorsChosen.append(colorsTextList1[(int(s[value][i]) - 1)])
        graphOut.write("\n")
        graphOut.write("The chosen solution and its associated colors are: ")
        graphOut.write(str(value + 1) + " => " + str(colorsChosen))
        global element
        element = turtle.Turtle()
        style = ('Times New Roman', 30, "normal")
        global position
        position = 2
        point1 = 0
        point2 = 200
        element.penup()
        element.screen.bgcolor("sandybrown")
        for i in range(nodes1) :
            p[i][0] = point1
            p[i][1] = point2
            element.pensize(4)
            element.begin_fill()
            element.color = colorsChosen[i]
            element.goto(point1, point2)
            element.pendown()
            element.fillcolor(colorsChosen[i])
            element.write(i + 1, font=style, align="center")
            element.circle(25)
            element.penup()
            point1 = point1 + 250
            if (i + 1) % position == 0 :
                point1 = 0
                point2 = point2 - 150
            element.end_fill()
        element.penup()
        for i in range(nodes1) :
            for j in range(nodes1) :
                if a[i][j] == 1 and i % 2 == 0 and j % 2 == 0 :
                    point1 = p[i][0]
                    point2 = p[i][1]
                    point3 = p[j][0]
                    point4 = p[j][1]
                    element.pensize(4)
                    element.goto(point1, point2)
                    element.pendown()
                    element.circle((point4 - point2) / 2, -180)
                    element.penup()
                    element.left(180)
                    element.penup()
                    a[j][i] = 0
                else :
                    if a[i][j] == 1 and i % 2 == 1 and j % 2 == 1 :
                        point1 = p[i][0]
                        point2 = p[i][1]
                        point3 = p[j][0]
                        point4 = p[j][1]
                        element.pensize(4)
                        element.goto(point1, point2)
                        element.pendown()
                        element.circle((point4 - point2) / 2, 180)
                        element.penup()
                        element.right(180)
                        element.penup()
                        a[j][i] = 0
                    else :
                        if a[i][j] == 1 :
                            point1 = p[i][0]
                            point2 = p[i][1]
                            point3 = p[j][0]
                            point4 = p[j][1]
                            element.penup()
                            element.goto(point1, point2)
                            element.pendown()
                            element.goto(point3, point4)
                            element.penup()
                            a[j][i] = 0
        element.hideturtle()                    
        drawingArea = turtle.Screen() 
        drawingArea.exitonclick()
    else :
        tkinter.messagebox.showinfo("Warning", "The number of colors is not correct!")

def readDataFromFileWithGraphAndGenerateAdjacentMatrixForColoringEdges() :
    with open("coloringEdges.in","r") as file :
        lines = file.readlines()
        elements = lines[0].split(" ")
        global nodes2
        nodes2 = int(elements[0])
        global edges2
        edges2 = int(elements[1])
        global colors2
        colors2 = int(elements[2])
        global a
        a = np.zeros((nodes2, nodes2))
        for i in range(1, edges2 + 1) :
            elements = lines[i].split(" ")
            x = int(elements[0])
            y = int(elements[1])
            a[x - 1][y - 1] = 1
            a[y - 1][x - 1] = 1

def readColorsFromFileForColoringEdges() :
    with open("colors.in", "r") as file :
        colorsText = file.readline()
        elements = colorsText.split(" ")
        global colorValue
        colorValue = elements.__len__()
        global colorsTextList2
        colorsTextList2 = []
        for color in elements :
            colorsTextList2.append(color)

def verifyIfColorIsUniqueOnLine(k, p) :
    nr = 0
    element = b[k][p]
    for j in range(nodes2) :
        if b[k][j] >= 0 and element == b[k][j] :
            nr = nr + 1
    if (nr > 1) :
        return 0
    return 1

def verifyIfColorIsUniqueOnColumn(k, p) :
    nr = 0
    element = b[k][p]
    for i in range(nodes2) :
        if b[i][p] >= 0 and element == b[i][p] :
             nr = nr + 1
    if (nr > 1) :
        return 0
    return 1

def verifyIfAllElementsAreUniqueOnLineAndOnColumn() :
    nr = 0
    for i in range(nodes2) :
        nr1 = 0
        nr2 = 0
        for j in range(nodes2) :
            if a[i][j] == 1 :
                if verifyIfColorIsUniqueOnLine(i, j) == 1 :
                    nr1 = nr1 + 1
                if verifyIfColorIsUniqueOnColumn(i, j) == 1 :
                    nr2 = nr2 + 1
        if nr1 == nr2 :
            nr = nr + 1
    if (nr == nodes2) :
        return 1
    return 0
        
def createInitialMatrixForEdges() :
    global b
    b = np.zeros((nodes2, nodes2))
    value = []
    for i in range(colors2) :
        value.append(i)

    for i in range(nodes2) :
        b[i][i] = -1

    for i in range(0, nodes2 - 1) :
        p = -1 
        for j in range(i + 1, nodes2) :
            if a[i][j] == 1 and i == 0:  
                p = p + 1     
                b[i][j] = value[p]
                b[j][i] = value[p]
            else :
                if a[i][j] == 1 and i > 0 :
                    b[i][j] = 1
                    b[j][i] = 1
                else :
                    if a[i][j] != 1 :
                        b[i][j] = -1
                        b[j][i] = -1

def createFinalMatrixForEdges() :
    listOfColors = []
    for i in range(colors2) :
        listOfColors.append(i)
    for i in range(1, nodes2) :
        k = 0
        for j in range(1, nodes2) :
            if a[i][j] == 1 and b[i][j] >= 1 :
                if verifyIfColorIsUniqueOnLine(i, j) == 0 and verifyIfColorIsUniqueOnColumn(i, j) == 0 :
                    k = k + 1
                    b[i][j] = b[i][j] + k
                    b[j][i] = b[j][i] + k
                else :
                    b[i][j] = 0
                    b[j][i] = 0

    for i in range(1, nodes2 - 1) :
        for j in range(i + 1, nodes2) :
            if a[i][j] == 1 :
                if verifyIfColorIsUniqueOnLine(i, j) == 0 or verifyIfColorIsUniqueOnColumn(i, j) == 0 :
                    for k in range(0, len(listOfColors)):
                        b[i][j] = listOfColors[k]
                        b[j][i] = listOfColors[k]
                        if verifyIfColorIsUniqueOnLine(i, j) == 1 and verifyIfColorIsUniqueOnColumn(i, j) == 1 :
                            break

def createNodesAndEdgesDesignForColoringEdges() :
    global p
    p = np.zeros((nodes2, 2))
    global colorsChosen
    colorsChosen = []
    if colors2 == edges2 - nodes2 + 1 :
        for i in range(len(colorsTextList2)) :
            colorsChosen.append(colorsTextList2[i])
        global element
        element = turtle.Turtle()
        style = ('Times New Roman', 30, "normal")
        global position
        position = 2
        point1 = 0
        point2 = 200
        element.penup()
        element.screen.bgcolor("sandybrown")
        for i in range(nodes2) :
            p[i][0] = point1
            p[i][1] = point2
            element.pensize(3)
            element.begin_fill()
            element.goto(point1, point2)
            element.pendown()
            element.fillcolor("gray")
            element.write(i + 1, font=style, align="center")
            element.circle(25)
            element.penup()
            point1 = point1 + 250
            if (i + 1) % position == 0 :
                point1 = 0
                point2 = point2 - 150
            element.end_fill()
        element.penup()
        for i in range(nodes2) :
            for j in range(nodes2) :
                if a[i][j] == 1 and i % 2 == 0 and j % 2 == 0 :
                    point1 = p[i][0]
                    point2 = p[i][1]
                    point3 = p[j][0]
                    point4 = p[j][1]
                    element.goto(point1, point2)
                    element.pensize(4)
                    element.pencolor(colorsTextList2[int(b[i][j])])
                    element.pendown()
                    element.circle((point4 - point2) / 2, -180)
                    element.penup()
                    element.left(180)
                    element.penup()
                    a[j][i] = 0
                else :
                    if a[i][j] == 1 and i % 2 == 1 and j % 2 == 1 :
                        point1 = p[i][0]
                        point2 = p[i][1]
                        point3 = p[j][0]
                        point4 = p[j][1]
                        element.goto(point1, point2)
                        element.pensize(4)
                        element.pencolor(colorsTextList2[int(b[i][j])])
                        element.pendown()
                        element.circle((point4 - point2) / 2, 180)
                        element.penup()
                        element.right(180)
                        element.penup()
                        a[j][i] = 0
                    else :
                        if a[i][j] == 1 :
                            point1 = p[i][0]
                            point2 = p[i][1]
                            point3 = p[j][0]
                            point4 = p[j][1]
                            element.penup()
                            element.goto(point1, point2)
                            element.pensize(4)
                            element.pencolor(colorsTextList2[int(b[i][j])])
                            element.pendown()
                            element.goto(point3, point4)
                            element.penup()
                            a[j][i] = 0
        element.hideturtle()                    
        drawingArea = turtle.Screen() 
        drawingArea.exitonclick()
    else :
        tkinter.messagebox.showinfo("Warning", "The number of colors is not correct!")

def chooseTheColoringNodes() :
    readDataFromFileWithGraphAndGenerateAdjacentMatrixForColoringNodes()
    readColorsFromFileForColoringNodes()
    x = np.zeros((nodes1))
    coloringNodes(x)
    createNodesAndEdgesDesignForColoringNodes()

def chooseTheColoringEdges() :
    readDataFromFileWithGraphAndGenerateAdjacentMatrixForColoringEdges()
    readColorsFromFileForColoringEdges()
    createInitialMatrixForEdges()
    createFinalMatrixForEdges()
    createNodesAndEdgesDesignForColoringEdges()

if __name__ == "__main__":
    
    element = tkinter.Tk()
    element.attributes('-fullscreen', True)

    CN = tkinter.Button(element, text ="Button for coloring nodes!", command = chooseTheColoringNodes)  
    CN.pack()
    CN.place(x = 550, y = 200)

    CE = tkinter.Button(element, text ="Button for coloring edges!", command = chooseTheColoringEdges)
    CE.pack()
    CE.place(x = 550, y = 400)

    CL = tkinter.Button(element, text ="Button for closing app!", command = element.destroy)
    CL.pack()
    CL.place(x = 550, y = 600)

    element.mainloop()