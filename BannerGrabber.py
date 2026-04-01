import socket
import sys

def banner_grab(ip, port):
    """Tenta conectar e extrair a assinatura (banner) do serviço."""
    try:
        # Criamos o socket com um timeout curto para não travar
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3.0)
            s.connect((ip, port))
            
            # Se for porta 80, precisamos enviar um request HTTP para receber o banner
            if port == 80:
                s.send(b"HEAD / HTTP/1.1\r\nHost: google.com\r\n\r\n")
            
            # Recebe a resposta do servidor
            banner = s.recv(1024)
            return banner.decode(errors='ignore').strip()
    except socket.timeout:
        return "Erro: Tempo de resposta esgotado (Timeout)."
    except ConnectionRefusedError:
        return "Erro: Conexão recusada pela porta."
    except Exception as e:
        return f"Erro: {e}"

# --- Interface Simples ---
if __name__ == "__main__":
    print("-" * 40)
    print("🎯 BANNER GRABBER V1.0")
    print("-" * 40)
    
    alvo = input("Digite o IP do alvo: ")
    porta = int(input("Digite a porta para análise (ex: 21, 22, 80): "))
    
    print(f"[*] Analisando {alvo}:{porta}...")
    resultado = banner_grab(alvo, porta)
    
    print(f"\n[+] Resultado do Banner:")
    print(f"{resultado}")
    print("-" * 40)