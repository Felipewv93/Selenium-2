# Selenium - Parte 2

Projeto de estudos de automação web usando Python e Selenium WebDriver, que faz parte da disciplina de **Automação de Testes de Software**.

## Objetivo

O script automatiza três páginas em abas diferentes do navegador:

- seleciona `Option 1` em um dropdown do site The Internet;
- inicia um carregamento dinâmico e captura o texto exibido;
- acessa a Wikipédia, pesquisa por `Automação` e coleta o link `Conteúdo destacado`;
- salva uma captura de tela como evidência da automação.

## Requisitos

- Python 3.10 ou superior;
- Google Chrome instalado;
- conexão com a internet;

O Selenium utiliza o gerenciamento automático do navegador para localizar o ChromeDriver compatível.

## Instalação

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Execução

Execute o script com:

```powershell
python automacao_selenium.py
```

O navegador é executado em modo headless, portanto a janela não será exibida. Para acompanhar a execução visualmente, remova ou comente a linha abaixo no script:

```python
options.add_argument("--headless=new")
```

## Resultado

Durante a execução, o terminal exibe os títulos das abas, a opção selecionada, o texto carregado e o endereço do link encontrado na Wikipédia.

A captura de tela é salva em:

```text
assets/evidencia_wiki.png
```

## Estrutura

```text
.selenium2
├── automacao_selenium.py
├── assets/
│   └── evidencia_wiki.png
├── requirements.txt
└── README.md
```

## Observações

As páginas utilizadas são externas e podem alterar sua estrutura. Caso algum seletor deixe de funcionar, será necessário atualizar os localizadores no script.

## Autor

**Felipe Viana**