# APIclassTrib

Este projeto acessa a API de Classificação Tributária do Portal da Conformidade Fiscal do RS, utilizando um certificado digital A1 (formato .pfx) para autenticação em requisições HTTPS.

---

## Objetivo

Baixar o arquivo classTrib.json diretamente da API oficial do Governo do Rio Grande do Sul, autenticando-se com um certificado A1 válido.

---

## 🛠️ Requisitos

- Python 3.8 ou superior
- Certificado digital A1 no formato .pfx
- Senha do certificado
- Acesso à internet   

---

## Instalação

### 1. Clone ou baixe o repositório
```bash
1. Clone ou baixe este repositório
git clone https://github.com/seu-usuario/APIclassTrib.git
cd APIclassTrib
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
```
Ative o ambiente:
```bash
venv\Scripts\activate
```
---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Configuração

1. Coloque seu certificado A1 (.pfx) na pasta Certificado/ com o nome Certificado.pfx
(ou ajuste o caminho no código conforme necessário).

2. Atualize a senha do certificado no arquivo principal (main.py ou onde estiver o if __name__ == "__main__"):
```bash
senha_certificado = "sua_senha_aqui"
```

## Execução

Com o ambiente ativado e dependências instaladas, execute:
```bash
python main.py
```
 
 O script fará uma requisição à API:
```bash
https://cff.svrs.rs.gov.br/api/v1/consultas/classTrib
```

E salvará a resposta em um arquivo chamado classTrib.json no diretório atual.

---
 
## Segurança

- Os arquivos PEM (chave privada e certificado público) são gerados temporariamente em disco e excluídos automaticamente após a requisição.
- O certificado original (.pfx) não é modificado.
- A senha é tratada como bytes e nunca exibida em logs.

---

## Licença
Este projeto é de uso livre para fins educacionais e profissionais, desde que respeitadas as políticas de uso da API oficial do Governo do RS.
 



