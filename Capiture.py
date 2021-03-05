import os
import time
from cv2 import cv2
def main(args):
    aux = 0
    texto = ''
    nFrames = 30
    diretorio = './Images'
    for f in os.listdir(diretorio):
        os.remove(os.path.join(diretorio,f))
    camera = cv2.VideoCapture(0)
    emLoop = True
    aux1 = 0
    aux = 0
    while (emLoop):
        tempo = 0
        retval, img = camera.read()
        ini = time.time()
        cv2.imshow('Camera', img)
        file = './Images/imagenTeste'+texto+'.png'
        cv2.waitKey(1)
        texto = str(aux1)
        aux1 = aux1 + 1
        cv2.imwrite(file, img)
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