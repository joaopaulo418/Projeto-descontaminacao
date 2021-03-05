import os
import time
from cv2 import cv2

def main(args):
    aux = 0
    texto = ''
    diretorio = './Images'
    for f in os.listdir(diretorio):
        os.remove(os.path.join(diretorio,f))
    camera = cv2.VideoCapture(0)
    #camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)'
    #camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024) 
    emLoop = True
    aux1 = 0
    aux = 0
    while (emLoop):
        tempo = 0
        _, img = camera.read()
        ini = time.time()
        cv2.imshow('Camera', img)
        src = './Images/imagenTeste'+texto+'.png'
        cv2.waitKey(1)
        texto = str(aux1)
        aux1 = aux1 + 1
        #aux2 = aux1 -1
        #texto1 = str(aux2)
        cv2.imwrite(src, img)
        #imgUMat = cv2.imread('./Images/ImagenTeste.png')
        #dst = cv2.detailEnhance(imgUMat,sigma_s=20, sigma_r=0.05)
        #cv2.imwrite(src,dst)
        fim = time.time()
        tempo = fim - ini
        aux = aux + tempo
        print (aux)
        if aux1 == 288:
            emLoop = False
    

    
    
    for f in os.listdir(diretorio):
        os.remove(os.path.join(diretorio,f))

    cv2.destroyAllWindows()
    camera.release()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))