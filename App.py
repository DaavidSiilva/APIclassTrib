import os
import tempfile
import requests
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    pkcs12,
)

class CertificadoA1:
    """Gerencia o certificado digital A1 (.pfx) e gera arquivos temporários PEM para uso em requisições HTTPS."""

    def __init__(self, caminho_arquivo, senha):
        self.caminho_arquivo = caminho_arquivo
        self.senha = senha.encode() if not isinstance(senha, bytes) else senha
        self.arquivo_chave = None
        self.arquivo_cert = None

    def carregar_certificado(self):
        """Carrega o .pfx e separa a chave privada e o certificado público."""
        try:
            with open(self.caminho_arquivo, "rb") as f:
                conteudo = f.read()
        except Exception as e:
            raise Exception(f"Erro ao ler o arquivo .pfx: {e}")

        try:
            chave, cert, _ = pkcs12.load_key_and_certificates(conteudo, self.senha)
        except Exception as e:
            if "invalid password" in str(e).lower():
                raise ValueError("Senha do certificado digital incorreta.")
            raise Exception(f"Erro ao carregar o certificado digital: {e}")

        # Cria arquivos temporários
        self.arquivo_cert = tempfile.NamedTemporaryFile(delete=False, suffix=".pem")
        self.arquivo_chave = tempfile.NamedTemporaryFile(delete=False, suffix=".pem")

        self.arquivo_cert.write(cert.public_bytes(Encoding.PEM))
        self.arquivo_chave.write(
            chave.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
        )

        self.arquivo_cert.close()
        self.arquivo_chave.close()

        return self.arquivo_chave.name, self.arquivo_cert.name

    def excluir_temp(self):
        """Remove os arquivos temporários criados."""
        for arq in [self.arquivo_cert, self.arquivo_chave]:
            if arq and os.path.exists(arq.name):
                os.remove(arq.name)


def fazer_requisicao_com_certificado(url, certificado_path, senha):
    """Exemplo de requisição HTTPS usando certificado A1 (.pfx)."""
    cert_a1 = CertificadoA1(certificado_path, senha)
    chave_path, cert_path = cert_a1.carregar_certificado()

    try:
        response = requests.get(url, cert=(cert_path, chave_path), timeout=30)
        if response.status_code == 200:
            with open("classTrib.json","w", encoding='utf-8') as f:
                f.write(response.text)

            print("Sucesso: Arquivo salvo em classTrib.json")
        else:
            print(f"Falha: Erro ao acessar API, Status: {response.status_code}")
    finally:
        cert_a1.excluir_temp()


if __name__ == "__main__":
    certificado_path = "Certificado/Certificado.pfx"
    senha_certificado = "associacao"

    fazer_requisicao_com_certificado(
        "https://cff.svrs.rs.gov.br/api/v1/consultas/classTrib", 
        certificado_path, 
        senha_certificado
    )
