---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: "Mi Proyecto de Datos"
footer: "Analista de Datos - 2025"
---

# Esta es la Diapositiva 1
Bienvenido a mi tutorial de Marp.

---

# Diapositiva 2
Aquí podemos poner puntos clave:

* Dominar SQL.
* Aprender Python 3.12.
* Usar FastAPI.

![width:400px](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

---
# Diapositiva con fondo oscuro
Esto solo afecta a esta lámina gracias al guion bajo (`_`).

![bg right:40%](https://via.placeholder.com/400)

# Análisis de Resultados
A la derecha tenemos la gráfica del modelo.
A la izquierda el texto explicativo.

---

@app.get("/")
def read_root():
    return {"Hello": "World"}
