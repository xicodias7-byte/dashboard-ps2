# 📊 Dashboard PS2 – Laboratórios de Informática

## 👥 Autores
- Francisco Dias
- Tomas Pipo

Objetivo
Este projeto implementa um sistema em Python capaz de:
✔️ Ler ficheiros PS2 (Débitos Diretos)  
✔️ Validar a estrutura e integridade dos ficheiros  
✔️ Processar e analisar os valores  
✔️ Apresentar resultados num **Dashboard Web interativo**

---

Tecnologias
- Python 3
- Shiny para Python
- pandas
- matplotlib
- Git + GitHub

---

Demonstração do Dashboard

Estatísticas Gerais
![Dashboard](report/dashboard-home.png)

Tabela de Operações
![Tabela](report/dashboard-table.png)

Gráfico Total por Cliente
![Gráfico](report/dashboard-graph.png)

---

📂 Estrutura

dashboard-ps2
├── app
│ ├── parser.py
│ ├── analyzer.py
│ ├── dashboard.py
│ └── init.py
├── data
├── report
│ ├── dashboard-home.png
│ ├── dashboard-table.png
│ ├── dashboard-graph.png
│ └── report.pdf
├── requirements.txt
└── README.md


---

Como Executar

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
shiny run --reload app/dashboard.py 

Abrir:
👉 http://127.0.0.1:8000

---

✅ Conclusão
Projeto totalmente funcional, validado e documentado.
