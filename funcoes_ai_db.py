from tinydb import TinyDB, Query


def fn_quebra_linhas(titulo, lista):
    texto = ""
    for item in lista:
        texto += item + '\n'
    return titulo + '\n' + texto + '\n\n'

def fn_busca_curriculo_db(nome_candidato):
    db = TinyDB('curriculos.json')
    QueryDB = Query()
    resultado = db.search(QueryDB.nome == nome_candidato)

    if resultado:
        return resultado[0]['content']
    else:
        return "    " 

def fn_busca_job():

    db = TinyDB("cargos.json")  # Substitua pelo nome correto do arquivo
    dados = db.storage.read()

    if dados:
        dados = db.all()  # Pega todos os registros corretamente
        for vaga in dados:
            nome_vaga = vaga.get("nome", "Nome não encontrado")

            prerequisitos = vaga.get("prerequisitos", [])
            prerequisitos = [p.strip("',") for p in prerequisitos]

            diferenciais = vaga.get("diferenciais", [])
            diferenciais = [p.strip("',") for p in diferenciais]

            principais_atividades = vaga.get("principais_atividades", [])
            principais_atividades = [p.strip("',") for p in principais_atividades]

    else:
        print("Nenhuma vaga encontrada no banco de dados.")

    return fn_quebra_linhas('prerequisitos', prerequisitos) + fn_quebra_linhas('diferenciais',diferenciais) + fn_quebra_linhas('principais_atividades',principais_atividades)

def fn_busca_resumo(curriculo):
    text = '''
              "Objetivo:** Avaliar um currículo com base em uma vaga específica e calcular a pontuação final. A nota máxima é 10.0.
              '''
    
    text +=  curriculo

    text += '''
              Por favor, gere um resumo do currículo fornecido, formatado em Markdown, seguindo rigorosamente o modelo abaixo. **Não adicione seções extras, tabelas ou qualquer outro tipo de formatação diferente da especificada.** Preencha cada seção com as informações relevantes, garantindo que o resumo seja preciso e focado.

            **Formato de Output Esperado:**

            ```markdown
            ## Nome Completo
            nome_completo aqui

            ## Experiência
            experiencia aqui

            ## Habilidades
            habilidades aqui

            ## Educação
            educacao aqui

            ## Idiomas
            idiomas aqui
            '''
    return text

def fn_busca_opiniao(cv, job ):
    text ='''
          Por favor, analise o currículo fornecido em relação à descrição da vaga aplicada e crie uma opinião ultra crítica e detalhada. A sua análise deve incluir os seguintes pontos:
            Você deve pensar como o recrutador chefe que está analisando e gerando uma opnião descritiva sobre o curriculo do canditato que se candidatou para a vaga

            Formate a resposta de forma profissional, coloque titulos grandes nas sessões.

            1. **Pontos de Alinhamento**: Identifique e discuta os aspectos do currículo que estão diretamente alinhados com os requisitos da vaga. Inclua exemplos específicos de experiências, habilidades ou qualificações que correspondem ao que a vaga está procurando.

            2. **Pontos de Desalinhamento**: Destaque e discuta as áreas onde o candidato não atende aos requisitos da vaga. Isso pode incluir falta de experiência em áreas chave, ausência de habilidades técnicas específicas, ou qualificações que não correspondem às expectativas da vaga.

            3. **Pontos de Atenção**: Identifique e discuta características do currículo que merecem atenção especial. Isso pode incluir aspectos como a frequência com que o candidato troca de emprego, lacunas no histórico de trabalho, ou características pessoais que podem influenciar o desempenho no cargo, tanto de maneira positiva quanto negativa.

            Sua análise deve ser objetiva, baseada em evidências apresentadas no currículo e na descrição da vaga. Seja detalhado e forneça uma avaliação honesta dos pontos fortes e fracos do candidato em relação à vaga.

            **Currículo Original:**
        '''
    text += cv  +  '**Descrição da Vaga:** '+ job
    text += 'Você deve devolver essa analise critica formatada como se fosse um relatorio analitico do curriculum com a vaga, deve estar formatado com titulos grandes em destaques'
    
    return text

def fn_gerar_score(cv, job):
    text ='''
            **Objetivo:** Avaliar um currículo com base em uma vaga específica e calcular a pontuação final. A nota máxima é 10.0.

            **Instruções:**

            1. **Experiência (Peso: 30%)**: Avalie a relevância da experiência em relação à vaga.
            2. **Habilidades Técnicas (Peso: 25%)**: Verifique o alinhamento das habilidades técnicas com os requisitos da vaga.
            3. **Educação (Peso: 10%)**: Avalie a relevância da formação acadêmica para a vaga.
            4. **Idiomas (Peso: 10%)**: Avalie os idiomas e sua proficiência em relação à vaga.
            5. **Pontos Fortes (Peso: 15%)**: Avalie a relevância dos pontos fortes para a vaga.
            6. **Pontos Fracos (Desconto de até 10%)**: Avalie a gravidade dos pontos fracos em relação à vaga.

            Curriculo do candidato
            '''
   
    text += cv
    text += 'Vaga que o candidato está se candidatando' + job
    return text

