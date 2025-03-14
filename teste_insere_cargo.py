from funcoes import fn_insere_cargo, fn_exclui_cargos

nome_cargo = 'Vaga de Gestor Comercial de B2B'
 
atividades = ['Gerenciar o time Comercial',
                'Desenhar estratégias de B2B para escalar o faturamento'
                'Definir e acompanhar metas do B2B com o time'
                'Acompanhar e ajudar o time a executar as estratégias definidas'
                'Reportar resultados e projeções dos seus KPIs']

prerequisitos = ['Experiência comprovada como Gestor de Vendas, Líder Comercial, Diretor Comercial ou afins',
                'Experiência comprovada em Vendas B2B (business to business)',
                'Experiência em empresas de Infoprodutos',
                'Proatividade e curiosidade, buscando constantemente aprender e melhorar as habilidades',
                'Foco em bater as metas estabelecidas para o time de Vendas',
                'Disponibilidade para trabalho em período integral (full time)']

diferenciais = ['Conhecimento da metodologia VTSD (Leandro Ladeira)',
                'Conhecimento avançado de Funis de Venda, com uma abordagem estratégica e eficaz na aquisição e retenção de clientes',
                'Interesse por Programação e Tecnologia (fique tranquilo, NÃO é necessário saber programar)',
                'Experiência como Gestor Comercial no nicho de Tecnologia em geral, Programação ou Data Science, proporcionando uma compreensão mais profunda do nosso público-alvo']
fn_exclui_cargos()

fn_insere_cargo(1, nome_cargo,  prerequisitos, diferenciais, atividades)

