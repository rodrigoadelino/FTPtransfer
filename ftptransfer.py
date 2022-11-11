import ftplib


# Variaveis
servidor = 'seuftpazure' # Informar o endereço do FTP Azure
usuario = 'seuusuario' # Informar usuario de acesso ao FTP
senha = 'suasenha'# Informar a Senha de acesso ao FTP
arquivolocal = 'C:\\temp\\teste.txt' # Local do Arquivo a ser enviado
remotefile='/in/pastaftp/teste.txt' # Local no FTP onde o arquivo será copiado o nome do arquivo é "teste.txt" 
#mas se colocar outro nome o arquivo sera criado no ftp com o nome escolhido

# Conexão
ftp = ftplib.FTP_TLS(servidor, timeout=10) # passando a variavel de conexao com o servidor e um timeout de 10 segundos
ftp.login(usuario, senha) # passando as variaveis de usuario e senha
ftp.prot_p() # Informando qual tipo de protocolo será usado
ftp.debugging = 1 #0-não produz saída de depuração, 1-quantidade moderada 2- ou superior produz a quantidade máxima de saída de depuração, 

# Ler o arquivo e envia para o FTP
with open(arquivolocal, "rb") as file:
    ftp.storbinary(f'STOR {remotefile}', file)
ftp.close()

# IMPORTANTE:
# Para o método que está falhando, no caso STORBINARY, 
# o erro parece estar na linha onde diz conn.unwrap()nesse método. 
# Comente esta linha. Digite a palavra-chave pass

# Links:
# https://docs.python.org/3/library/ftplib.html # Documentacao da Biblioteca utilizada
# https://stackoverflow.com/questions/31851998/ftplib-file-creation-very-slow-sslerror-the-read-operation-timed-out # Problema do STORBINARY