# Monitoramento de Rede com Ping

Este projeto realiza o monitoramento de hosts na rede usando comandos de ping. Ele verifica se os hosts estão online e fornece informações sobre o tempo de resposta (latência).

## Como usar

1. Certifique-se de ter o Python instalado em seu sistema. Caso não tenha, você pode baixar em: https://www.python.org/downloads/
2. Clonar ou fazer o download deste repositório:
    ```bash
    git clone https://github.com/Brenassilva/monitoramento-solarwinds.git
    ```
3. Navegar até a pasta onde você clonou o repositório e editar a lista de `hosts` no arquivo `monitoramento_ping.py` com os endereços IP ou domínios que você deseja monitorar.

    ```python
    hosts = ["8.8.8.8", "192.168.0.1", "www.google.com"]
    ```

4. Execute o script para monitorar os hosts:
    ```bash
    python monitoramento_ping.py
    ```

## Projeto de Monitoramento de Ping

Este projeto é um script simples de monitoramento de ping que verifica a conectividade de uma lista de hosts e exibe os resultados do ping de cada um deles.

### Descrição
O script realiza o ping de vários hosts e exibe o tempo de resposta ou a perda de pacotes para cada um deles. Ele foi desenvolvido em Python e pode ser utilizado para monitorar rapidamente a conectividade de hosts ou dispositivos em uma rede.

### Como usar

**Pré-requisitos**
- Python 3.x instalado em seu sistema.

### Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
