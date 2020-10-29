import pygame,sys,time,random

pygame.init()
size = width, height = 1000, 500
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
black = 0, 0, 0
gray = 150,150,150
white = 255,255,255
green = 0, 255,0
red = 255,0,0
blue = 0,0,255
yellow = 255, 255,0
font = pygame.font.SysFont('Comic Sans MS',32)
x = 50
y = 490
w=20
swaps= False
def iSort():
    arr = [[random.randint(1,150),False] for n in range(45)]
    i=1
    j=i
    while i < len(arr):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Insertion Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
        rect = pygame.Rect(x+j*w,y,w,-arr[j][0]*3)
        pygame.draw.rect(screen,green,rect,2)
        rect2 = pygame.Rect(x+(j-1)*w,y,w,-arr[j-1][0]*3)
        pygame.draw.rect(screen,red,rect2,2)
        if arr[j] < arr[j-1]:
            pygame.draw.rect(screen,black,rect,2)
            pygame.draw.rect(screen,black,rect2,2)
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            rect = pygame.Rect(x+j*w,y,w,-arr[j][0]*3)
            pygame.draw.rect(screen,red,rect,2)
            rect2 = pygame.Rect(x+(j-1)*w,y,w,-arr[j-1][0]*3)
            pygame.draw.rect(screen,green,rect2,2)
            if j-1 > 0:
                j-=1
            else:
                i+=1
                j=i
        else:
            i+=1
            j=i
    
        pygame.display.flip()
        clock.tick(30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Insertion Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            pygame.draw.rect(screen,blue,rect,2)

            x+=w
        x=50
        pygame.display.flip()
        clock.tick(30)

def sSort():
    arr = [[random.randint(1,150),False] for n in range(45)]
    i=0
    temp=0
    j=1
    ind=0
    while i < len(arr):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Selection Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
        rect = pygame.Rect(x+i*w,y,w,-arr[i][0]*3)
        pygame.draw.rect(screen,yellow,rect,2)
        rect = pygame.Rect(x+ind*w,y,w,-arr[ind][0]*3)
        pygame.draw.rect(screen,green,rect,2)
        rect = pygame.Rect(x+j*w,y,w,-arr[j][0]*3)
        pygame.draw.rect(screen,red,rect,2)
        if (arr[ind] > arr[j]):
            ind = j
        if j+1 < len(arr):
            j+=1
        else:
            temp = arr[i]
            arr[i] = arr[ind]
            arr[ind] = temp
            arr[i][1]=True
            i+=1
            ind=i
            if i+1 != len(arr):
                j=i+1
        pygame.display.flip()
        clock.tick(30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Selection Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
        pygame.display.flip()
        clock.tick(30)
    

def bSort():
    arr = [[random.randint(1,150),False] for n in range(45)]
    i= len(arr)
    j=0
    swaps= False
    while i > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Bubble Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
        rect = pygame.Rect(x+j*w,y,w,-arr[j][0]*3)
        pygame.draw.rect(screen,green,rect,2)
        rect2 = pygame.Rect(x+(j+1)*w,y,w,-arr[j+1][0]*3)
        pygame.draw.rect(screen,red,rect2,2)
        if (arr[j] > arr[j + 1]):
            pygame.draw.rect(screen,black,rect,2)
            pygame.draw.rect(screen,black,rect2,2)
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            swaps = True
            rect = pygame.Rect(x+j*w,y,w,-arr[j][0]*3)
            pygame.draw.rect(screen,red,rect,2)
            rect2=pygame.Rect(x+(j+1)*w,y,w,-arr[j+1][0]*3)
            pygame.draw.rect(screen,green,rect2,2)

        if j+1 < i-1:
            j+=1
        else:
            arr[j+1][1]=True
            i-=1
            j=0
        if i == 0:
            arr[0][1] = True
        pygame.display.flip()
        clock.tick(30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Bubble Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
        pygame.display.flip()
        clock.tick(30)

def merge(arr,l1,r1,l2,r2):
    temp = []
    x=50
    while l1 <=r1 and l2 <=r2:
        if arr[l1] <= arr[l2]:
            temp.append(arr[l1])
            l1+=1
        else:
            temp.append(arr[l2])
            l2+=1

    while l1 <=r1:
        temp.append(arr[l1])
        l1+=1
    while l2 <=r2:
        temp.append(arr[l2])
        l2+=1
    return temp
	
def mSort():
    arr = [[random.randint(1,150),False] for n in range(45)]
    l = 1
    n = len(arr)
    i=0
    while l < n:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Merge Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
        if i < n:
            l1 =i
            r1=i+l-1
            l2=i+l
            r2= i+2*l-1
            if l2 >=n:
                l = 2*l
                i=0
                continue
            if r2>= n:
                r2=n-1
            rectl = pygame.Rect(x+l1*w,y,w,-arr[l1][0]*3)
            pygame.draw.rect(screen,green,rectl,2)
            rectlr=pygame.Rect(x+r1*w,y,w,-arr[r1][0]*3)
            pygame.draw.rect(screen,red,rectlr,2)
            rectr = pygame.Rect(x+l2*w,y,w,-arr[l2][0]*3)
            pygame.draw.rect(screen,red,rectr,2)
            rectrr=pygame.Rect(x+r2*w,y,w,-arr[r2][0]*3)
            pygame.draw.rect(screen,green,rectrr,2)
            temp=merge(arr,l1,r1,l2,r2)
            for j in range(r2-l1+1):
                arr[i+j]=temp[j]
            i+=2*l
        else:
            l = 2*l
            i=0
        pygame.display.flip()
        clock.tick(10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Merge Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            pygame.draw.rect(screen,blue,rect,2)
           
            x+=w
        x=50
        pygame.display.flip()
        clock.tick(30)

def partition(arr, l, h): 
    i = ( l - 1 ) 
    x = arr[h] 
    
    for j in range(l, h): 
        if arr[j] <= x: 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1)
def qSort():
    arr = [[random.randint(1,150),False] for n in range(45)]
    size = len(arr)
    stack = [0] * (size) 
    l=0
    h= size-1
    top = -1
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Quick Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            if r[1]:
                pygame.draw.rect(screen,blue,rect,2)
            else:
                pygame.draw.rect(screen,gray,rect,2)
            x+=w
        x=50
  
        # Set pivot element at its correct position in 
        # sorted array 
        rect = pygame.Rect(x+l*w,y,w,-arr[l][0]*3)
        pygame.draw.rect(screen,green,rect,2)
        rect2=pygame.Rect(x+h*w,y,w,-arr[h][0]*3)
        pygame.draw.rect(screen,red,rect2,2)
        p = partition( arr, l, h ) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
        pygame.display.flip()
        clock.tick(10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        draw_text("Quick Sort",font,white,screen,390,10)
        x=50
        for r in arr:
            rect = pygame.Rect(x,y,w,-r[0]*3)
            pygame.draw.rect(screen,blue,rect,2)
           
            x+=w
        x=50
        pygame.display.flip()
        clock.tick(30)

#arr = [1,2,3,10,3,4,5,6,7]
def draw_text(text,font,color,surface,x,y):
    text_obj =font.render(text,1,color)
    text_rect =text_obj.get_rect()
    text_rect.topleft =(x,y)
    surface.blit(text_obj,text_rect)

click = False       
def menu():
    while True:
        screen.fill(black)
        draw_text("Sorting Vizualizer",font,white,screen, 390,10)
        draw_text("Press 'Space' to quit main menu or Algorithm",font,white,screen, 290,460)

        mx,my = pygame.mouse.get_pos()
        
        bSort_button = pygame.Rect(170,50,200,50)
        sSort_button = pygame.Rect(170,150,200,50)
        iSort_button = pygame.Rect(170,250,200,50)
        mSort_button = pygame.Rect(170,350,200,50)
        qSort_button = pygame.Rect(600,50,200,50)
        if bSort_button.collidepoint((mx,my)):
            if click:
                bSort()
        if sSort_button.collidepoint((mx,my)):
            if click:
                sSort()
        if iSort_button.collidepoint((mx,my)):
            if click:
                iSort()
        if mSort_button.collidepoint((mx,my)):
            if click:
                mSort()
        if qSort_button.collidepoint((mx,my)):
            if click:
                qSort()
        pygame.draw.rect(screen,blue,bSort_button)
        pygame.draw.rect(screen,blue,sSort_button)
        pygame.draw.rect(screen,blue,iSort_button)
        pygame.draw.rect(screen,blue,mSort_button)
        pygame.draw.rect(screen,blue,qSort_button)
        draw_text("Bubble Sort",font,white,screen, 205,65)
        draw_text("Selection Sort",font,white,screen, 195,165)
        draw_text("Insertion Sort",font,white,screen, 195,265)
        draw_text("Merge Sort",font,white,screen, 205,365)
        draw_text("Quick Sort",font,white,screen, 645,65)
        click =False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click= True
        pygame.display.flip()
        clock.tick(30)
menu()