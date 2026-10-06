# TP_Teo_Compiladores

## Estructura
StoreLang/
├── StoreLang.g4          
├── semantic.py          
├── main.py                
├── requirements.txt       
├── README.md               
├── ejemplos/
│   ├── valido1.store
│   ├── error_sintactico.store
│   ├── error_lexico.store
│   └── error_semantico.store
├── StoreLangLexer.py      
├── StoreLangParser.py         
├── StoreLangVisitor.py
└── TP_Teo_Compiladores.ipynb

## Instalar
pip install antlr4-python3-runtime==4.13.2

## Terminal Run
python main.py ejemplos/valido1.store
python main.py ejemplos/error_sintactico.store
python main.py ejemplos/error_semantico.store
python main.py ejemplos/error_lexico.store
