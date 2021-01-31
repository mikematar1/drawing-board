import pygame,sys
pygame.init()
screen=pygame.display.set_mode((700,700))
bg=pygame.image.load("white.jpg")
bg=pygame.transform.scale(bg,(700,700))
motion=[]
colors=[(255,0,0),(0,255,0),(255,255,255)]
colors_pos=[(30,50),(60,50),(90,50)]
draw=False
erase=False
color=colors[0]
pygame.Color(255,0,0)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            a=pygame.mouse.get_pos()
            for b in colors_pos:
                if ((a[0]-b[0])**2+(a[1]-b[1])**2)<=10**2:
                    color=colors[colors_pos.index(b)]

            erase=False
            draw=True
        elif event.type==pygame.MOUSEBUTTONUP:
            draw=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_f:
                erase=True
                draw=False
    if erase:
        a=pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(a),10)
    
    if draw:
        a=pygame.mouse.get_pos()
        pygame.draw.circle(screen,color,(a),10)
    
    for x in range(len(colors_pos)):
        pygame.draw.circle(screen,(colors[x]),(colors_pos[x]),10)
    
    pygame.display.update()
