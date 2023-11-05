LAB06 - Contorno de Imagens

Alunos: Gabriel Pasquarelli RA: 222.200.11-5
Gabriel Vieira RA: 222.200.12-3

Parametros utilizados:

a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a/2*1.2, a,cv2.THRESH_BINARY_INV)

results: Pasta com os resultados obtidos utilizando os parametros acima.


