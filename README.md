# 🌐 Subdomain Enumerator

🕵️ Ferramenta simples de enumeração de subdomínios feita em Python. Ideal para profissionais de pentest, OSINT e reconhecimento de alvos na web.

## ✨ O que faz?

Essa ferramenta usa uma wordlist e testa diferentes subdomínios no domínio alvo. Se o subdomínio estiver ativo (responder), ele será listado no terminal.

## 🚀 Como usar

```bash
python3 subdomain-enumerator.py
```

- Informe o domínio alvo (exemplo: `example.com`)
- Informe o caminho da wordlist (exemplo: `wordlist.txt`)

## 📂 Exemplo

```bash
Enter target domain: example.com
Enter path to wordlist: wordlist.txt
[+] Found: http://mail.example.com (200)
[+] Found: http://admin.example.com (403)
```

## 🧠 Ideal para:
- Reconhecimento em testes de intrusão
- Coleta de dados em processos de OSINT
- Automação de varreduras manuais

![demo](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2MycTg5cjVyY2dnZTcxdjBqZzNrbWNwZnk1M3hjbTJoNG02cG8zeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/I0e4u216Qhww8eRTVq/giphy.gif)
