import os
import readline
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Define o template de prompt para o chatbot, que inclui informações de data/hora e histórico de conversa.
template = """
Você é ICEBERG IA, um chatbot útil. Responda à pergunta do usuário de maneira clara, lógica, concisa e objetiva, levando em consideração o contexto da conversa.
--- Informações gerais ---
Data e hora atual: {data_hora}
--- Fim das informações ---

--- Histórico da conversa ---
{context}
--- Fim do histórico ---

Pergunta do usuário:
<｜User｜>{question}

<｜Assistant｜> Resposta:
"""

# Define o modelo de IA a ser usado.
# Recomenda-se o modelo DeepSeek-R1:8b por ser eficiente e oferecer boas respostas.
IA_MODEL = "deepseek-r1:8b"

# Configuração do modelo e template
model = OllamaLLM(model=IA_MODEL)  # Inicializa o modelo com o nome especificado
prompt = ChatPromptTemplate.from_template(template)  # Cria um template de prompt

# Combina o template e o modelo para formar uma cadeia de processamento
chain = prompt | model

# Configurações do histórico
HISTORICO_ARQUIVO = "historico_conversa.txt"  # Nome do arquivo para salvar o histórico
MAX_INTERACOES = 200  # Número máximo de interações mantidas no contexto


def carregar_historico():
    """Carrega o histórico salvo de um arquivo, se existir."""
    if os.path.exists(HISTORICO_ARQUIVO):  # Verifica se o arquivo existe
        with open(HISTORICO_ARQUIVO, "r", encoding="utf-8") as file:
            return file.read()  # Retorna o conteúdo do arquivo
    return ""  # Retorna uma string vazia se o arquivo não existir


def salvar_historico(context):
    """Salva o histórico no arquivo com formatação adequada."""
    with open(HISTORICO_ARQUIVO, "w", encoding="utf-8") as file:
        file.write(context)  # Escreve o contexto no arquivo


def limitar_contexto(context):
    """Limita o número de interações armazenadas no contexto."""
    interacoes = context.strip().split(
        "\n\n"
    )  # Divide o contexto em interações separadas
    if len(interacoes) > MAX_INTERACOES:
        interacoes = interacoes[-MAX_INTERACOES:]  # Mantém apenas as últimas interações
    return "\n\n".join(interacoes)  # Reconstroi o contexto com as interações limitadas


def obter_resposta(context, pergunta):
    """Gera a resposta usando o modelo e retorna o contexto atualizado."""
    try:
        result = chain.invoke(
            {"context": context, "question": pergunta, "data_hora": obter_data_hora()}
        )
        return result.strip()  # Remove espaços em branco desnecessários
    except Exception as e:
        return f"Erro ao processar a resposta: {e}"  # Retorna o erro em caso de falha


def obter_data_hora():
    """Retorna a data e hora atual formatada."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def manter_conversa():
    """Função principal para manter a conversa."""
    context = carregar_historico()  # Carrega o histórico existente, se disponível
    print(f"Seja bem-vindo ao ICEBERG IA (Modelo: {IA_MODEL})")
    print("Digite 'sair' para encerrar o chatbot.\n")

    while True:
        user_input = input("Você: ")  # Recebe a entrada do usuário
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
        context = limitar_contexto(
            context
        )  # Limita o contexto ao número máximo permitido


if __name__ == "__main__":
    manter_conversa()
