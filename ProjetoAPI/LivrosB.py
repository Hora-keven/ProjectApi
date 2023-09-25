from sqlalchemy import Integer, String, create_engine, update, delete, select
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from Models import Base, LivroBase
import json
import requests
from sqlalchemy.dialects.sqlite import insert


engine = create_engine("sqlite:///Livros.db", echo=True)
cursor = engine.connect()

class Livros(Base):
    __tablename__ = 'Livros'
    id:Mapped[int] = mapped_column(primary_key=True, nullable=True)
    nome_livro:Mapped[str]=mapped_column(String(100))
    quantidade_livro:Mapped[int]=mapped_column(Integer)
    
    
class FuncaoBanco:
    @staticmethod
    def adicionar_dados_banco(livro:Livros) -> None:
        cursor.execute(insert(Livros),[
          { 'id':livro.id, 'nome_livro':livro.nome_livro, 'quantidade_livro':livro.quantidade_livro}
        ])
        cursor.commit()
      
    @staticmethod
    def selecionar_tudo(livro:Livros)->list:
        selecionando = cursor.execute(select(Livros), [{'nome_livro':livro.nome_livro}])
        livroZip = []
        coluna = ['Id', 'nome_livro', 'quantidade_capitulos']
       
        for linha in selecionando:
            livroZip.append(dict(zip(coluna, linha)))
         
        return livroZip

    @staticmethod
    def selecionar_por_id(id:int)->dict or str:
        dados = cursor.execute(select(Livros).filter(Livros.id == id)).all()
        print(dados)

        if dados == []:
        
           return f"id não encontrado"
        
        dados ={
                "id":dados[0][0],
                "nome_livro":dados[0][1], 
                "quantidade_livro":dados[0][2]
                }
        
        return dados
    
    @staticmethod
    def atualizar(livro:LivroBase)->str:
        livros = cursor.execute(select(Livros), [{'nome_livro':Livros.nome_livro}]).fetchall()
        mensagem = True

        for i, l in enumerate(livros):
            if livro.id not in l:
              mensagem = False
          
        if mensagem:
            return f"{livro.id}"
       
        dados_atualizando = cursor.execute(update(Livros).where(Livros.id == livro.id),
                [{"nome_livro": livro.nome_livro, "quantidade_livro":livro.quantidade_livro},
        ])
    
        cursor.commit()

        
        return f'{dados_atualizando}'
    
    @staticmethod
    def deletar_por_id(id:int) -> str:
        livros = cursor.execute(select(Livros), [{'nome_livro':Livros.nome_livro}]).fetchall()
        print(livros)
        mensagem = True
        for i, l in enumerate(livros):
            if id not in l:
                mensagem = False

        if mensagem:
           return "id não encontrado"
        
        cursor.execute(delete(Livros).where(Livros.id == id))
        cursor.commit()
        
        return f"id: {id} deletado com sucesso!"


    def buscarDados(livros:list, capitulos:list):
      request = requests.get("https://www.abibliadigital.com.br/api/books")
      j = json.loads(request.content)
      
      for i in range(66):
        livros.append(j[i]['name'])
        capitulos.append(j[i]['chapters'])

      return livros, capitulos
    
Base.metadata.create_all(engine) 






