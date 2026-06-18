# Guia Básico de Git 🌳

Este guia foi feito para quem **nunca usou Git** e quer entender as funcionalidades mais importantes do dia a dia.

---

## O que é o Git?

O **Git** é um sistema de **controle de versão**. Na prática, ele funciona como uma "máquina do tempo" para o seu projeto: ele registra cada alteração que você faz nos arquivos, permitindo que você:

- Volte para versões anteriores do código.
- Saiba o que mudou, quando e por quem.
- Trabalhe em equipe sem sobrescrever o trabalho dos outros.
- Teste novas ideias sem quebrar o que já funciona.

> **Importante:** Git roda no **seu próprio computador**. Ele é diferente do GitHub (que é um serviço online). Veja mais no outro README.

---

## Instalação

- **Windows:** baixe em [git-scm.com](https://git-scm.com/)
- **Mac:** `brew install git` (ou já vem com as ferramentas de desenvolvedor)
- **Linux:** `sudo apt install git` (Debian/Ubuntu)

Para conferir se instalou:

```bash
git --version
```

---

## Configuração inicial (faça uma vez só)

Diga ao Git quem é você. Esse nome e e-mail aparecerão no histórico de alterações.

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

## Conceitos essenciais

| Termo | O que significa |
|-------|-----------------|
| **Repositório (repo)** | A pasta do seu projeto que o Git está monitorando. |
| **Commit** | Um "ponto de salvamento" do seu projeto, com uma mensagem descrevendo a mudança. |
| **Branch (ramo)** | Uma linha de trabalho paralela, onde você pode mexer sem afetar a versão principal. |
| **Staging area** | A "área de preparação": arquivos que você marcou para entrar no próximo commit. |

O fluxo geral é: **editar arquivos → adicionar ao staging (`add`) → salvar (`commit`)**.

---

## Comandos mais usados

### Começar um projeto

```bash
git init
```
Transforma a pasta atual em um repositório Git.

### Ver o estado atual

```bash
git status
```
Mostra quais arquivos foram modificados, quais estão prontos para commit, etc. **Use sempre que estiver na dúvida.**

### Adicionar arquivos ao próximo commit

```bash
git add nome-do-arquivo.txt   # adiciona um arquivo específico
git add .                     # adiciona todos os arquivos modificados
```

### Salvar as mudanças (commit)

```bash
git commit -m "Mensagem descrevendo o que mudou"
```
A mensagem deve ser curta e explicar **o que** você fez (ex: `"Adiciona tela de login"`).

### Ver o histórico

```bash
git log              # histórico completo
git log --oneline    # versão resumida, uma linha por commit
```

### Ver o que mudou

```bash
git diff             # mostra as alterações ainda não adicionadas ao staging
```

---

## Trabalhando com Branches (ramos)

Branches permitem desenvolver uma funcionalidade nova sem mexer no código principal (geralmente chamado de `main`).

```bash
git branch                      # lista as branches existentes
git branch nova-funcionalidade  # cria uma nova branch
git switch nova-funcionalidade  # muda para essa branch
```

Atalho para criar **e** já mudar para a branch:

```bash
git switch -c nova-funcionalidade
```

> Em versões mais antigas do Git, usa-se `git checkout` no lugar de `git switch`.

### Juntar uma branch na principal (merge)

Estando na branch `main`:

```bash
git merge nova-funcionalidade
```
Isso traz as alterações da branch `nova-funcionalidade` para a `main`.

---

## Desfazendo coisas

```bash
git restore arquivo.txt          # descarta alterações não salvas de um arquivo
git restore --staged arquivo.txt # tira um arquivo do staging (sem perder o conteúdo)
```

Para voltar a um commit anterior **mantendo o histórico**:

```bash
git revert <id-do-commit>
```

---

## O arquivo `.gitignore`

Alguns arquivos não devem ser monitorados (senhas, arquivos temporários, pastas como `node_modules`). Crie um arquivo chamado `.gitignore` na raiz do projeto e liste o que ignorar:

```
node_modules/
.env
*.log
.DS_Store
```

---

## Resumo do fluxo do dia a dia

```bash
git status                  # 1. Ver o que mudou
git add .                   # 2. Preparar as mudanças
git commit -m "mensagem"    # 3. Salvar as mudanças
```

E pronto! Com esses comandos você já consegue versionar qualquer projeto. 🚀


# Guia Básico de GitHub 🐙

Este guia foi feito para quem **nunca usou GitHub** e quer entender as funcionalidades mais importantes da plataforma.

---

## O que é o GitHub?

O **GitHub** é uma plataforma **online** que hospeda projetos que usam Git. Pense nele como uma "rede social para código": é onde você guarda seus repositórios na nuvem, compartilha com outras pessoas e colabora em equipe.

### Git x GitHub — qual a diferença?

| Git | GitHub |
|-----|--------|
| Programa que roda no **seu computador**. | Serviço **online** (site) na nuvem. |
| Controla as versões do projeto localmente. | Hospeda os repositórios na internet. |
| Funciona sem internet. | Precisa de internet. |
| Criado pela comunidade. | Empresa (da Microsoft). |

> Em resumo: **Git** é a ferramenta; **GitHub** é o lugar onde você guarda e compartilha o que fez com o Git. Existem alternativas ao GitHub, como GitLab e Bitbucket.

---

## Primeiros passos

1. Crie uma conta gratuita em [github.com](https://github.com/).
2. Confirme seu e-mail.
3. (Opcional, mas recomendado) Configure uma **chave SSH** ou um **token** para conseguir enviar código sem digitar senha toda hora.

---

## Criando um repositório

1. Clique no botão **"New"** (ou no `+` no canto superior direito → *New repository*).
2. Dê um **nome** ao repositório.
3. Escolha entre **Público** (qualquer um vê) ou **Privado** (só você e quem autorizar).
4. Marque a opção de criar um arquivo **README** (recomendado).
5. Clique em **"Create repository"**.

---

## Conectando seu projeto local ao GitHub

Se você já tem um projeto no seu computador (usando Git), pode enviá-lo ao GitHub:

```bash
git remote add origin https://github.com/seu-usuario/seu-repo.git
git branch -M main
git push -u origin main
```

- `git remote add origin ...` → conecta seu projeto local ao repositório online.
- `git push` → **envia** seus commits do computador para o GitHub.
- `git pull` → **baixa** as atualizações do GitHub para o seu computador.

### Clonar (baixar) um projeto existente

```bash
git clone https://github.com/usuario/projeto.git
```
Isso copia um repositório do GitHub para o seu computador.

---

## Funcionalidades mais usadas

### 📥 Push e Pull
- **Push** (`git push`): envia suas alterações locais para o GitHub.
- **Pull** (`git pull`): traz as alterações que estão no GitHub para o seu computador. Sempre dê `pull` antes de começar a trabalhar para ter a versão mais recente.

### 🍴 Fork
Cria uma **cópia do repositório de outra pessoa** na sua própria conta. Muito usado para contribuir com projetos de código aberto sem precisar de permissão direta.

### 🔀 Pull Request (PR)
É o coração da colaboração no GitHub. Um Pull Request é um **pedido para juntar suas alterações** ao projeto. O fluxo típico é:

1. Você cria uma branch e faz suas alterações.
2. Envia a branch para o GitHub (`git push`).
3. Abre um **Pull Request** explicando o que mudou.
4. Outras pessoas **revisam**, comentam e aprovam.
5. As mudanças são **mescladas (merge)** ao projeto principal.

### 🐛 Issues
São os "tickets" do projeto. Servem para:
- Relatar **bugs** (erros).
- Sugerir **novas funcionalidades**.
- Organizar **tarefas** e discussões.

Você pode atribuir issues a pessoas, adicionar etiquetas (*labels*) e marcos (*milestones*).

### ⭐ Star
É como "curtir" e salvar um repositório que você gostou. Ajuda a encontrá-lo depois e demonstra apoio ao projeto.

### 👁️ Watch
"Seguir" um repositório para receber notificações sobre tudo que acontece nele (novas issues, PRs, etc.).

### 📄 README.md
O arquivo que aparece na página inicial do repositório. É o "cartão de visitas" do projeto: explica o que ele faz, como instalar e como usar. (Você está lendo um exemplo de README agora!)

---

## Recursos extras úteis

| Recurso | Para que serve |
|---------|----------------|
| **GitHub Actions** | Automatiza tarefas (testes, deploy) automaticamente a cada push. |
| **GitHub Pages** | Hospeda um site gratuitamente direto do seu repositório. |
| **Projects** | Quadro estilo Kanban para organizar tarefas. |
| **Wiki** | Documentação mais extensa do projeto. |
| **Releases** | Publica versões oficiais e prontas do seu projeto. |
| **Gist** | Compartilha trechos de código rápidos e isolados. |

---

## Fluxo de colaboração típico

```bash
git pull                       # 1. Baixa as últimas atualizações
git switch -c minha-feature    # 2. Cria uma branch para sua tarefa
# ... faça suas alterações ...
git add .                      # 3. Prepara as mudanças
git commit -m "mensagem"       # 4. Salva localmente
git push -u origin minha-feature  # 5. Envia para o GitHub
# 6. Abra um Pull Request no site do GitHub
```

---

Com isso você já tem o essencial para colaborar e compartilhar projetos no GitHub. Bons commits! 🚀

