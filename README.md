# Sistema-de-Gerenciamento-Compartilhado-de-Recursos-da-Universidade---SIGCRU

O **SIGCRU** é um sistema desenvolvido para centralizar e organizar o  
uso compartilhado de recursos da universidade, como salas, equipamentos  
e patrimônios diversos. Ele fornece uma plataforma completa para  
registro, controle, auditoria e gestão de atividades realizadas por  
usuários e setores, garantindo transparência, rastreabilidade e  
eficiência nas operações internas.

A proposta principal do sistema é permitir que a universidade tenha: -  
Uma visão clara dos recursos disponíveis - Controle de solicitações e  
reservas - Registro de manutenções e uso dos recursos - Histórico  
detalhado das ações - Gestão centralizada e integrada entre setores

Este projeto utiliza **Django + Django REST Framework**, oferecendo uma  
API moderna e extensível, além de possibilidade de integração com  
sistemas externos ou interfaces frontend.

---
## Visão Geral do Projeto

O SIGCRU foi estruturado para ser modular, claro e escalável. Cada parte  
do sistema representa um aspecto real da gestão universitária, desde  
patrimônios e solicitações até manutenções e histórico de ações.  
Em conjunto, esses módulos compõem uma solução que cobre o ciclo  
completo de uso de um recurso --- desde sua criação, uso, manutenção e  
auditoria.

Os principais pilares do sistema são:

### Gestão de Usuários

Permite controle de acesso, autenticação e identificação dos  
responsáveis por ações no sistema.

### Administração de Patrimônios

Inclui prédios, blocos, salas, localizações e itens patrimoniais. O  
sistema organiza e vincula fisicamente cada recurso.

### Controle de Solicitações

Fluxo completo de criação, aprovação e acompanhamento de pedidos de uso  
dos recursos.

### Gestão de Manutenções

Registra reparos, trocas, inspeções e qualquer manutenção realizada em  
patrimônios.

### Histórico de Atividades

Criado para garantir rastreabilidade total. Cada ação relevante gera um  
registro automático.

O sistema foi projetado para ser simples de utilizar, fácil de expandir  
e flexível para diferentes cenários da instituição.

---

## Tecnologias Utilizadas

- **Python 3**
- **Django**
- **Django REST Framework**
- **SQLite** (padrão, podendo ser substituído por PostgreSQL)
- `.env` para variáveis de ambiente

---
## Rodar o Projeto na Máquina

### **1. Criar ambiente virtual**
```
python -m venv venv
```

### **2. Ativar o ambiente**
Windows:
```
venv\Scripts\activate
```
Linux/Mac:
```
source venv/bin/activate
```

### **3. Instalar dependências**
```
pip install -r requirements.txt
```

### **4. Criar o arquivo `.env`**
```
SECRET_KEY=coloque_uma_chave_aqui
DEBUG=True
ALLOWED_HOSTS=*
```

### **5. Aplicar migrations**
```
python manage.py migrate
```

### **6. Criar superusuário**
```
python manage.py createsuperuser
```

### **7. Executar o servidor**
```
python manage.py runserver
```

Acessar:

- Sistema: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

## Banco de Dados

O projeto utiliza **SQLite** por padrão, o que torna a instalação  
simples e imediata.  
Se quiser migrar para **PostgreSQL**, posso gerar a configuração  
completa.
