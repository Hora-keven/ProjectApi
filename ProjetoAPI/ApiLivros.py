import fastapi as f
from fastapi import HTTPException, status
import uvicorn
import LivrosB
from LivrosB import FuncaoBanco, Livros
from Models import  LivroBase, Atualiza_livro

app = f.FastAPI()


@app.get("/livros", response_model=None, status_code=status.HTTP_200_OK)
async def selecionar() -> dict:
    livros = FuncaoBanco.selecionar_tudo(Livros)
    return livros

@app.get("/livros/{id}",status_code=status.HTTP_200_OK)  
def selecionar_livro_id(id) -> dict:
    buscando = FuncaoBanco.selecionar_por_id(id)
    if buscando == "id não encontrado":
        raise HTTPException(status_code=404, detail="Livro não encontrado com esse id")
    
    return buscando


@app.post("/cadastra_livro" ,status_code=status.HTTP_201_CREATED)
def cadastrar_livro(livro:LivroBase) -> dict:
    
    livro_dic = {
        'nome_livro':livro.nome_livro,
        'quantidade_livro':livro.quantidade_capitulos
    }
    
    FuncaoBanco.adicionar_dados_banco(livro)
    return livro_dic


@app.put("/atualiza_livro/{id}", response_model=None, status_code=status.HTTP_201_CREATED)
async def cadastrar_livro(id:int, atualiza:Atualiza_livro) -> dict:
    selecionado = FuncaoBanco.selecionar_por_id(id)
    atualiza.id = id
    FuncaoBanco.atualizar(atualiza)
    
    if selecionado == f"id não encontrado":
        raise HTTPException(status_code=404, detail="Livro não encontrado com esse id")
    return selecionado


@app.delete("/deleta_livro/{id}")
async def deletar_livro(id:int) ->  str:
      deletando = FuncaoBanco.deletar_por_id(id)
      if deletando =="id não encontrado":
            raise HTTPException(status_code=404, detail="Livro não encontrado com esse id") 
      return deletando

if __name__ == '__main__':
    uvicorn.run(app)