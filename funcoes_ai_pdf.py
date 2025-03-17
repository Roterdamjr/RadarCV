import fitz
from funcoes import fn_busca_conteudo_curriculo

def fn_busca_job():
  return '''
activities
Gerenciar o time Comercial
Desenhar estratégias de B2B para escalar o faturamento
Definir e acompanhar metas do B2B com o time
Acompanhar e ajudar o time a executar as estratégias definidas
Reportar resultados e projeções dos seus KPIs


prequisites
Experiência comprovada como Gestor de Vendas, Líder Comercial, Diretor Comercial ou afins
Experiência comprovada em Vendas B2B (business to business)
Experiência em empresas de Infoprodutos
Proatividade e curiosidade, buscando constantemente aprender e melhorar as habilidades.
Foco em bater as metas estabelecidas para o time de Vendas
Disponibilidade para trabalho em período integral (full time)


differentials
Conhecimento da metodologia VTSD (Leandro Ladeira)
Conhecimento avançado de Funis de Venda, com uma abordagem estratégica e eficaz na aquisição e retenção de clientes
Interesse por Programação e Tecnologia (fique tranquilo, NÃO é necessário saber programar)
Experiência como Gestor Comercial no nicho de Tecnologia em geral, Programação ou Data Science, proporcionando uma compreensão mais profunda do nosso público-alvo

       '''



def fn_busca_resumo(file_path):

  text = '''
              "Objetivo:** Avaliar um currículo com base em uma vaga específica e calcular a pontuação final. A nota máxima é 10.0.
              '''

  text +=  fn_busca_conteudo_curriculo(file_path)
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