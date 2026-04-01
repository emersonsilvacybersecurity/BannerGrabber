# BannerGrabber
Ferramenta em Python para Service Fingerprinting. Realiza a extração de banners TCP e HTTP para identificação de versões de softwares e serviços de rede.

Ferramenta de reconhecimento ativo desenvolvida para extrair assinaturas (banners) de serviços e identificar versões de software para estudos de segurança e auditoria.

### Python Service Fingerprinting Tool
Este projeto foca na etapa de enumeração e mapeamento de vulnerabilidades, permitindo que o analista identifique a versão exata de serviços como SSH, FTP e Servidores Web. A ferramenta utiliza a biblioteca nativa de sockets do Python para interagir com o alvo e capturar informações de cabeçalho e boas-vindas.

### Funcionalidades
* **Identificação de Versões:** Extração de strings de identificação (banners) de protocolos TCP.
* **Injeção de Payload HTTP:** Suporte automático a requisições HEAD para forçar respostas de banners em servidores web.
* **Robustez de Dados:** Tratamento de decodificação de caracteres para suportar banners de sistemas legados.
* **Gestão de Conexão:** Controle de timeouts para garantir estabilidade em redes externas e serviços silenciosos.


Análise de segurança (Aviso Legal)
Este roteiro foi desenvolvido exclusivamente para fins educacionais e auditorias de segurança autorizadas.
Ética: O uso desta ferramenta contra alvos sem permissão prévia é ilegal.
Responsabilidade: O autor não se responsabiliza por qualquer uso indevido ou danos causados a terceiros.

   

   
