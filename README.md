## 🎯 Readme
# 🛒 Tienda Online Django - Proyecto Final

![Django](https://img.shields.io/badge/Django-4.2.26-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

Una aplicación completa de e-commerce desarrollada en Django, con funcionalidades de autenticación de usuarios, carrito de compras, gestión de pedidos y catálogo de productos.

## ✨ Características Principales

- **🔐 Autenticación de Usuarios**: Registro, login y perfiles personalizados
- **🛍️ Catálogo de Productos**: Categorías, productos con imágenes y búsqueda
- **🛒 Carrito de Compras**: Gestión dinámica del carrito con sesiones
- **📦 Sistema de Pedidos**: Creación y seguimiento de pedidos
- **👤 Perfiles de Usuario**: Información personal y foto de perfil
- **🔍 Búsqueda de Productos**: Filtrado por categoría y nombre
- **📱 Diseño Responsive**: Compatible con diferentes dispositivos

## 🏗️ Arquitectura del Proyecto
proyectofinal/

├── account/ # Gestión de usuarios y perfiles

├── cart/ # Carrito de compras

├── orders/ # Sistema de pedidos

├── shop/ # Catálogo de productos

└── proyectofinal/ # Configuración del proyecto

## 🖥️​ Crear entorno virtual
1️⃣ **Instalar virtualenv si no está instalado**

pip install virtualenv

2️⃣ **Crear entorno virtual llamado 'venv'**

virtualenv venv

3️⃣ **Activar el entorno virtual**

.\venv\Scripts\activate

4️⃣ **Instalar Django**

pip install django

5️⃣ **Ejecutar servidor**

python manage.py runserver

## Acceder a la aplicación

- 🌐 **Tienda Online**: http://localhost:8000

- ⚙️**Admin**: http://localhost:8000/admin

## 📁 Estructura de Aplicaciones
👥 account - Gestión de Usuarios

📝 Registro y autenticación

📸 Perfiles con foto y fecha de nacimiento

✏️ Edición de datos personales

🛒 cart - Carrito de Compras

💾 Gestión de sesiones de carrito

➕➖ Añadir/eliminar productos

🔄 Actualizar cantidades

🧮 Calcular totales

📦 orders - Sistema de Pedidos

📝 Creación de pedidos

📋 Historial de pedidos por usuario

🔍 Detalles de pedido

🔗 Integración con carrito

🛍️ shop - Catálogo de Productos

🏷️ Categorías y productos

🔍 Búsqueda y filtrado

🖼️ Imágenes de productos

🔗 URLs

## 🗑️ Borrar base de datos y comenzar de nuevo
rm db.sqlite3

python manage.py migrate

## 🔒 Credenciales de Prueba
👤 Usuario normal:

Usuario: manuel_portilla

Contraseña: manu1234

👑 Administrador:

Usuario: admin

Contraseña: admin123

(Estos usuarios pueden ser creados desde el panel admin)

## 🔄 Flujo de Compra:
👤 Usuario → 🔎 Ver Productos → ➕ Añadir al Carrito → 
📋 Revisar Carrito → 📝 Crear Pedido → ✅ Confirmación

## 🔗 Relaciones de Base de Datos:
👤 User (1) → (1) 📄 Profile

👤 User (1) → (*) 📦 Order

📦 Order (1) → (*) 📋 OrderItem

🛍️ Product (1) → (*) 📋 OrderItem

🏷️ Category (1) → (*) 🛍️ Product

## 📊 ​Diagramas
- **Diagrama de casos de uso**:
<img width="11553" height="917" alt="Diagrama de casos de uso" src="https://github.com/user-attachments/assets/8225020f-9d66-4934-b4b6-4df6de156e19" />

- **Diagrama de clases**:
<img width="3383" height="3607" alt="Diagrama de clases" src="https://github.com/user-attachments/assets/e427564e-5c44-4e10-8356-8f0c731ef615" />

- **Diagrama de secuencia**:
<img width="3702" height="5964" alt="Diagrama de secuencias" src="https://github.com/user-attachments/assets/a41e5774-48d0-4aa0-8e38-3d870f13f2bf" />
