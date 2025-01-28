from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = """
Você é um chatbot útil. Use o contexto fornecido para responder à pergunta do usuário de maneira clara e concisa.
Não exiba o contexto se ele for desnecessário para a resposta.
Não responda sempre relembrando que 'Com base no contexto fornecido'

Histórico da conversa:
{context}

Pergunta atual:
{question}

Resposta:
"""

IA_MODEL = "llama3.1:8b"

# Configuração do modelo e template
model = OllamaLLM(model=IA_MODEL)
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


def obter_resposta(context, pergunta):
    """Gera a resposta usando o modelo e retorna o contexto atualizado."""
    try:
        result = chain.invoke({"context": context, "question": pergunta})
        return result.strip()  # Remove espaços em branco desnecessários
    except Exception as e:
        return f"Erro ao processar a resposta: {e}"


def manter_conversa():
    """Função principal para manter a conversa."""
    context = ""
    print(f"Seja bem-vindo ao Ollama IA (Modelo: {IA_MODEL})")
    print("Digite 'sair' para encerrar o chatbot.\n")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Encerrando a conversa. Até mais!")
            break

        # Obter resposta e atualizar o contexto
        resposta = obter_resposta(context, user_input)
        print("Bot:", resposta)

        # Atualizar o contexto
        context += f"Você: {user_input}\nBot: {resposta}\n"


if __name__ == "__main__":
    manter_conversa()


# result = model.invoke(input="ola Ollama, como você está?")
# result = chain.invoke({"context": "", "question": "Ola, me diga em uma linha, o que você é"})
# print(result)
