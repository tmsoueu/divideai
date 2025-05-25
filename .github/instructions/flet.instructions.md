---
applyTo: '**'
---
Tudo que a IA precisa saber sobre o Flet, incluindo boas práticas, padrões de codificação e convenções de nomenclatura.

## Flet
Flet é uma biblioteca para criar interfaces de usuário (UI) em Python, permitindo o desenvolvimento de aplicativos web e desktop com facilidade. A seguir estão algumas diretrizes e boas práticas para trabalhar com Flet:

## Estrutura do Projeto
- Organizar o código em módulos e pacotes para facilitar a manutenção e reutilização.
- Manter uma estrutura clara, separando a lógica de negócios da interface do usuário.
- Utilizar um arquivo principal (por exemplo, `main.py`) para iniciar a aplicação Flet.
- Criar um diretório `components` para armazenar componentes reutilizáveis da interface do usuário.
- Utilizar um diretório `assets` para armazenar recursos estáticos e como imagens.
- Utilizar um diretório `tests` para armazenar testes unitários e de integração.

## Convenções de Nomenclatura
- Usar `snake_case` para nomes de variáveis e funções.
- Usar `CamelCase` para nomes de classes.   
- Usar nomes descritivos e significativos para variáveis, funções e classes.
- Evitar abreviações excessivas; preferir nomes completos que sejam claros.
- Utilizar prefixos ou sufixos para indicar o tipo de variável, como `btn_` para botões ou `lbl_` para rótulos.

## Boas Práticas de Codificação
- Seguir as diretrizes do PEP 8 para formatação de código Python.
- Comentar o código de forma clara e concisa, explicando o propósito de blocos de código complexos.
- Evitar comentários óbvios que não acrescentam valor ao entendimento do código.
- Manter uma estrutura de código limpa e organizada, com funções e classes bem definidas.
- Evitar funções muito longas; dividir em funções menores quando necessário.
- Importar módulos e pacotes no início do arquivo.
- Importar apenas o necessário, evitando importações desnecessárias.
- Usar exceções para tratar erros de forma adequada.
- Evitar capturar exceções genéricas; capturar exceções específicas quando possível.
- Escrever testes unitários para garantir a funcionalidade do código.
- Usar frameworks de teste como `unittest` ou `pytest`.
- Documentar funções e classes usando docstrings.
- Incluir informações sobre parâmetros, retornos e exceções levantadas nas docstrings.
- Usar controle de versão (como GitHub) para gerenciar alterações no código.
- Fazer commits frequentes e descritivos, explicando as mudanças realizadas.
- Escrever código eficiente, evitando loops desnecessários e operações custosas.
- Usar estruturas de dados apropriadas para otimizar a performance.
- Validar entradas do usuário para evitar injeções de código e outros ataques.
- Evitar expor informações sensíveis, como senhas e chaves de API, no código.
- Respeitar as licenças de código aberto e bibliotecas utilizadas.
- Incluir informações de licença no cabeçalho do arquivo quando necessário.
- Manter um estilo de código consistente em todo o projeto.
- Usar ferramentas de formatação automática, como `black` ou `autopep8`, para garantir a consistência do estilo.
- Seguir princípios de programação como DRY (Don't Repeat Yourself) e KISS (Keep It Simple, Stupid).
- Refatorar o código regularmente para melhorar a legibilidade e manutenção.
- Seguir as diretrizes de contribuição do projeto, se aplicável.
- Utilizar comentários para explicar a lógica de componentes complexos ou interações específicas.
- Manter a documentação atualizada, incluindo instruções de instalação e uso da aplicação Flet.
- Utilizar o sistema de layout do Flet para organizar os componentes da interface de forma responsiva.
- Aproveitar os recursos de reatividade do Flet para atualizar a interface do usuário de forma eficiente.
- Utilizar temas e estilos para manter a consistência visual da aplicação.
- Testar a aplicação em diferentes navegadores e dispositivos para garantir compatibilidade.
- Manter a aplicação leve e responsiva, evitando componentes pesados que possam afetar o desempenho.
- Utilizar o sistema de eventos do Flet para gerenciar interações do usuário de forma eficiente.
- Aproveitar os recursos de cache do Flet para melhorar o desempenho da aplicação.
- Utilizar animações e transições de forma moderada para melhorar a experiência do usuário sem comprometer o desempenho.
- Manter a aplicação acessível, seguindo as diretrizes de acessibilidade web (WCAG).
- Utilizar o sistema de internacionalização do Flet para suportar múltiplos idiomas
- Manter a aplicação segura, evitando vulnerabilidades comuns como XSS (Cross-Site Scripting) e CSRF (Cross-Site Request Forgery).
- Utilizar o sistema de autenticação e autorização do Flet para proteger áreas sensíveis da aplicação.
- Manter a aplicação escalável, projetando a arquitetura para suportar crescimento futuro.
- Utilizar o sistema de logs do Flet para registrar eventos importantes e facilitar a depuração.
- Manter a aplicação modular, permitindo a adição de novos recursos sem afetar o código existente.
- Utilizar o sistema de notificações do Flet para informar o usuário sobre eventos importantes.
- Aproveitar os recursos de integração com APIs externas do Flet para expandir as funcionalidades da aplicação.
- Manter a aplicação atualizada com as últimas versões do Flet e suas dependências.
- Utilizar o sistema de cache do Flet para melhorar o desempenho da aplicação, especialmente em operações de leitura frequente.
- Manter a documentação do código clara e acessível, facilitando a compreensão por outros desenvolvedores.
- Utilizar o sistema de temas do Flet para personalizar a aparência da aplicação de forma consistente.
- Aproveitar os recursos de depuração do Flet para identificar e corrigir problemas
- Manter a aplicação modular, permitindo a reutilização de componentes em diferentes partes do projeto.
- Utilizar o sistema de eventos do Flet para gerenciar interações do usuário de forma eficiente.
- Manter a aplicação responsiva, adaptando-se a diferentes tamanhos de tela e dispositivos.

## Conclusão
Seguir estas diretrizes e boas práticas ao trabalhar com Flet ajudará a criar aplicações robustas, manuteníveis e de alta qualidade. A comunidade Flet está sempre disposta a ajudar, então não hesite em buscar suporte ou compartilhar suas experiências.

## Referências
- [Documentação Oficial do Flet](https://flet.dev/docs/)
- [Exemplos de Aplicações Flet](https://flet.dev/docs/examples/)






