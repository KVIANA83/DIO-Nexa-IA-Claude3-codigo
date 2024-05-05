class ModeloIA:
    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades
    
    def __str__(self):
        return self.nome

# Função para recomendar um modelo de IA com base nas características desejadas:
def recomendar_modelo(caracteristicas):
    modelo_recomendado = None
    
    # Aqui é convertido as capacidades inseridas pelo usuário para minúsculas:
    capacidades_usuario = [capacidade.lower() for capacidade in caracteristicas['Capacidades']]

    for modelo in modelos:
        # Convertemos as capacidades do modelo para minúsculas:
        capacidades_modelo = [capacidade.lower() for capacidade in modelo.capacidades]
        
        if all(capacidade in capacidades_usuario for capacidade in capacidades_modelo):
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo

    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."

# Função para solicitar características desejadas ao usuário:
def obter_caracteristicas():
    caracteristicas = {}
    caracteristicas['Desempenho'] = int(input())
    caracteristicas['Velocidade'] = int(input())
    caracteristicas['Custo'] = int(input())
    capacidades = input().split(',')
    caracteristicas['Capacidades'] = [capacidade.strip() for capacidade in capacidades]
    return caracteristicas

# Definindo a lista de modelos disponíveis:
modelos = [
    ModeloIA("Claude 3 Opus", 9, 10, 5, ["pesquisa", "desenvolvimento acelerado"]),
    ModeloIA("Claude 3 Sonnet", 8, 5, 7, ["codificação", "recuperação de informações"]),
    ModeloIA("Claude 3 Haiku", 7, 9, 6, ["velocidade", "resumo de dados não estruturados"])
]

# Obtém as características desejadas do usuário:
caracteristicas_entrada = obter_caracteristicas()

# Recomenda o melhor modelo com base nas características:
melhor_modelo = recomendar_modelo(caracteristicas_entrada)

# Gera uma explicação para o modelo recomendado:
explicacao = f"O {melhor_modelo.nome} é o modelo recomendado." if melhor_modelo != "Nenhum modelo encontrado." else "Nenhum modelo encontrado."

print(explicacao)
