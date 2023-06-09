# By Alberto Caro S.
# Ing. Civil en Computacion
# Doctor(c) Cs. de la Computacion
# Pontificia Universidad Catolica de Chile
# Programacion de Robot -> INFO1139
#---------------------------------------------------------------------
#__________      ___.           __  .__               
#\______   \ ____\_ |__   _____/  |_|__| ____ _____   
# |       _//  _ \| __ \ /  _ \   __\  |/ ___\\__  \  
# |    |   (  <_> ) \_\ (  <_> )  | |  \  \___ / __ \_
# |____|_  /\____/|___  /\____/|__| |__|\___  >____  /
#        \/           \/                    \/     \/ 
#---------------------------------------------------------------------
import pygame as PG, time as Ti, random as RA, ctypes as ct
from pygame.locals import *

#---------------------------------------------------------------------
# Definicion de Constantes Globales
#---------------------------------------------------------------------
nRES = (960,640); nTW_X = nTH_Y = 32 ; nMx = nMy = 0 ; lOK = True 
Map1_X = 0
Map1_Y = 0
Map2_X = 0
Map2_Y = 0
Map3_X = 0
Map3_Y = 0
#---------------------------------------------------------------------
# Definicion de Structura
#---------------------------------------------------------------------
class eRobots(ct.Structure):
 _fields_ = [
             ('nF',ct.c_short),
             ('nX',ct.c_short),
             ('nY',ct.c_short),
             ('nR',ct.c_short),
             ('dX',ct.c_short),
             ('dY',ct.c_short),
	   ('nV',ct.c_short)
            ]

#---------------------------------------------------------------------
# Carga imagenes y convierte formato PG
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except PG.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PGs.-
#---------------------------------------------------------------------
def PyGame_Init():
    PG.init()
    PG.mouse.set_visible(False) 
    PG.display.set_caption('Dynamic Big Map 2D - By Alberto Caro')
    return PG.display.set_mode(nRES) 

#---------------------------------------------------------------------
# Inicilaiza parametros de los Robots
#---------------------------------------------------------------------
def Init_Robots():
    return

#---------------------------------------------------------------------
# Pinta los Robots en el Super Extra Mega Mapa.-
# Se pintan los Robots en Surface -> sMapa (6400 x 480)
#---------------------------------------------------------------------
def Pinta_Robots():
    return

#---------------------------------------------------------------------
# Actualiza la estructura de datos de cada uno de los robots dentro del
# Mapa sMapa.
#---------------------------------------------------------------------
def Mueve_Robots():
    return
    
#---------------------------------------------------------------------
# Inicializa las Baldozas = Tiles del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Get_Tiles(nMW_X,nMH_Y,tRng):      
    return [[ RA.randint(tRng[0],tRng[1]) for i in range(0,nMW_X/nTW_X)] for i in range(0,nMH_Y/nTH_Y)]
 
#---------------------------------------------------------------------
# Inicializa Superficie del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Get_Surface(nAncho_X,nAlto_Y):
    return PG.Surface((nAncho_X,nAlto_Y))

#---------------------------------------------------------------------
# Inicializa Array de Sprites.-
#---------------------------------------------------------------------
def Img_Init():
    aImg = []
    aImg.append(Load_Image('T00.png',False )) # Tierra
    aImg.append(Load_Image('T01.png',False )) # Tierra + Piedras
    aImg.append(Load_Image('T02.png',False )) # Rocas
    aImg.append(Load_Image('T03.png',False )) # Marmol Celeste    
    aImg.append(Load_Image('T04.png',False )) # Marmol Star Yellow
    aImg.append(Load_Image('T05.png',False )) # Marmol Star Blue
    aImg.append(Load_Image('T06.png',False )) # Marmol Star Red
    aImg.append(Load_Image('T07.png',False )) # Marmol Gris Claro
    aImg.append(Load_Image('T08.png',False )) # Marmol Cafe
    aImg.append(Load_Image('T09.png',True  )) # Mouse
    aImg.append(Load_Image('bkg.png',False )) # Bkg
    aImg.append(Load_Image('video.png',False )) # Video
    aImg.append(Load_Image("MiniMapa.png",False)) #MiniMapa
    return aImg

#---------------------------------------------------------------------
# Make Mapa 
#---------------------------------------------------------------------
def Make_Mapa(sMem,aTiles,tCF):
    nPx = nPy = 0
    for f in range(0,tCF[1]/nTH_Y):
     for c in range(0,tCF[0]/nTW_X):
      if aTiles[f][c] == 0: 
         sMem.blit(aSprt[0],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 1: 
         sMem.blit(aSprt[1],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 2: 
         sMem.blit(aSprt[2],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 3: 
         sMem.blit(aSprt[3],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 4: 
         sMem.blit(aSprt[4],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 5: 
         sMem.blit(aSprt[5],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 6: 
         sMem.blit(aSprt[6],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 7: 
         sMem.blit(aSprt[7],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 8: 
         sMem.blit(aSprt[8],(nPx,nPy)); nPx += nTW_X
     nPx = 0; nPy += nTH_Y
    return

#---------------------------------------------------------------------
# Pinta Mouse
#---------------------------------------------------------------------
def Pinta_Mouse():
    sPanta.blit(aSprt[9],(nMx,nMy))
    return 

#---------------------------------------------------------------------
# Pinta Display Main
#---------------------------------------------------------------------
def Pinta_Panta():
    sPanta.blit(aSprt[10],(0,0))
    sPanta.blit(aSprt[11],(5,5))
    return 

#---------------------------------------------------------------------
# Pinta Mapas
#---------------------------------------------------------------------
def Pinta_Mapas():
    sPanta.blit(sMap_1.subsurface((Map1_X,Map1_Y,597,304)),(357,5))
    sPanta.blit(sMap_2.subsurface((Map2_X,Map2_Y,345,393)),(5,241))
    sPanta.blit(sMap_3.subsurface((Map3_X,Map3_Y,597,319)),(357,315))
    return

def Pinta_Minimapa():
    sPanta.blit(aSprt[12],(783,7)) #Mapa 1
    sPanta.blit(aSprt[12],(180,242)) #Mapa 2
    sPanta.blit(aSprt[12],(785,315))

def ZoomMapa_1(nMx,nMy):
    global Map1_X, Map1_Y
    rangoMax_X = 953  #rango minimo mas 170
    rangoMin_X = 762  #rango minimo X
    rangoMax_Y = 129  #rango minimo mas 122
    rangoMin_Y = 7    #rango minimo Y
    if nMx in range(783,953):
        if nMy in range(7,129):
            Map1_X = int(3840 * (nMx - 783) / 170)
            Map1_Y = int(1920 * (nMy - 7) / 122)
            if Map1_X >= 3243:
                Map1_X = 3243
            if Map1_Y >= 1616:
                Map1_Y = 1616
    return Map1_X, Map1_Y

def ZoomMapa_2(nMx,nMy):
    global Map2_X, Map2_Y
    rangoMax_X =  350
    rangoMin_X = 180
    rangoMax_Y = 129
    rangoMin_Y = 7
    if nMx in range(180,350):
        if nMy in range(242,364):
            Map2_X = int(1920 * (nMx - 180) / 170)
            Map2_Y = int(3200 * (nMy - 242) / 122)
            if Map2_X >= 1545:
                Map2_X = 1545
            if Map2_Y >= 2807:
                Map2_Y = 2807
    return Map2_X, Map2_Y


def ZoomMapa_3(nMx,nMy):
    global Map3_X,Map3_Y
    rangoMax_X = 5
    rangoMin_X = 0
    rangoMax_Y = 5
    rangoMin_Y = 6
    if nMx in range(785,953):
        if nMy in range(315,437):
            Map3_X = int(1920 * (nMx - 785) / 170)
            Map3_Y = int(1920 * (nMy - 315) / 122)
            if Map3_X >= 1323:
                Map3_X = 1323
            if Map3_Y >= 1601:
                Map3_Y = 1601
    return Map3_X, Map3_Y

#---------------------------------------------------------------------
# Pinta Reglas
#---------------------------------------------------------------------
def Pinta_Regla():
    if nMx >= 357 and nMx <= 953:
       if nMy >= 5 and nMy <= 308:
          PG.draw.line(sPanta,(255,255,0),(357,nMy),(953,nMy),2)
          PG.draw.line(sPanta,(255,255,0),(nMx,5),(nMx,308),2)
    return

#--------------------------------------------------------------
# Handle de Pause.-
##--------------------------------------------------------------
def Pausa():
    while 1:
     e = PG.event.wait()
     if e.type in (PG.QUIT, PG.KEYDOWN):
        return

#--------------------------------------------------------------
# Mueve
##--------------------------------------------------------------
def Mueve(cKey):
    global nXd
    if cKey == 'D':
       nXd += 1
       if nXd >= 2880: nXd = 2880
    if cKey == 'I':
       nXd -= 1
       if nXd <= 0: nXd = 0
    return     

#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
    
# Display Main
sPanta = PyGame_Init(); 

# Tiles/Sprites
aSprt = Img_Init() 

# Mapas....
sInfo  = Get_Surface(0345,0230); 
sMap_1 = Get_Surface(3840,1920); 
sMap_2 = Get_Surface(1920,3200); 
sMap_3 = Get_Surface(1920,1920); 

aMapTi_1 = Get_Tiles(3840,1920,(0,2)); Make_Mapa(sMap_1,aMapTi_1,(3840,1920)) 
aMapTi_2 = Get_Tiles(1920,3200,(3,5)); Make_Mapa(sMap_2,aMapTi_2,(1920,3200)) 
aMapTi_3 = Get_Tiles(1920,1920,(6,8)); Make_Mapa(sMap_3,aMapTi_3,(1920,1920)) 

aClk = [PG.time.Clock(),PG.time.Clock()] # Init Array de Cloks

nXd = nYd = 0

while lOK:

    cKey = PG.key.get_pressed()
    if cKey[PG.K_ESCAPE] : lOK = False
    if cKey[PG.K_p]      : Pausa()
    if cKey[PG.K_c]      : PG.image.save(sPanta,'foto.png')
    if cKey[PG.K_a]      : Mueve('D')
    if cKey[PG.K_s]      : Mueve('I')

    ev = PG.event.get()
    for e in ev:
        if e.type == QUIT           : lOK = False

    nMx,nMy = PG.mouse.get_pos()
    click = PG.mouse.get_pressed()
    if click[0]:
        Map1_X, Map1_Y = ZoomMapa_1(nMx,nMy)
        Map2_X, Map2_Y = ZoomMapa_2(nMx,nMy)
        Map3_X, Map3_Y = ZoomMapa_3(nMx,nMy)

    Pinta_Panta()
    Pinta_Mapas()
    Pinta_Minimapa()
    Pinta_Regla()
    Pinta_Mouse()
    PG.display.flip()
    aClk[0].tick(100)

    PG.quit






