from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto

#criar o modelo
myChatBot.createModel()

#Carregar o modelo treinado
#myChatBot.loadModel()


print("Bem vindo ao Chatbot")
print("teste")


pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
if len(resposta) > 1:
            myChatBot.multiple_response(intencao[0]['intent'])
for resp in resposta:
    print(resp + "   ["+intencao[0]['intent']+"]\n")

#print(resposta + "   ["+intencao[0]['intent']+"]")




while (intencao[0]['intent']!="despedida"):
    if intencao[0]['intent']=="saudacao":
        pergunta = input("Como posso te ajudar?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        if len(resposta) > 1:
            myChatBot.multiple_response(intencao[0]['intent'])
        for resp in resposta:
            print(resp + "   ["+intencao[0]['intent']+"]\n")
        #print(resposta + "\n[" + intencao[0]['intent'] + "]")
    else:
        pergunta = input("Posso lhe ajudar com algo a mais?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        if len(resposta) > 1:
            myChatBot.multiple_response(intencao[0]['intent'])
        for resp in resposta:
            print(resp + "   ["+intencao[0]['intent']+"]\n")
        #print(resposta + "\n[" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo!")
