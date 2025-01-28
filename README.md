### 📌 **ICEBERG IA - Chatbot Inteligente com DeepSeek-R1**
**ICEBERG IA** é um chatbot interativo baseado em **modelos de IA avançados** e executado na **Ollama**, utilizando o modelo **DeepSeek-R1:8b** para processamento eficiente e inteligente de linguagem natural.

🚀 **Destaques do projeto:**
- Modelo de IA **DeepSeek-R1:8b**, altamente otimizado para desempenho superior em **raciocínio, código e matemática**.
- Persistência de **histórico de conversa** entre interações.
- Suporte para **comandos interativos** no terminal.
- Interface otimizada para **uso eficiente de memória e processamento**.

---

## 📦 **Instalação**
### 1️⃣ **Pré-requisitos**
Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:

- **Python** (>= 3.8)
- **Ollama** ([instalar aqui](https://ollama.ai/))
- **Gerenciador de dependências**: [UV](https://docs.astral.sh/uv/)
- **Dependências Python** (listadas no `pyproject.toml`)

### 2️⃣ **Baixar e instalar dependências**
Clone o repositório e instale as dependências:

```bash
git clone https://github.com/ICE3BR/chatbot-IA.git
cd chatbot-ia
uv sync
```

> ⚠️ **Nota:** Se estiver utilizando **WSL2** ou **Ubuntu**, garanta que a **Ollama** esteja configurada corretamente.

---

## 🚀 **Como executar**
Após instalar tudo, execute o chatbot com:

```bash
python main.py
```

🔹 O terminal exibirá a mensagem de boas-vindas:  
```bash
Seja bem-vindo ao ICEBERG IA (Modelo: deepseek-r1:8b)
Digite 'sair' para encerrar e salvar o histórico do o chatbot.
```

🔹 Agora, você pode interagir digitando suas perguntas e recebendo respostas contextuais.

---

## 🖥️ **Requisitos de Hardware**
O desempenho do **ICEBERG IA** varia de acordo com o modelo escolhido. Modelos maiores exigem mais memória e processamento para rodar de forma eficiente.

### 🔹 **Como escolher um modelo compatível com seu hardware?**
Cada modelo de IA possui um **tamanho de memória necessário** para ser carregado e processado corretamente. Como regra geral:

- **O tamanho do modelo indica a memória mínima necessária** para carregá-lo na GPU ou na RAM.
- **Se sua GPU não tiver VRAM suficiente, o processamento será feito na CPU**, o que pode resultar em respostas mais lentas.

| Modelo             | Parâmetros | Tamanho do Arquivo | Requisitos de Memória |
|--------------------|-----------|--------------------|----------------------|
| **DeepSeek-R1**    | 1.5B      | 2.7GB              | **3GB RAM/VRAM** |
| **DeepSeek-R1**    | 8B        | 4.9GB              | **5GB RAM/VRAM** |
| **DeepSeek-R1**    | 14B       | 7.5GB              | **8GB RAM/VRAM** |
| **DeepSeek-R1**    | 32B       | 16GB               | **16GB RAM/VRAM** |

💡 **Dica:**  
Se sua máquina **não possui GPU suficiente**, o modelo pode rodar via CPU, mas **o tempo de resposta será maior**.  
Se deseja **respostas mais rápidas**, recomenda-se **executar o chatbot em uma GPU com VRAM suficiente** para o modelo escolhido.

> **Exemplo:** Se você escolher o **DeepSeek-R1:8B**, que possui **4.9GB de tamanho**, sua GPU precisa de **pelo menos 5GB de VRAM disponível** para carregá-lo eficientemente.

---

## 🤖 **Modelos de IA disponíveis**
O **ICEBERG IA** suporta múltiplos modelos na **Ollama**. Atualmente, recomenda-se o **DeepSeek-R1:8b**, mas você pode alternar para outros modelos no código, alterando a variável `IA_MODEL`.

| Modelo             | Parâmetros | Tamanho  | Comando Ollama                        |
|--------------------|-----------|----------|---------------------------------------|
| **DeepSeek-R1**    | 8B        | 4.9GB    | `ollama run deepseek-r1:8b`          |
| **DeepSeek-R1**    | 1.5B      | 2.7GB    | `ollama run deepseek-r1:1.5b`        |
| **Llama 3.1**      | 8B        | 5.2GB    | `ollama run llama3.1:8b`             |
| **Llama 3.2**      | 3B        | 3.5GB    | `ollama run llama3.2:3b`             |

> 💡 **Recomendação:** O **DeepSeek-R1:8B** é um modelo **mais eficiente e rápido**, consumindo **menos recursos** e entregando um desempenho comparável ao **GPT-O1**.

### 🔹 **O que são os parâmetros?**
Os parâmetros de um modelo representam os pesos treináveis, indicando sua capacidade de raciocínio. Quanto maior o número de parâmetros, mais detalhadas e precisas são as respostas, mas também maior é o uso de memória e processamento. Modelos menores são mais leves, enquanto os maiores oferecem maior desempenho em tarefas complexas. 

---

## 💾 **Histórico de Conversa**
O chatbot mantém um **histórico de interações** no arquivo `historico_conversa.txt`, permitindo a continuidade do diálogo entre sessões.

🔹 **Formato do histórico salvo:**
```
[28-01-2025 15:30:45] | Você: Olá, como está?
[28-01-2025 15:30:47] Bot: Olá! Estou bem. Como posso te ajudar?
```

> 🔍 **Configuração:** O histórico é limitado a **200 interações** por padrão (`MAX_INTERACOES = 200`), mas pode ser alterado no código.

---

## 🛠️ **Personalizações**
Você pode modificar o comportamento do chatbot alterando o arquivo `main.py`:

### 📌 **Alterar modelo de IA**
Edite a variável `IA_MODEL` no código:

```python
IA_MODEL = "deepseek-r1:8b"  # Altere aqui para outro modelo
```

### 📌 **Alterar limite de histórico**
Modifique a constante `MAX_INTERACOES` para ajustar o número de mensagens armazenadas.

```python
MAX_INTERACOES = 100  # Define um novo limite
```

---

## 📜 **Licença**
Este projeto é distribuído sob a **MIT License**. O modelo **DeepSeek-R1** também é licenciado sob **MIT**, permitindo uso comercial e modificações.

🔗 **Mais informações sobre DeepSeek-R1:**  
[DeepSeek R1 no Ollama](https://ollama.ai/library/deepseek-r1)
