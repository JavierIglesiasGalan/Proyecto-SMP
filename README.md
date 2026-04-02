# 🚀 Server Monitoring Platform (SMP)

Plataforma de monitorización de servidores desarrollada en Python que permite visualizar en tiempo real el uso de recursos (CPU, RAM y disco) mediante un sistema distribuido basado en agentes.

---

## 📌 Características

* 📡 Monitorización en tiempo real (CPU, RAM, disco)
* 🖥️ Gestión de múltiples servidores
* 📊 Dashboard interactivo con gráficas
* 🔄 Actualización automática cada 5 segundos
* 🚨 Alertas visuales por alto consumo de recursos
* 🐳 Proyecto completamente dockerizado
* 🤖 Agente ligero para monitorización remota

---

## 🏗️ Arquitectura

```
                ┌───────────────┐
                │   Agente      │
                │ (psutil)      │
                └──────┬────────┘
                       │ HTTP
                       ▼
              ┌──────────────────┐
              │   API FastAPI    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PostgreSQL     │
              └──────────────────┘

                       ▲
                       │ HTTP
              ┌────────┴─────────┐
              │   Frontend       │
              │ (Chart.js + JS)  │
              └──────────────────┘
```

---

## ⚙️ Tecnologías utilizadas

### Backend

* Python
* FastAPI
* SQLAlchemy

### Base de datos

* PostgreSQL

### Frontend

* HTML + JavaScript
* Chart.js

### DevOps

* Docker
* Docker Compose

### Agente

* Python
* psutil
* requests

---

## 🚀 Puesta en marcha

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/server-monitoring-platform.git
cd server-monitoring-platform
```

---

### 2️⃣ Levantar el proyecto con Docker

```bash
docker-compose up --build
```

---

### 3️⃣ Acceder a los servicios

* 🌐 Frontend → http://localhost:3000
* 📡 API → http://localhost:8000/docs

---

## 🖥️ Cómo usar el sistema

### 1. Crear un servidor

Accede a:

```
http://localhost:8000/docs
```

Usa el endpoint:

```
POST /servers
```

Ejemplo:

```json
{
  "name": "Servidor 1",
  "ip": "192.168.1.1"
}
```

---

### 2. Ejecutar el agente

Ir a la carpeta `agent/`:

```bash
cd agent
pip install -r requirements.txt
python3 agent.py
```

⚠️ Configurar previamente `config.py`:

```python
API_URL = "http://localhost:8000/metrics"
SERVER_ID = 1
```

---

### 3. Acceder al dashboard

```
http://localhost:3000
```

Verás:

* Selector de servidores
* Gráficas en tiempo real
* Alertas automáticas

---

## 📊 Funcionalidades del dashboard

* Actualización automática cada 5 segundos
* Visualización de CPU, RAM y disco
* Cambio dinámico entre servidores
* Sistema de alertas:

  * CPU > 80%
  * RAM > 80%
  * Disco > 90%

---

## 🤖 Agente de monitorización

El agente recoge métricas del sistema mediante `psutil` y las envía a la API.

### Métricas recogidas:

* Uso de CPU
* Uso de memoria RAM
* Uso de disco

---

## 🐳 Servicios Docker

* `backend` → API FastAPI
* `db` → PostgreSQL
* `frontend` → Servidor Nginx

---

## ⚠️ Problemas comunes

### Error CORS

Asegúrate de tener CORS habilitado en FastAPI.

### No aparecen datos

* Verifica que el agente está ejecutándose
* Comprueba que el servidor existe en la base de datos

### Cambios en frontend no se reflejan

Reconstruye el contenedor:

```bash
docker-compose build frontend
```

---

## 👨‍💻 Autor

Javier Iglesias

---

## ⭐ Sobre el proyecto

Este proyecto demuestra:

* Desarrollo de APIs con Python
* Monitorización de sistemas
* Arquitectura distribuida
* Uso de Docker y DevOps
* Integración frontend-backend

---
