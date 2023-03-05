#Script made by Colin Campbell
#The script takes the x and y list for each letter in a word
#That word will be displayed on the Ti-84 graph using lines
#The script outputs the code that needs to be copied into the Ti-Connect program
#That program then is transfered to calculator for use.



placeHolder = 0
#Capital letters [max-x is 4, max-y is 10]
#Lowercase letters [max-x is 3, max-y is 5]
#Current list
#Capital -FIL
#Lowercase - cku
Fx = [0,0,4,4,2,2,4,4,2,2,0,4]
Fy = [0,10,10,8,8,6,6,4,4,0,0,0]
ux = [0,0,.75,.75,2.25,2.25,3,3,0,3]
uy = [0,5,5,2,2,5,5,0,0,0]
cx = [0,0,3,3,1,1,3,3,0,3]
cy = [0,5,5,4,4,1,1,0,0,0]
kx = [0,0,1,1,2,3,1,1,3,2,1,1,0,3]
ky = [0,5,5,4,5,5,3,2,0,0,1,0,0,0]
Ix = [0,0,1.5,1.5,0,0,4,4,2.5,2.5,4,4,0,4]
Iy = [0,2,2,8,8,10,10,8,8,2,2,0,0,0]
Lx = [0,0,1.5,1.5,4,4,0,4]
Ly = [0,10,10,1.5,1.5,0,0,0]
ox = [0,0,3,3,0,1,1,2,2,1,0,3]
oy = [0,5,5,0,0,1.5,3.5,3.5,1.5,1.5,0,0]
vx = [1,0,0.75,1.25,1.75,2.25,3,2,1,3]
vy = [0,5,5,2,2,5,5,0,0,0]
ex = [0,0,3,2,2,1,1,2,3,3,1,1,3,3,0,3]
ey = [0,5,5,4,3,3,4,4,5,2,2,1,1,0,0,0]
Yx = [1.5,1.5,0,1,2,3,4,2.5,2.5,1.5,4]
Yy = [0,4,10,10,5,10,10,4,0,0,0]

x = []
y = []
def letter(letterx,lettery,placeHolder):
    for i in range(len(letterx)):
        x.append(str(letterx[i]) + "F+"+ str(placeHolder)+"F")
    for i in range(len(lettery)):
        y.append(str(lettery[i]) + "F")
    placeHolder+=5
    return placeHolder

placeHolder = letter(Fx,Fy,placeHolder)
placeHolder = letter(ux,uy,placeHolder)
placeHolder = letter(cx,cy,placeHolder)
placeHolder = letter(kx,ky,placeHolder)

print("{"+",".join(x)+"}→L₁")
print("{"+",".join(y)+"}→L₂")