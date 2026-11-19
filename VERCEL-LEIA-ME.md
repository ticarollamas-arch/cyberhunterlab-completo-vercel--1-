# Deploy no Vercel — CyberHunterLab

Envie estes arquivos para a **raiz do repositório** (onde ficam as pastas `apps/` e `docs/`), mantendo as pastas:

```
vercel.json
requirements.txt
.python-version
.vercelignore
api/index.py
apps/api/cyberhunter_api/resume_parser.py   (substitui o atual: lê PDF sem poppler)
```

No Vercel: Add New → Project → importe o repositório → Deploy.
Se o repositório tiver a pasta `cyberhunterlab/` em volta de tudo, defina **Root Directory = cyberhunterlab**.

O que roda no Vercel:
- Site React do Engenheiro Reverso (inclusive /curriculo-ats)
- API Python do funil em /api/health e /api/funnel/*

Variáveis de ambiente: nenhuma é obrigatória para o funil.

Limitação: a análise de APK/ZIP (/api/analyze-architecture) usa o servidor Express e arquivos de até 250 MB. Ela não roda no Vercel (o limite de upload é 4,5 MB) e precisa de uma VPS.
