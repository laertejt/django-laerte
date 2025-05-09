from ninja import Router, Schema
from typing import List, Optional

class AlunoOut(Schema):
    id: int
    nome_aluno: str
    email: Optional[str]