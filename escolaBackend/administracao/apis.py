from ninja import Router
from administracao.models import TbAlunos
from typing import List


router = Router()

@router.get("/alunos", response=List[dict])
def pegar_alunos(request):
    return TbAlunos.objects.all().values()