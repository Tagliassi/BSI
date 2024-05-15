from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

from datetime import datetime as dt
from datetime import timedelta

# Gerar uma chave privada RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Obtém chave pública
public_key = private_key.public_key()

# Construir o objeto de informações do sujeito
subject = x509.Name([
    # A letra 'u' na frente da string denota uma codificação de string tipo Unicode
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"BR"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Parana"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Curitiba"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Ciberseguranca"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"ciberseguranca.com.br")
])

# Criar um objeto de certificado
# Configura todos os atributos do certificado:
#    Nome do sujeito
#    Nome do emissor (Autoridade de Certificação (CA))
#    Chave pública  
#    Número de série
#    Inválido antes da data corrente
#    Inválido depois de um ano (data corrente + 365 dias)
#    Assinatura realizada com a chave privada, utilizando o algoritmo de hash SHA256 e o backend padrão 
cert = x509.CertificateBuilder() \
    .subject_name(subject) \
    .issuer_name(subject) \
    .public_key(public_key) \
    .serial_number(x509.random_serial_number()) \
    .not_valid_before(dt.utcnow()) \
    .not_valid_after(dt.utcnow() + timedelta(days=365))\
    .sign(private_key, hashes.SHA256(), default_backend())

# Exportar o certificado no formato Privacy Enhanced Mail (PEM)
cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)

# Exportar a chave privada no formato PEM (sem senha)
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Salvar o certificado em um arquivo
with open("cert.pem", "wb") as cert_file:
    cert_file.write(cert_pem)

# Salvar a chave privada em um arquivo
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key_pem)
