def jogar():

    palavra_secreta= "Rangel"
    acertou= False
    enforcou= False
    forca= ('_','_','_','_','_''_')
    print("Bem Vindos ao jogo da Forca")
    print("****************************")
    print(forca)


    while acertou == False or enforcou == False:
        print("Jogando...")
        palpite= input("Digite uma Letra:")
        for letra in palavra_secreta:
            if palpite == letra:
                acerto= letra
                print("Muito bem!")
                x= palpite
                valor_mostrado= palavra_secreta.find(x)
                forca= acerto[valor_mostrado]
                print(forca)
            elif palpite !=  letra:
                continue
            
if (__name__=='__main__'):
        jogar()