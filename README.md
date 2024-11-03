# ShellSenses

ShellSenses é um assistente de terminal inteligente que interpreta comandos em linguagem natural e executa ações no terminal, incluindo a criação de arquivos e pastas automaticamente, ou a execução de comandos de shell. O projeto utiliza a API do ChatGPT para interpretar a entrada do usuário e convertê-la em comandos específicos.

## Índice

- [Introdução](#introdução)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
  - [Comandos Shell](#comandos-shell)
  - [Criação de Arquivos e Pastas](#criação-de-arquivos-e-pastas)
- [Licença](#licença)

## Introdução

O ShellSenses permite que usuários interajam com o terminal usando descrições em linguagem natural. Com este assistente, você pode:

- Executar comandos shell com o prefixo `run:`.
- Criar arquivos e pastas automaticamente com o prefixo `create:`, incluindo conteúdo básico com base no tipo de arquivo.

O projeto foi desenvolvido com o objetivo de facilitar a criação e execução de comandos no terminal para usuários que desejam uma interface mais amigável.

## Pré-requisitos

- Python 3.6 ou superior
- Uma conta no [OpenAI](https://platform.openai.com) para obter a API key do ChatGPT
- Biblioteca `openai` instalada
- Biblioteca `dotenv` instalada para configurar variáveis de ambiente

## Instalação

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/shellsenses.git
cd shellsenses
```

Instale as dependências necessárias com o comando:

```bash
pip install -r requirements.txt
```

## Configuração

Para que o ShellSenses funcione corretamente, você precisa configurar sua API key do OpenAI. 

1. **Obtenha sua API key do ChatGPT**:
   - Acesse [OpenAI API](https://platform.openai.com) e crie uma API key na sua conta.

2. **Crie um arquivo `.env`** na raiz do projeto e adicione sua API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Configure o modelo** desejado no arquivo `config/config.yaml`:

   ```yaml
   openai:
     model: "gpt-4o-mini"  # Defina o modelo de sua preferência aqui
   ```

## Uso

Execute o script principal `main.py` para iniciar o ShellSenses:

```bash
python src/main.py
```

### Comandos Shell

Para executar um comando de shell, use o prefixo `run:` seguido da descrição do comando em linguagem natural. O ShellSenses interpretará a descrição e executará o comando shell correspondente.

#### Exemplo:

```plaintext
ShellSenses> run: crie uma nova pasta chamada projetos
```

O ShellSenses converterá isso em um comando shell real (como `mkdir projetos`) e perguntará se você deseja executá-lo.

### Criação de Arquivos e Pastas

Para criar arquivos e pastas com conteúdo automaticamente, use o prefixo `create:` seguido de uma descrição em linguagem natural. O ShellSenses interpretará a descrição e criará as pastas e arquivos necessários com conteúdo básico.

#### Exemplo:

```plaintext
ShellSenses> create: crie uma pasta chamada documentos com um arquivo de texto chamado notas.txt com o conteúdo "Minhas notas iniciais"
```

O ShellSenses irá criar a pasta `documentos`, o arquivo `notas.txt` dentro dela e preencher o conteúdo conforme solicitado.

### Estrutura dos Comandos

Aqui estão alguns exemplos de comandos e suas funções:

- **run:** Executa comandos shell interpretados pelo ChatGPT.
  - Exemplo: `run: liste todos os arquivos nesta pasta`
- **create:** Cria arquivos ou pastas automaticamente com conteúdo básico.
  - Exemplo: `create: crie um arquivo HTML básico chamado index.html`

> **Observação**: O ShellSenses utiliza o ChatGPT para interpretar comandos em linguagem natural. Tenha cuidado ao executar comandos shell, especialmente aqueles que podem alterar ou remover dados.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.

