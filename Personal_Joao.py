import cv2
import numpy as np
import time
import PoseModule as pm


# Caminho para capturar a imagem
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Abrindo o Video
detector = pm.poseDetector()

# Realizando a contagem de supinos
count = 0
dir = 0

# Declarando variavel para o FPS
pTime = 0

# Declarando a %

# Abrir o video do cara fazendo flexão
while True:


    success, img = cap.read()
    img = cv2.resize(img, (1000, 600) )
    # img = cv2.imread('test.jpg')
    img = detector.findPose(img, False)

    # Coletando os dados da Imagem
    lmList = detector.findPosition(img, False)
    # print(lmList)

    if len(lmList) != 0:

        # Braço direito
        angle = detector.findAngle(img, 12, 14, 16)

        # Braço Esquerdo
        angle =  detector.findAngle(img, 11, 13, 15)

        # Perna Esquerda
        # angle = detector.findAngle(img, 24, 26, 28)

        # Perna Direita
        # angle = detector.findAngle(img, 23, 25, 27)

        # Calculando a % do Burp para realizar a contagem
        per = np.interp(angle, (60, 150), (0, 100) )

        # print(angle, per)


        # Contagem dos Supinos
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir ==1:
                count += 0.5
                dir = 0
        # print(count)

        

        # Imprimindo na Tela a contagem de Burp
        cv2.putText(img, f'Repeticoes: {int(count)}', (50, 550), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5 )

    # Calculando o FPS
    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (50, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 5 )


    
    # Abrindo a Imagem
    cv2.imshow('Image', img)
    cv2.waitKey(1)