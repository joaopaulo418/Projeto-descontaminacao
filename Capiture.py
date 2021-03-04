import cv2
import time
from cv2 import cv2
def main(args):
    aux = 0
    texto = ''
    nFrames = 30
    camera = cv2.VideoCapture(0)
    emLoop = True
    aux1 = 0
    aux = 0
    while (emLoop):
        tempo = 0
        ini = time.time()
        retval, img = camera.read()
        cv2.imshow('Foto', img)
        file = 'Imagens/' + texto + '.png'
        texto = str(aux1)
        aux1 = aux1 + 1
        cv2.imwrite(file, img)
        fim = time.time()
        tempo = fim - ini
        aux = aux + tempo
        print (aux)
    cv2.destroyAllWindows()
    camera.release()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))