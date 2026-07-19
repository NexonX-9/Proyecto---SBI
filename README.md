# Sistema de Gestión de Taller Mecánico (SBI)

Esta aplicación es un sistema integral para la gestión de talleres mecánicos, diseñada para optimizar el flujo de trabajo entre clientes y técnicos. Permite registrar reportes de averías, gestionar órdenes de trabajo, controlar el inventario de repuestos y realizar el seguimiento en tiempo real del estado de reparación de vehículos.

## 🛠️ Tecnologías Utilizadas
* **Backend**: Python 3.14
* **Interfaz Web**: Streamlit
* **Base de Datos**: Microsoft SQL Server
* **Conector**: pyodbc (ODBC Driver 17 for SQL Server)
* **Análisis de Datos**: Pandas

## 🚀 Características Principales
* **Rol de Cliente**: Registro de fallas, seguimiento del estado del vehículo (semáforo de reparación) y visualización de recibos de pago.
* **Rol de Técnico**: Asignación de reportes a órdenes de trabajo, gestión de inventario de repuestos, actualización de estados y consulta del historial clínico de los vehículos.
* **Facturación**: Liquidación automática de órdenes de trabajo basada en mano de obra y repuestos utilizados.
* **Telemetría**: Sistema de actualización de estados para comunicación transparente con el cliente.

## 📋 Requisitos Previos
1. **SQL Server**: Instancia local instalada.
2. **ODBC Driver**: Asegúrate de tener instalado el *ODBC Driver 17 for SQL Server*.
3. **Python**: Versión 3.x instalada.

## ⚙️ Instalación
1. Clona el repositorio:
   ```bash
   git clone [tu-url-de-repositorio]