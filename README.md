# Monitoramento de Rede com Ping

Este projeto realiza o monitoramento de hosts na rede usando comandos de ping. Ele verifica se os hosts estão online e fornece informações sobre o tempo de resposta (latência).

## Como usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git


Projeto de Monitoramento de Ping
Este projeto é um script simples de monitoramento de ping que verifica a conectividade de uma lista de hosts e exibe os resultados do ping de cada um deles.

Descrição
O script realiza o ping de múltiplos hosts e exibe o tempo de resposta ou a perda de pacotes para cada um deles. Ele foi desenvolvido em Python e pode ser utilizado para monitorar rapidamente a conectividade de hosts ou dispositivos em uma rede.

Como usar
Pré-requisitos
Python 3.x instalado em seu sistema. Você pode baixá-lo aqui.
Configuração
Clone este repositório para a sua máquina local:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd nome-do-repositorio
Abra o arquivo monitoramento_ping.py e edite a lista de hosts com os IPs ou domínios que deseja monitorar:

python
Copiar código
hosts = ["8.8.8.8", "192.168.0.1", "www.google.com"]
Salve o arquivo após a edição.

Executando o Script
Para executar o script, use o seguinte comando no terminal:

bash
Copiar código
python monitoramento_ping.py
O script irá exibir o status de conectividade de cada host da lista.

Exemplo de saída
bash
Copiar código
Disparando 8.8.8.8 com 32 bytes de dados:
Resposta de 8.8.8.8: bytes=32 tempo=30ms TTL=114

Disparando 192.168.0.1 com 32 bytes de dados:
Resposta de 192.168.0.1: bytes=32 tempo=1ms TTL=64

Disparando www.google.com com 32 bytes de dados:
Resposta de www.google.com: bytes=32 tempo=48ms TTL=54
Contribuições
Contribuições são bem-vindas! Se você tiver ideias para melhorias ou encontrar problemas, sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.