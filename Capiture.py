import os
import time
from cv2 import cv2

def Binarization(src):
    imgUMat = cv2.imread(src) #le o path atual da imagem
    resized = cv2.resize(imgUMat, (64, 64), interpolation = cv2.INTER_CUBIC) # redimensiona a imagem
    grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    return grayImage

def main(args):
    aux = 0
    texto = ''
    diretorio = './Images'
    for f in os.listdir(diretorio):
        os.remove(os.path.join(diretorio,f))
    camera = cv2.VideoCapture(0)
    #camera.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
    #camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 64) 
    emLoop = True
    aux1 = 1
    aux = 0
    while (emLoop):
        tempo = 0
        _, img = camera.read()
        ini = time.time()
        texto = str(aux1) #transforma o numero em string
        src = './Images/'+texto+'.png'
        cv2.imwrite(src, img)
        aux1 = aux1 + 1
        cv2.imwrite(src,Binarization(src)) ##sobrescreverá a imagem com um novo formato
        fim = time.time()
        tempo = fim - ini
        aux = aux + tempo
        print (aux)
        if aux1 == 288:
            emLoop = False
    

    
    
   

    cv2.destroyAllWindows()
    camera.release()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))