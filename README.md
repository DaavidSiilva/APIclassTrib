# 🔐 Certificado A1 — Requisições HTTPS Autenticadas com .PFX

Este projeto permite **fazer requisições HTTPS autenticadas** usando um **certificado digital A1 (.pfx)**, como os utilizados por empresas para comunicação segura com APIs governamentais (por exemplo, SEFAZ e CFF).

Ele extrai a chave privada e o certificado público do arquivo `.pfx`, cria **arquivos temporários .pem** e os usa para autenticar uma requisição HTTPS via biblioteca `requests`.

---

## 🚀 Funcionalidades

- Carrega e separa o certificado `.pfx` em **chave privada** e **certificado público**.
- Gera **arquivos temporários** no formato PEM compatíveis com `requests`.
- Faz **requisições HTTPS autenticadas** com esses certificados.
- Remove os arquivos temporários ao final (segurança).
- Salva a resposta em um arquivo `classTrib.json`.

---

## 📦 Requisitos

- Python **3.8+**
- Módulos:
  - `requests`
  - `cryptography`

---

## ⚙️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/certificado-a1.git
cd certificado-a1
