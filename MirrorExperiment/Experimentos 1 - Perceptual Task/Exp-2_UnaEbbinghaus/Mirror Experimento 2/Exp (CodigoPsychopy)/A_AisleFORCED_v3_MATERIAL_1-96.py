from psychopy import visual, core, event, gui
import random, time


options={"Experimento":"2b","Descripcion":"Una Figura", "Procedimiento":"2AFC","Participante":"Usuario1"}
myDlg=gui.DlgFromDict(dictionary=options, title="Gano")
if myDlg.OK:
    print "Ok"
else:
    core.quit()
#
#WINDOW CONFIGURATION
#	
mywindow= visual.Window(monitor="testMonitor", units="cm", fullscr=True, color="white")
mymouse= event.Mouse(mywindow)
mymouse.setVisible(0)
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()

#PantallaInicio=visual.ImageStim(mywindow, image="Bienvenido.png", pos=[0,0])
#PantallaInicio.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)
#
#FIRST INSTRUCTIONS
#
#print "Total Time"
#total_time = time.time()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
#####Instrucciones1=visual.ImageStim(mywindow, image="Inst_1.png", pos=[0,0])
#####Instrucciones1.draw()
#####txtResults=visual.TextStim(mywindow,text="Instrucciones:"+"\n"+"\n"+"\n"+"\n"+"En la pantalla se te mostraran dos circulos en color claro cuyo tamano deberas comparar. El circulo del lado izquierdo permanecera aislado, como referencia. El circulo del lado derecho aparecera rodeado de un conjunto de circulos de distinto tamano" +"\n"+"\n"+"\n"+"\n"+"Presiona la tecla S cuando los circulos claros SI sean del mismo tamano. "+"\n"+"\n"+"Presiona la tecla N si NO son iguales"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#####txtResults.draw()
#txtInst1=visual.TextStim(mywindow,text="Instrucciones:",wrapWidth = 60,color=[0,0,0], pos=[0,14], colorSpace="rgb255")
#txtInst2=visual.TextStim(mywindow,text="En el centro de la pantalla se te mostrara un circulo aislado cuyo tamano y posicion permaneceran constantes. Este sera nuestro Circulo de Referencia.",wrapWidth = 35,color=[0,0,0], pos=[0,0], colorSpace="rgb255")
#txtInst3=visual.TextStim(mywindow,text="Presiona la barra espaciadora para continuar",wrapWidth = 60,color=[0,0,0], pos=[0,-15], colorSpace="rgb255")
#img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
#txtInst1.draw()
#txtInst2.draw()
#txtInst3.draw()
#img4.draw()
mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)

#
#FIRST EXAMPLE
#

#mywindow.update()
#img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17.5,-3])
#img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
#img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
#img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3], size=[3,3])
#img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3], size=[1,1])
#txtResults=visual.TextStim(mywindow,text="A cada lado del Circulo de Referencia aparecera un circulo del mismo color rodeado por una serie de circulos de distinto tamano.",wrapWidth = 35,pos=[0,13], color=[0,0,0], colorSpace="rgb255")
#txtRes=visual.TextStim(mywindow,text="Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-15], color=[0,0,0], colorSpace="rgb255")
#img1.draw()
#img2.draw()
#img3.draw()
#img4.draw()
#img5.draw()
#txtResults.draw()
#txtRes.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)
    

mywindow.update()
#img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17.5,-3])
#img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
#img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
#img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3], size=[3,3])
#img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3], size=[1,1])
#txtResults=visual.TextStim(mywindow,text="Tu tarea consiste en indicar, presionando la TECLA DERECHA o IZQUIERDA, cual de las figuras laterales tiene el circulo central que MAS SE PARECE (en tamano) al Circulo de Referencia.",wrapWidth = 35,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
#txtRes=visual.TextStim(mywindow,text="Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-15], color=[0,0,0], colorSpace="rgb255")
#img1.draw()
#img2.draw()
#img3.draw()
#img4.draw()
#img5.draw()
#txtResults.draw()
#txtRes.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)
    
    

mywindow.update()
#img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[17.5,-3])
#img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
#img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7], size=[3,3])
#img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3], size=[3,3])
#img6=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3], size=[1,1])
#txtResults=visual.TextStim(mywindow,text="Por ejemplo, en este caso el circulo central de la figura derecha es mucho mas pequeno que el Circulo de Referencia. En tanto que, el circulo del lado izquierdo parece tener el mismo tamano. Deberias presionar la Tecla IZQUIERDA",wrapWidth = 45,pos=[0,12], color=[0,0,0], colorSpace="rgb255")
#txtRes=visual.TextStim(mywindow,text="Presiona la TECLA IZQUIERDA",wrapWidth = 30,pos=[0,-15], color=[0,0,0], colorSpace="rgb255")
#img1.draw()
#img2.draw()
#img3.draw()
#img4.draw()
#img5.draw()
#txtResults.draw()
#txtRes.draw()
#mywindow.update()
#	
#userSel=" "
#validkeys=['left']
#while userSel !='left':
#	keys=event.getKeys()
#	for k in keys:
#		if k in validkeys:
#			userSel=k
#		elif k=='escape': 
#			myfile.Close()
#			core.quit()
#	core.wait(0.1)

#INSTRUCCIONES  (2DA PARTE)
#Respecto de la REGLITA
#mywindow.update()
#imgx=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,1.5])
#txtResults=visual.TextStim(mywindow,text="Posteriormente, se te presentara una escala como la siguiente: ",wrapWidth = 45,pos=[0,8], color=[0,0,0], colorSpace="rgb255")
#txtRes=visual.TextStim(mywindow,text="Deberas teclear el numero 1, 2 o el 3, dependiendo de que tan seguro estas de tu respuesta."+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 30,pos=[0,-7], color=[0,0,0], colorSpace="rgb255")
#imgx.draw()
#txtResults.draw()
#txtRes.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)
#mywindow.update()
#
#END OF FIRST EXAMPLE
#
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
#txtResults=visual.TextStim(mywindow,text="En cada ensayo DEBERAS ELEGIR UNA de las dos figuras laterales: La que contenga el circulo central CUYO TAMANO SE PAREZCA MAS al Circulo de Referencia."+"\n"+"\n"+"\n"+"\n"+"Elige siempre la opcion de la cual estes mas seguro(a)"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#txtResults.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)
    

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
#txtResults=visual.TextStim(mywindow,text="Cada pareja a comparar se te mostrara por solo un par de segundos."+"\n"+"\n"+"\n"+"\n"+"NO avanzaras al siguiente ensayo hasta que registres tu respuesta."+"\n"+"\n"+"\n"+"\n"+"Una vez respondas, el programa esperara a que presiones la barra espaciadora para indicar que estas listo(a) para el siguiente ensayo"+"\n"+"\n"+"\n"+"\n"+"Los ensayos se presentara en distintos colores para facilitar su distincion, los colores NO SON INDICADORES de nada."+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para continuar",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255")
#txtResults.draw()
mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)


mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
#txtResults=visual.TextStim(mywindow,text="\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para comenzar el experimento",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255",alignHoriz="center")
#txtResults.draw()
#mywindow.update()
#while 'space' not in event.getKeys(): 
#	core.wait(0.1)

#END OF INSTRUCTIONS
#


#
#VARIABLE INITIALIZATION
#
mybaseline=open("MirrorEx2b"+"_"+options["Participante"]+"_"+time.strftime("%Y-%m-%d")+"_"+"2AFC.csv", 'w')
signalright=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 99, 100, 103, 104, 107, 108, 111, 112, 115, 116, 119, 120, 123, 124, 127, 128, 131, 132, 135, 136, 139, 140, 143, 144, 147, 148, 151, 152, 155, 156, 159, 160, 163, 164, 167, 168, 171, 172, 175, 176, 179, 180, 183, 184, 187, 188, 191, 192]
signalleft=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 98, 101, 102, 105, 106, 109, 110, 113, 114, 117, 118, 121, 122, 125, 126, 129, 130, 133, 134, 137, 138, 141, 142, 145, 146, 149, 150, 153, 154, 157, 158, 161, 162, 165, 166, 169, 170, 173, 174, 177, 178, 181, 182, 185, 186, 189, 190]
AS_AN=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
BS_BN=[49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
AS_BN=[97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144] 
BS_AN=[145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]
AS_BS=[193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240]
Null_ASright=[194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240]
AN_BN=[241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288]
Null_ANright=[242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288]
Pur=[4, 7, 10, 13, 20, 23, 26, 29, 36, 39, 42, 45, 52, 55, 58, 61, 68, 71, 74, 77, 84, 87, 90, 93, 195, 198, 201, 204, 210, 215, 221, 224, 228, 231, 234, 237, 242, 248, 251, 253, 257, 263, 268, 270, 275, 277, 282, 288, 100, 148, 103, 151, 106, 154, 109, 157, 116, 164, 119, 167, 122, 170, 125, 173, 132, 180, 135, 183, 138, 186, 141, 189]
Nar=[3, 6, 9, 16, 19, 22, 25, 32, 35, 38, 41, 48, 51, 54, 57, 64, 67, 70, 73, 80, 83, 86, 89, 96, 197, 200, 203, 206, 209, 212, 218, 223, 225, 232, 235, 238, 243, 245, 250, 256, 258, 264, 267, 269, 276, 278, 281, 287, 99, 147, 102, 150, 105, 153, 112, 160, 115, 163, 118, 166, 121, 169, 128, 176, 131, 179, 134, 182, 137, 185, 144, 192]
Az=[2, 5, 12, 15, 18, 21, 28, 31, 34, 37, 44, 47, 50, 53, 60, 63, 66, 69, 76, 79, 82, 85, 92, 95, 193, 196, 202, 207, 213, 216, 219, 222, 227, 230, 233, 240, 241, 247, 252, 254, 260, 262, 265, 271, 274, 280, 283, 285, 98, 146, 101, 149, 108, 156, 111, 159, 114, 162, 117, 165, 124, 172, 127, 175, 130, 178, 133, 181, 140, 188, 143, 191]
Ver=[1, 8, 11, 14, 17, 24, 27, 30, 33, 40, 43, 46, 49, 56, 59, 62, 65, 72, 75, 78, 81, 88, 91, 94, 194, 199, 205, 208, 211, 214, 217, 220, 226, 229, 236, 239, 244, 246, 249, 255, 259, 261, 266, 272, 273, 279, 284, 286, 97, 145, 104, 152, 107, 155, 110, 158, 113, 161, 120, 168, 123, 171, 126, 174, 129, 177, 136, 184, 139, 187, 142, 190]


ALL=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288]


#Variables uses to count the four possible results in Signal Detection Theory: hit, false alarm, miss and rejection
#Variables for counting in the first block
rightcounterb=0
wrongcounterb=0
falsealarmB=0
hitB=0
rejectionB=0
missB=0
#Variables for counting in the second block
rightcounterT=0
wrongcounterT=0
falsealarmT=0
hitT=0
rejectionT=0
missT=0

#central=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
mybaseline.write("Ensayo, Estimulo, Comparacion, SignallPosition, Respuesta, Eleccion, OpcionPredicha, RTime1, RTime2, Color, Hits, ContadorH, Rechazos, ContadorR, Falsas alarmas, ContadorF, Omisiones, ContadorM, \n")
mywindow.update()


#
#BEGIN OF FIRST BLOCK
#
for j in range(1):
	central = list()
	for i in range (96):
		central.append (i+1)
	for i in range (96):
#		choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288]
		choice = central.pop(random.randint(0,len(central)-1))
#AS-AN 
		if choice==1:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[17,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,8],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-1],size=[3,3])
		if choice==2:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-1],size=[2.5,2.5])
		if choice==3:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==4:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-17.5,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17.5,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-3],size=[2,2])
		if choice==5:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[16.5,-3],size=[1.5,1.5])
		if choice==6:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-1],size=[3,3])
		if choice==7:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-17.5,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-2],size=[2,2])
		if choice==8:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-3],size=[2,2])
		if choice==9:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==10:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[17.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==11:
			img1=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-3],size=[2,2])
		if choice==12:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-19,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-2],size=[2,2])
		if choice==13:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[16.5,-3],size=[3,3])
		if choice==14:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[18,-1],size=[2.5,2.5])
		if choice==15:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17.5,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[16.5,-3],size=[2,2])
		if choice==16:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-19,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-2],size=[2,2])
		if choice==17:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[18,-1],size=[3,3])
		if choice==18:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[16.5,-3],size=[2.5,2.5])
		if choice==19:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[2,2])
		if choice==20:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-19,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[16.5,-2],size=[2,2])
		if choice==21:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[1.5,1.5])
		if choice==22:
			img1=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1.5,1.5])
		if choice==23:
			img1=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[16.5,-3],size=[2,2])
		if choice==24:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-17.5,-1])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[16.5,-2],size=[2,2])
		if choice==25:
			img1=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[-17.5,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[3,3])
		if choice==26:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-17.5,-2])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[17.5,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-1],size=[2.5,2.5])
		if choice==27:
			img1=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17.5,-3],size=[2,2])
		if choice==28:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[17.5,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-19,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17.5,-2],size=[2,2])
		if choice==29:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-17.5,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[17.5,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-2],size=[3,3])
		if choice==30:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-17.5,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[16.5,-3],size=[2.5,2.5])
		if choice==31:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17.5,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17.5,-3],size=[2,2])
		if choice==32:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17.5,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-19,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-2],size=[2,2])
		if choice==33:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-17.5,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17.5,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-3],size=[1.5,1.5])
		if choice==34:
			img1=visual.ImageStim(mywindow, image="cext_under2_az.png", pos=[-17.5,-2])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17.5,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-1],size=[1.5,1.5])
		if choice==35:
			img1=visual.ImageStim(mywindow, image="cext_over2_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_an.png", pos=[17.5,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-3],size=[2,2])
		if choice==36:
			img1=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under2_pur.png", pos=[17.5,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-2],size=[2,2])
		if choice==37:
			img1=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[-18,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-19,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[3,3])
		if choice==38:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-18,-2])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-19,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-1],size=[2.5,2.5])
		if choice==39:
			img1=visual.ImageStim(mywindow, image="cext_over3_pur.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[18,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17.5,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-3],size=[2,2])
		if choice==40:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-18.5,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[18,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-2],size=[2,2])
		if choice==41:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-18,-3])
			img2=visual.ImageStim(mywindow, image="cext_over3_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-19,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[16.5,-3],size=[1.5,1.5])
		if choice==42:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-18,-2])
			img2=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-19,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-1],size=[3,3])
		if choice==43:
			img1=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[-18.5,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[18,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-2],size=[2,2])
		if choice==44:
			img1=visual.ImageStim(mywindow, image="cext_over3_az.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17.5,-2],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-1],size=[2,2])
		if choice==45:
			img1=visual.ImageStim(mywindow, image="cext_under3_pur.png", pos=[-18,-3])
			img2=visual.ImageStim(mywindow, image="cext_over2_pur.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-19,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-3],size=[2.5,2.5])
		if choice==46:
			img1=visual.ImageStim(mywindow, image="cext_under3_ver.png", pos=[-18,-3])
			img2=visual.ImageStim(mywindow, image="cext_under2_ver.png", pos=[18,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-19,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[18,-3],size=[1.5,1.5])
		if choice==47:
			img1=visual.ImageStim(mywindow, image="cext_over2_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_under3_az.png", pos=[18,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[2,2])
		if choice==48:
			img1=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under3_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-19,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-1],size=[2,2])
# BS - BN
		if choice==49:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-3],size=[3,3])
		if choice==50:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[18,-1],size=[2.5,2.5])
		if choice==51:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==52:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-2],size=[2,2])
		if choice==53:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[1.5,1.5])
		if choice==54:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[3,3])
		if choice==55:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-2],size=[2,2])
		if choice==56:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-3],size=[2,2])
		if choice==57:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2.5,2.5])
		if choice==58:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==59:
			img1=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-3],size=[2,2])
		if choice==60:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-19,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-2],size=[2,2])
		if choice==61:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-3],size=[3,3])
		if choice==62:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-18,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17.5,-1],size=[2.5,2.5])
		if choice==63:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[2,2])
		if choice==64:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[2,2])
		if choice==65:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17.5,-1],size=[3,3])
		if choice==66:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[2.5,2.5])
		if choice==67:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-3],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-3],size=[2,2])
		if choice==68:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-2],size=[2,2])
		if choice==69:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-3],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-3],size=[1.5,1.5])
		if choice==70:
			img1=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[1.5,1.5])
		if choice==71:
			img1=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[-17,-3])
			img2=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[17,-3])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17,-3],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-3],size=[2,2])
		if choice==72:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-2],size=[2,2])
		if choice==73:
			img1=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[3,3])
		if choice==74:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-1],size=[2.5,2.5])
		if choice==75:
			img1=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-17,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17.5,-1],size=[2,2])
		if choice==76:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-18,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17.5,-1],size=[2,2])
		if choice==77:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-2],size=[3,3])
		if choice==78:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_ver.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-2],size=[2.5,2.5])
		if choice==79:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17.5,-1],size=[2,2])
		if choice==80:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==81:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_ver.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17,-2],size=[1.5,1.5])
		if choice==82:
			img1=visual.ImageStim(mywindow, image="cext_under7_az.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-18.5,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[18,-1],size=[1.5,1.5])
		if choice==83:
			img1=visual.ImageStim(mywindow, image="cext_over7_an.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under7_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-17,-2],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17.5,-1],size=[2,2])
		if choice==84:
			img1=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18.5,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17.5,-1],size=[2,2])
		if choice==85:
			img1=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[17,-2],size=[3,3])
		if choice==86:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2.5,2.5])
		if choice==87:
			img1=visual.ImageStim(mywindow, image="cext_over8_pur.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-17,-2],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[18,-1],size=[2,2])
		if choice==88:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[18,-1],size=[2,2])
		if choice==89:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over8_an.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[17,-2],size=[1.5,1.5])
		if choice==90:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[18,-1],size=[3,3])
		if choice==91:
			img1=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18.5,-1],size=[3,3])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[18,-1],size=[2,2])
		if choice==92:
			img1=visual.ImageStim(mywindow, image="cext_over8_az.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-2],size=[2.5,2.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[18,-1],size=[2,2])
		if choice==93:
			img1=visual.ImageStim(mywindow, image="cext_under8_pur.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_over7_pur.png", pos=[17,-2])
			img3=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_pur.png", pos=[17,-2],size=[2.5,2.5])
		if choice==94:
			img1=visual.ImageStim(mywindow, image="cext_under8_ver.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under7_ver.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[-18,-1],size=[2,2])
			img5=visual.ImageStim(mywindow, image="ccentral_ver.png", pos=[17.5,-1],size=[1.5,1.5])
		if choice==95:
			img1=visual.ImageStim(mywindow, image="cext_over7_az.png", pos=[-17,-2])
			img2=visual.ImageStim(mywindow, image="cext_under8_az.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[-17,-2],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_az.png", pos=[18,-1],size=[2,2])
		if choice==96:
			img1=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[-18,-1])
			img2=visual.ImageStim(mywindow, image="cext_under8_an.png", pos=[18,-1])
			img3=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[0,7],size=[2,2])
			img4=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[-18,-1],size=[1.5,1.5])
			img5=visual.ImageStim(mywindow, image="ccentral_an.png", pos=[18,-1],size=[2,2])
#
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio3.png", pos=[0,13])
		txtRecordat2=visual.ImageStim(mywindow,image="Right.png", pos=[17,-15.8])
		txtRecordat3=visual.ImageStim(mywindow,image="Left.png", pos=[-17,-15.8])
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		img1.draw()
		img2.draw()
		img3.draw()
		img4.draw()
		img5.draw()
		mybaseline.close
		mywindow.update()
		presentation_time = time.time()
#Tiempo que duran los ensayos0
		core.wait(1)
		presentation2_time = time.time()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		txtRecordat1=visual.ImageStim(mywindow, image="Recordatorio3.png", pos=[0,13])
		txtRecordat2=visual.ImageStim(mywindow,image="Right.png", pos=[17,-15.8])
		txtRecordat3=visual.ImageStim(mywindow,image="Left.png", pos=[-17,-15.8])
		txtRecordat1.draw()
		txtRecordat2.draw()
		txtRecordat3.draw()
		mywindow.update()
		userSel=" "
		validkeys=['left', 'right']
		while userSel !='left' and userSel !='right':
			keys=event.getKeys()
			for k in keys:
				if k in validkeys:
					userSel=k
				elif k=='escape': 
					mytestline.Close()
					core.quit() 
			core.wait(0.1)
			response_time = time.time() - presentation_time
			response_timeB = time.time() - presentation2_time
		isASAN=(choice in AS_AN)
		if isASAN: 
			Comparacion='1 AS-AN'
		isBSBN=(choice in BS_BN)
		if isBSBN: 
			Comparacion='3 BS-BN'
		isASBN=(choice in AS_BN)
		if isASBN: 
			Comparacion='2 AS-BN'
		isBSAN=(choice in BS_AN)
		if isBSAN: 
			Comparacion='4 BS-AN'
		isASBS=(choice in AS_BS)
		if isASBS: 
			Comparacion='5 AS-BS'
			PosSenal='Both'
		isANBN=(choice in AN_BN)
		if isANBN: 
			Comparacion='6 AN-BN'
			PosSenal='None'
		isPurple=(choice in Pur)
		if isPurple: 
			Colorx='Purpura'
		isOrange=(choice in Nar)
		if isOrange: 
			Colorx='Naranja'
		isGreen=(choice in Ver)
		if isGreen: 
			Colorx='Verde'
		isBlue=(choice in Az)
		if isBlue: 
			Colorx='Azul'
		isCorrect=(choice in signalright and userSel =='right') or (choice in signalleft and userSel =='left')
		if isCorrect: 
			Correcto=1
			rightcounterb=rightcounterb+1
			PrefPred=1
		isWrong=(choice in signalright and userSel =='left') or (choice in signalleft and userSel =='right')
		if isWrong:
			 wrongcounterb=wrongcounterb+1
			 Correcto=0
			 PrefPred=0
		isAS=(choice in signalright and choice in AS_AN and userSel =='right') or (choice in signalright and choice in AS_BN and userSel =='right') or (choice in signalleft and choice in AS_AN and userSel =='left') or (choice in signalleft and choice in AS_BN and userSel =='left') or (choice in AS_BS and choice not in Null_ASright and userSel =='left') or (choice in AS_BS and choice in Null_ASright and userSel =='right')
		if isAS: 
			Eleccion='AS'
		isAN=(choice in signalright and choice in AS_AN and userSel =='left') or (choice in signalleft and choice in AS_AN and userSel =='right') or (choice in signalright and choice in BS_AN and userSel =='left') or (choice in signalleft and choice in BS_AN and userSel =='right') or (choice in AN_BN and choice not in Null_ANright and userSel =='left') or (choice in AN_BN and choice in Null_ANright and userSel =='right')
		if isAN: 
			Eleccion='AN'
		isBS=(choice in signalright and choice in BS_AN and userSel =='right') or (choice in signalright and choice in BS_BN and userSel =='right') or (choice in signalleft and choice in BS_AN and userSel =='left') or (choice in signalleft and choice in BS_BN and userSel =='left') or (choice in AS_BS and choice not in Null_ASright and userSel =='right') or (choice in AS_BS and choice in Null_ASright and userSel =='left')
		if isBS: 
			Eleccion='BS'
		isBN=(choice in signalright and choice in BS_BN and userSel =='left') or (choice in signalleft and choice in BS_BN and userSel =='right') or (choice in signalleft and choice in AS_BN and userSel =='right') or (choice in signalright and choice in AS_BN and userSel =='left') or (choice in AN_BN and choice not in Null_ANright and userSel =='right') or (choice in AN_BN and choice in Null_ANright and userSel =='left')
		if isBN: 
			Eleccion='BN'
		isNULLConsistent=(choice in AS_BS and choice not in Null_ASright and userSel =='left') or (choice in AS_BS and choice in Null_ASright and userSel =='right') or (choice in AN_BN and choice not in Null_ANright and userSel =='right') or (choice in AN_BN and choice in Null_ANright and userSel =='left')
		if isNULLConsistent:
			PrefPred=1
		isNULLInconsistent=(choice in AS_BS and choice not in Null_ASright and userSel =='right') or (choice in AS_BS and choice in Null_ASright and userSel =='left') or (choice in AN_BN and choice not in Null_ANright and userSel =='left') or (choice in AN_BN and choice in Null_ANright and userSel =='right')
		if isNULLInconsistent:
			PrefPred=0
		isSignalright=(choice in signalright)
		if isSignalright:
			PosSenal='Right'
		isSignalleft=(choice in signalleft)
		if isSignalleft: 
			PosSenal='Left'
		isNoRightAnswer=(choice in AN_BN or choice in AS_BS)
		if isNoRightAnswer: 
			Correcto='NA'
			Hit='NA'
			Rechazo='NA'
			FalseAlarm='NA'
			Miss='NA'
		isHit_and_Rejection=(choice in signalright and userSel =='right') or (choice in signalleft and userSel =='left')
		if isHit_and_Rejection: 
			hitB=hitB+1
			Hit=1
			rejectionB=rejectionB+1
			Rechazo=1
			FalseAlarm=0
			Miss=0
		isFalseAlarm_and_Miss=(choice in signalright and userSel =='left') or (choice in signalleft and userSel =='right')
		if isFalseAlarm_and_Miss: 
			falsealarmB=falsealarmB+1
			FalseAlarm=1
			missB=missB+1
			Miss=1
			Hit=0
			Rechazo=0
		mybaseline.write(str(i)+","+str(choice)+","+str(Comparacion)+","+str(PosSenal)+','+str(userSel)+","+str(Eleccion)+","+str(PrefPred)+","+str(response_time)+","+str(response_timeB)+','+str(Colorx)+','+str(Hit)+","+str(hitB)+","+str(Rechazo)+","+str(rejectionB)+","+str(FalseAlarm)+","+str(falsealarmB)+","+str(Miss)+","+str(missB)+"\n")
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
		mywindow.update()
		txtResults=visual.TextStim(mywindow,text="\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para avanzar al siguiente ensayo.",wrapWidth = 45,color=[0,0,0], colorSpace="rgb255",alignHoriz="center")
		txtResults.draw()
		mywindow.update()
		while 'space' not in event.getKeys(): 
			core.wait(0.1)
#		mybaseline.write(str(i)+","+str(choice)+","+str(userSel)+","+str(isCorrect)+","+str(rightcounterb)+","+str(wrongcounterb)+","+str(isHit)+","+str(hitB)+","+str(isRejection)+","+str(rejectionB)+","+str(isFalseAlarm)+","+str(falsealarmB)+","+str(isMiss)+","+str(missB)+","+"\n")
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		core.wait(0.5)
#		reglita=visual.ImageStim(mywindow, image="Reglita.png", pos=[0,0])
#		reglita.draw()
#		txtRegla=visual.ImageStim(mywindow, image="Recordatorio2.png", pos=[0,8])
#		txtRegla.draw()
#		mywindow.update()
#		reglita_time = time.time()
#Tiempo que dura la Reglita 
#		core.wait(.5)
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
#		mywindow.update()
#		userSel=" "
#		validkeys=['1', '2', '3']
#		while userSel !='1' and userSel !='2' and userSel !='3':
#			keys=event.getKeys()
#			for k in keys:
#				if k in validkeys:
#					userSel=k
#				elif k=='escape': 
#					mytestline.Close()
#					core.quit()
#			core.wait(0.1)
#			response_time2 = time.time() - reglita_time
#		isHighOld=(isFalseAlarm and userSel =='3') or (isHit and userSel =='3')
#		if isHighOld: 
#			Confidence=6 
#		isHighNew=(isRejection and userSel =='3') or (isMiss and userSel =='3')
#		if isHighNew: 
#			Confidence=1
#		isMediumOld=(isFalseAlarm and userSel =='2') or (isHit and userSel =='2')
#		if isMediumOld: 
#			Confidence=5
#		isMediumNew=(isRejection and userSel =='2') or (isMiss and userSel =='2')
#		if isMediumNew: 
#			Confidence=2
#		isLowOld=(isFalseAlarm and userSel =='1') or (isHit and userSel =='1')
#		if isLowOld: 
#			Confidence=4
#		isLowNew=(isRejection and userSel =='1') or (isMiss and userSel =='1')
#		if isLowNew: 
#			Confidence=3

#END OF ONE TEST
	#END OF A BLOCK OF 48 TESTS
#
#END OF THE FIRST BLOCK
#
TOTAL_time = time.time() - total_time
print str(TOTAL_time)
mybaseline.write(str(TOTAL_time))

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()

mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Resultado: "+"\n"+"\n"+"Respuesatas Correctas: "+str(rightcounterb)+"\n"+"Respuestas Incorrectas: "+str(wrongcounterb)+"\n"+"\n"+"Presiona la barra espaciadora para continuar",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)



mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
mywindow.setColor(color=[255,255,255], colorSpace="rgb255")
mywindow.update()
txtResults=visual.TextStim(mywindow,text="Listo! El experimento ha terminado!"+"\n"+"\n"+"Muchisimas gracias por tu tiempo y cooperacion."+"\n"+"\n"+"Gracias por contribuir al trabajo de una tesista"+"\n"+"\n"+"\n"+"\n"+"Presiona la barra espaciadora para salir",color=[0,0,0], colorSpace="rgb255")
txtResults.draw()
mywindow.update()
while 'space' not in event.getKeys(): 
	core.wait(0.1)

