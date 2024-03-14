from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Criando a engine e a sessão
engine = create_engine('sqlite:///banco_relacional.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Definindo a base
Base = declarative_base()

# Definindo as classes Cliente e Conta
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))

    cliente = relationship("Cliente", back_populates="contas")

# Criando as tabelas no banco de dados relacional
Base.metadata.create_all(engine)

# Inserindo dados de exemplo
cliente1 = Cliente(nome='João')
cliente2 = Cliente(nome='Maria')

conta1 = Conta(saldo=1000, cliente=cliente1)
conta2 = Conta(saldo=500, cliente=cliente2)

session.add_all([cliente1, cliente2, conta1, conta2])
session.commit()

# Recuperando dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'Cliente: {cliente.nome}')
    for conta in cliente.contas:
        print(f'Conta ID: {conta.id}, Saldo: {conta.saldo}')


