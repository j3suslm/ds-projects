---
marp: true
theme: uncover
class: invert
paginate: true
header: "Data Science Project | 2025"
footer: "Jesus LM"
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }
  h1 {
    color: #00ffcc;
  }
  code {
    background: #28282b;
    color: #abb2bf;
  }
  blockquote {
    background: #1e1e1e;
    border-left: 10px solid #00ffcc;
    font-style: italic;
  }
---

# 🚀 Predicción de Modelos con FastAPI

### Flujo de Trabajo Moderno en Python 3.12

---

## 📊 Resumen del Pipeline

1. **Extracción:** SQL & Mamba
2. **Modelo:** XGBoost & Scikit-Learn
3. **API:** FastAPI
4. **Deploy:** Docker

---

## 💻 Implementación del Modelo

```python
# Usando Python 3.12 Type Hinting
def get_prediction(data: dict) -> float:
    score = model.predict(data)
    return score
