import os
import readline
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = """
Você é ICEBERG IA, um chatbot útil. Use o contexto fornecido para responder à pergunta do usuário de maneira clara e concisa.
Não exiba o contexto se ele for desnecessário para a resposta.
Não responda sempre relembrando que 'Com base no contexto fornecido'.

--- Informações ---
Data e hora atual: {data_hora} | hora: HH:MM:SS | data: DD-MM-YYYY

--- Fim das informações ---

--- Histórico da conversa ---
Histórico da conversa:
{context}
--- Fim do histórico ---

Pergunta atual:
{question}

Resposta:
"""

# Modelo de IA usado | llama3.1:8b | llama3.2:3b // deepseek-r1:1.5b | deepseek-r1:8b // Recomendo usar o deepseek
IA_MODEL = "deepseek-r1:8b"

# Configuração do modelo e template
model = OllamaLLM(model=IA_MODEL)
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

# Caminho para salvar o contexto
HISTORICO_ARQUIVO = "historico_conversa.txt"
MAX_INTERACOES = 200  # Número máximo de interações armazenadas no contexto


def carregar_historico():
    """Carrega o histórico salvo de um arquivo, se existir."""
    if os.path.exists(HISTORICO_ARQUIVO):
        with open(HISTORICO_ARQUIVO, "r", encoding="utf-8") as file:
            return file.read()
    return ""


def salvar_historico(context):
    """Salva o histórico no arquivo com formatação adequada."""
    with open(HISTORICO_ARQUIVO, "w", encoding="utf-8") as file:
        file.write(context)


def limitar_contexto(context):
    """Limita o número de interações armazenadas no contexto."""
    interacoes = context.strip().split("\n\n")
    if len(interacoes) > MAX_INTERACOES:
        interacoes = interacoes[-MAX_INTERACOES:]  # Mantém apenas as últimas interações
    return "\n\n".join(interacoes)


def obter_resposta(context, pergunta):
    """Gera a resposta usando o modelo e retorna o contexto atualizado."""
    try:
        result = chain.invoke(
            {"context": context, "question": pergunta, "data_hora": obter_data_hora()}
        )
        return result.strip()  # Remove espaços em branco desnecessários
    except Exception as e:
        return f"Erro ao processar a resposta: {e}"


def obter_data_hora():
    """Retorna a data e hora atual formatada."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def manter_conversa():
    """Função principal para manter a conversa."""
    context = carregar_historico()  # Carrega o histórico existente, se disponível
    print(f"Seja bem-vindo ao ICEBERG IA (Modelo: {IA_MODEL})")
    print("Digite 'sair' para encerrar o chatbot.\n")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Encerrando a conversa. Até mais!")
            salvar_historico(context)  # Salva o histórico ao encerrar
            break

        # Obter resposta
        resposta = obter_resposta(context, user_input)
        print("Bot:", resposta)

        # Obter data e hora
        data_hora = obter_data_hora()

        # Atualizar o contexto com data e hora
        context += (
            f"[{data_hora}] | Você: {user_input}\n[{data_hora}] Bot: {resposta}\n\n"
        )
        context = limitar_contexto(context)


if __name__ == "__main__":
    manter_conversa()
