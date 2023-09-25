from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import DeclarativeBase

class LivroBase(BaseModel):
   id:Optional[int]=None
   nome_livro:str
   quantidade_capitulos: int
   ...

class Atualiza_livro(BaseModel):
    id:Optional[int]=None
    nome_livro: Optional[str] = None
    quantidade_capitulos: Optional[int] = None

class Base(DeclarativeBase):
  ...

