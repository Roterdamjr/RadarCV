from google import genai

client = genai.Client(api_key="AIzaSyAA4_6qB-yAnwmmutcY4nytgQBlw1YWrtA")

trecho_01 = ''' 
              "Objetivo:** Avaliar um currículo com base em uma vaga específica e calcular a pontuação final. A nota máxima é 10.0.

        **Instruções:**

        1. **Experiência (Peso: 30%)**: Avalie a relevância da experiência em relação à vaga.
        2. **Habilidades Técnicas (Peso: 25%)**: Verifique o alinhamento das habilidades técnicas com os requisitos da vaga.
        3. **Educação (Peso: 10%)**: Avalie a relevância da formação acadêmica para a vaga.
        4. **Idiomas (Peso: 10%)**: Avalie os idiomas e sua proficiência em relação à vaga.
        5. **Pontos Fortes (Peso: 15%)**: Avalie a relevância dos pontos fortes para a vaga.
        6. **Pontos Fracos (Desconto de até 10%)**: Avalie a gravidade dos pontos fracos em relação à vaga."
              '''
trecho_02 = '''
Curriculo do candidato

PEDRO ARGENTO H. CAVALCANTE
Rio de Janeiro, RJ | ��+55 (21) 98869-1629 | ✉️ pedroargento16@gmail.com
��linkedin.com/in/pedroargentoholanda
SUMMARY
Talent Acquisition | Recruitment | Headhunting | R&S | Manpower | RPO
�� 4 years-experience in Talent Acquisition/R&S, providing services to international clients (US, Canada and LATAM). Expertise in full-cycle recruitment within the Oil & Gas industry, having employed and transformed over 300 lives through the world of work.
�� Expertise in high-volume recruitment projects, actively searching candidates through headhunting and talent acquisition strategies, having brought R$2.5M revenue within a 5 months project (Seadrill West Auriga/Polaris).
�� Responsible for placing high-quality candidates in key roles within Engineering, Procurement, and Construction (EPC) projects, as well as Supply Chain & Logistics, Finance/Accounting/Administration, Human Resources (HR) and operational positions.
EXPERIENCE
ICM PEOPLE - Remote Aug 2023 - Present Recruitment Consultant II
Recruitment for offshore Oil & Gas positions in Brazil and Latin America, as well as providing mentorship and guidance to team members.
Clients: Noble, Seadrill, Saudi Aramco, Valaris, Transocean and Ventura
● Delivered full-cycle recruitment processes, including talent sourcing, screening, and placement ● Conducted talent sourcing strategies using LinkedIn Recruiter, ATS Cornerstone and industry network, securing high-caliber candidates for specific technical roles
● Verifying candidates’ certifications and licenses, ensuring compliance with offshore regulations and reducing onboarding time significantly
● Initiating visa application processes for international hires, enabling faster deployment of qualified professionals
● Scheduling medical exams, sometimes within tight deadlines in order to meet client timelines ● Scheduling candidates’ medical exams with Personal Department
● Briefing positions with clients to understand staffing needs, align goals and expectations ● Mentored 5 junior recruiters, enhancing sourcing strategies and improving team submission rates
● Optimized resumes to highlight candidates’ key qualifications
SEADRILL - Rio de Janeiro, RJ Mar 2024 - Sep 2024 Talent Acquisition Partner (Temporary contract through ICM)
Seadrill is a global leader in offshore drilling services, specializing in advanced rigs for oil and gas exploration.
● Managed end-to-end recruitment of offshore workers for West Auriga and West Polaris drilling units, as well as for other rigs as needed.
● Placed around 150 candidates within tight deadlines, using tools such as LinkedIn Recruiter and Cornerstone ATS to build reliable candidate pipelines
● Developed and implemented proactive headhunting strategies, resulting in a significant increase of qualified candidate application in hard-to-fill roles
● Constantly communicated with HR Advisors to forecast and address staffing needs, ensuring project timelines were met
● Delivered high-volume recruitment solutions for operational, engineering, and technical roles, meeting stringent compliance and certification requirements.
AIRSWIFT - Rio de Janeiro, RJ Apr 2021 - Aug 2023 International Recruitment Consultant II (US & Canada) May 2022 - Aug 2023 Expertise in identifying and securing talent across Engineering, Procurement, and Construction, successfully placing 100+ professionals in niche roles.
Clients: Chevron, ExxonMobil, ConocoPhillips, Phillips 66, Shell, Marathon Petroleum, Total Energies, Valero, Chesapeake, ENI, BP, Equinor...
● Engineering Professionals: Civil, Mechanical (piping, HVAC, rotating equipment), Electrical (power distribution, control systems), Structural, Instrumentation & Control, and Process Engineers for industrial projects.
● Procurement: Procurement Managers, Contract Managers, Buyers, and Purchasers. ● Construction: HSE Technicians, QC/QA Engineers, Safety Officers, and Technicians. ● Project Controls: Project Managers, Cost Estimators, Planners/Schedulers, and Risk Managers.
● Warehouse and Logistics: Supply Chain Analysts, Warehouse Managers, Material Controllers, and Inventory Managers.
● Operational Roles: Lease Operators, Mechanics, Pipefitters, and Welders.
● Corporate Positions: Document Controllers, Accountants, Bookkeepers, and Administrative Professionals.
● Environmental and Regulatory Specialists: Environmental Engineers and Permitting Specialists.
Recruitment Consultant I (US, Canada and LATAM) Apr 2021 - May 2022 Responsible for attracting qualified candidates for companies in the Oil and Gas sector in the US and Canada.
● Keeping communication and doing online meetings with clients to better align expectations and needs
● Search, select, discuss profiles, interview, attract and close qualified candidates suitable for positions according to the client's needs;
● Conduct telephone interviews of potential candidates to present to hiring managers; ● Sending qualified candidates to clients in a short period of time, ranging from 1 to 4 days, depending on the specifications and qualifications required for the position;
● Search for potential professionals on Indeed, LinkedIn Recruiter, CareerBuilder, Dice and Bullhorn.
EDUCATION
● UFRJ - Rio de Janeiro, RJ - MBA/Post-Graduation – International Trade – Apr 2019 - Mar 2021 ● PUC-RJ - Rio de Janeiro, RJ Graduation – International Relations – Feb 2014 – Dec 2017
LANGUAGES
● English – Proficient/Fluent (C2)
○ CAE Certificate (Certificate of Advanced English) issued by the University of Cambridge, England;
○ Certificate level C2 by Studio Cambridge Institution (England) – Exchange Program during 2015;
○ ‘Cultura Inglesa’ English Course (2004 - 2014)
● Spanish - Intermediate

Vaga que o candidato está se candidatando

activities = Gerenciar o time Comercial
Desenhar estratégias de B2B para escalar o faturamento
Definir e acompanhar metas do B2B com o time
Acompanhar e ajudar o time a executar as estratégias definidas
Reportar resultados e projeções dos seus KPIs

prequisites =
Experiência comprovada como Gestor de Vendas, Líder Comercial, Diretor Comercial ou afins
Experiência comprovada em Vendas B2B (business to business)
Experiência em empresas de Infoprodutos
Proatividade e curiosidade, buscando constantemente aprender e melhorar as habilidades.
Foco em bater as metas estabelecidas para o time de Vendas
Disponibilidade para trabalho em período integral (full time)

differentials =
Conhecimento da metodologia VTSD (Leandro Ladeira)
Conhecimento avançado de Funis de Venda, com uma abordagem estratégica e eficaz na aquisição e retenção de clientes
Interesse por Programação e Tecnologia (fique tranquilo, NÃO é necessário saber programar)
Experiência como Gestor Comercial no nicho de Tecnologia em geral, Programação ou
Data Science, proporcionando uma compreensão mais profunda do nosso público-alvo
'''
trecho_03 =''' 
Analise o currículo fornecido em relação à descrição da vaga aplicada e crie uma opinião ultra crítica e detalhada. A sua análise deve incluir os seguintes pontos:
Você deve pensar como o recrutador chefe que está analisando e gerando uma opnião descritiva sobre o curriculo do canditato que se candidatou para a vaga

Formate a resposta de forma profissional, coloque titulos grandes nas sessões.

        1. **Pontos de Alinhamento**: Identifique e discuta os aspectos do currículo que estão diretamente alinhados com os requisitos da vaga. Inclua exemplos específicos de experiências, habilidades ou qualificações que correspondem ao que a vaga está procurando.

        2. **Pontos de Desalinhamento**: Destaque e discuta as áreas onde o candidato não atende aos requisitos da vaga. Isso pode incluir falta de experiência em áreas chave, ausência de habilidades técnicas específicas, ou qualificações que não correspondem às expectativas da vaga.

        3. **Pontos de Atenção**: Identifique e discuta características do currículo que merecem atenção especial. Isso pode incluir aspectos como a frequência com que o candidato troca de emprego, lacunas no histórico de trabalho, ou características pessoais que podem influenciar o desempenho no cargo, tanto de maneira positiva quanto negativa.

        Sua análise deve ser objetiva, baseada em evidências apresentadas no currículo e na descrição da vaga. Seja detalhado e forneça uma avaliação honesta dos pontos fortes e fracos do candidato em relação à vaga.
'''

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[trecho_01 + trecho_02])

for chunk in response:
    print(chunk.text, end="")

print('========================================================')

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[trecho_03])

for chunk in response:
    print(chunk.text, end="")