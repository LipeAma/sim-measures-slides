# 🚀 Apresentação Interativa com Manim Slides

Este repositório contém o código e os comandos necessários para gerar uma apresentação interativa usando a biblioteca **Manim** e a ferramenta **manim-slides**.
Acesse em https://lipeama.github.io/sim-measures-slides/

---

## 💻 Passos para a Execução

Siga os passos abaixo para preparar e renderizar a apresentação.

### 1. Instalação e Configuração

Você precisará das dependências do projeto para rodar o código.

* **Com Nix (Recomendado):**
    Se estiver usando o **Nix** (ou **NixOS**), basta executar o comando abaixo para entrar em um *shell* de desenvolvimento com todas as dependências instaladas:
    ```bash
    nix develop
    ```

* **Sem Nix:**
    Caso não esteja usando Nix, você precisará instalar as dependências manualmente, que incluem o `manim` e o `manim-slides`.

### 2. Preparação do Código

O código da sua apresentação, geralmente vindo de um *notebook* ou script Python, deve ser colocado no arquivo principal.

* Coloque o código da sua apresentação no caminho:
    ```
    src/main.py
    ```

### 3. Renderização das Cenas

Após configurar o ambiente e adicionar o código, você pode renderizar as cenas da apresentação.

* Rode o comando de renderização com a lista exata das classes/funções que compõem os slides:

    ```bash
    manim-slides render src/main.py DefineI DefineEmbeddingFunction Proposition ProofA1 ProofA2 ProofA3 ProofA4 SimilarityMeasureDef Proposition3 ProofS1 ProofS2 ProofS3 DefineIVFSEmbedding IVFSSimilarityMeasure ObjectSimilarityProposition ProofP1IVFS ProofP2IVFS ProofP3IVFS ProofP4IVFS HierarchicalClusteringAlgorithm ExampleWalkthrough ExampleWalkthroughPart2
    ```

---

## 🌐 Geração do Arquivo HTML

Após a renderização das cenas, o comando a seguir as agrupará em um único arquivo HTML interativo e *offline*.

* Rode o comando para converter as cenas renderizadas em um arquivo HTML único:

    ```bash
    manim-slides convert --one-file --offline DefineI DefineEmbeddingFunction Proposition ProofA1 ProofA2 ProofA3 ProofA4 SimilarityMeasureDef Proposition3 ProofS1 ProofS2 ProofS3 DefineIVFSEmbedding IVFSSimilarityMeasure ObjectSimilarityProposition ProofP1IVFS ProofP2IVFS ProofP3IVFS ProofP4IVFS HierarchicalClusteringAlgorithm ExampleWalkthrough ExampleWalkthroughPart2 out.html
    ```

O resultado será o arquivo **`out.html`**, que você pode abrir em qualquer navegador para visualizar a apresentação.
