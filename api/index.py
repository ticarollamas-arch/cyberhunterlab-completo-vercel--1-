"""Função Python do Vercel: expõe a API do funil (apps/api) em /api/*."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "apps" / "api"))

from cyberhunter_api.server import app  # noqa: E402,F401  (ASGI detectado pelo Vercel)
