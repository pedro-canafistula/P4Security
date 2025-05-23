# P4Security
Projeto da matéria de Novas tecnologias

## Fluxo de Autenticação e Restrições de Segurança
### 1.Como funciona o fluxo de autenticação:
 - Quando um usuário acessa o site (/), verificamos se ele já está logado:
    - Se estiver logado (existe 'usuario_logado' na sessão), redirecionamos para o dashboard
    - Se não estiver logado, redirecionamos para a tela de login
 - Na tela de login (/login):
    - O usuário preenche o formulário com nome de usuário e senha
    - Ao enviar o formulário (método POST), verificamos se as credenciais são válidas
    - Se forem válidas, armazenamos informações na sessão e redirecionamos para o dashboard
    - Se forem inválidas, exibimos uma mensagem de erro e mantemos o usuário na tela de login
 - No dashboard (/dashboard):
    - Verificamos se o usuário está logado antes de mostrar o conteúdo
    - Se não estiver logado, redirecionamos para a tela de login com uma mensagem
 - No logout (/logout):
    - Removemos as informações do usuário da sessão
    - Redirecionamos para a tela de login
### 2.Como o Flask gerencia sessões:
O Flask usa cookies criptografados para armazenar dados de sessão
A secret_key é usada para criptografar esses cookies, por isso é importante usar uma chave segura
Quando armazenamos dados na sessão (session['usuario_logado'] = usuario), eles ficam disponíveis em todas as requisições do mesmo usuário
Os dados da sessão persistem até serem explicitamente removidos ou até o cookie expirar
### 3.Proteção de rotas:
Usamos verificações como if 'usuario_logado' not in session: para proteger rotas
Isso é chamado de "proteção manual de rotas" - cada função verifica se o usuário está autenticado
Em aplicações maiores, poderíamos usar decorators personalizados para simplificar essa proteção
### 4.Limitações e melhorias de segurança:
Nosso sistema atual armazena senhas em texto puro, o que não é seguro para ambientes reais
Em um sistema de produção, deveríamos:
Armazenar senhas com hash (usando bibliotecas como bcrypt ou passlib)
Implementar proteção contra ataques de brute force (limitando tentativas de login)
Usar HTTPS para criptografar a comunicação
Implementar autenticação de dois fatores
Usar um banco de dados real em vez de um dicionário em memória
### 5.Mensagens Flash:
O sistema de mensagens flash do Flask permite enviar mensagens temporárias entre requisições
Usamos flash('mensagem', 'categoria') para criar a mensagem
No template, recuperamos essas mensagens com get_flashed_messages()
As mensagens são exibidas apenas uma vez e depois desaparecem