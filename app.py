import streamlit as st
import pyodbc
import pandas as pd
import bcrypt

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA (Estética Sobria)
# ==========================================
st.set_page_config(
    page_title="Sistema de Gestión de Averías",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar el estado de la sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.rol = None
    st.session_state.usuario = None

# ==========================================
# 2. CONEXIÓN A LA BASE DE DATOS (Autenticación Windows)
# ==========================================
def iniciar_conexion():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=proyecto_db;'
            'Trusted_Connection=yes;' 
        )
        return conn
    except Exception as e:
        st.error(f"Error de conexión a la Base de Datos: {e}")
        return None

# ==========================================
# 3. FUNCIONES DE BASE DE DATOS (QUERIES)
# ==========================================
def obtener_reportes_pendientes():
    conn = iniciar_conexion()
    if conn:
        try:
            # Trae los reportes que NO tienen una orden de trabajo (O.ID_Reporte IS NULL)
            query = """
                SELECT 
                    R.ID_Reporte, 
                    C.Nombre AS Cliente, 
                    R.Fecha AS Fecha_Reporte,
                    R.Observaciones AS [Detalle y Vehículo]
                FROM T_tReporte_Averia R
                INNER JOIN T_tCliente C ON R.IdCliente = C.IdCliente
                LEFT JOIN T_tOrden_Trabajo O ON R.ID_Reporte = O.ID_Reporte
                WHERE O.ID_Reporte IS NULL
            """
            return pd.read_sql(query, conn)
        except Exception as e:
            st.error(f"Error al cargar reportes: {e}")
    return pd.DataFrame()

def obtener_mis_ordenes(id_tecnico):
    conn = iniciar_conexion()
    if conn:
        try:
            query = """
                SELECT 
                    O.ID_Orden AS [N° Orden],
                    R.ID_Reporte AS [N° Reporte],
                    C.Nombre AS Cliente,
                    ISNULL(R.Estado_Servicio, 'En Espera') AS [Estado],
                    O.Diagnostico
                FROM T_tOrden_Trabajo O
                INNER JOIN T_tReporte_Averia R ON O.ID_Reporte = R.ID_Reporte
                INNER JOIN T_tCliente C ON R.IdCliente = C.IdCliente
                WHERE O.T_tTecnico_ID = ?
            """
            return pd.read_sql(query, conn, params=(id_tecnico,))
        except Exception as e:
            st.error(f"Error al cargar órdenes: {e}")
    return pd.DataFrame()

# Actualizamos esta función para que reciba el id_tecnico y lo guarde en la BD
def insertar_orden(id_orden, id_reporte, id_tecnico, diagnostico, solucion):
    conn = iniciar_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO T_tOrden_Trabajo 
                (ID_Orden, ID_Reporte, Diagnostico, Solucion_Aplicada, T_tReporte_Averia_ID_Reporte, 
                 ID_Cuadrilla, T_tCuadrilla_ID_Cuadrilla, T_tTecnico_ID, T_tTecnico_T_tTecnico_ID, 
                 ID_Vehiculo, T_tVehiculo_ID_Vehiculo, ID_est_Orden, T_tEstado_Orden_ID_est_Orden,
                 Fecha, Hora_Salida, Hora_Llegada, Hora_Solucion, FechaSolucion) 
                VALUES (?, ?, ?, ?, ?, 1, 1, ?, ?, 1, 1, 1, 1, GETDATE(), GETDATE(), GETDATE(), GETDATE(), GETDATE())
            """
            # Pasamos el id_tecnico a los parámetros de la consulta
            cursor.execute(query, (id_orden, id_reporte, diagnostico, solucion, id_reporte, id_tecnico, id_tecnico))
            conn.commit()
            return True
        except Exception as e:
            st.error(f"Error al ejecutar INSERT: {e}")
            return False

def obtener_reportes_cliente(id_cliente):
    conn = iniciar_conexion()
    if conn:
        try:
            query = """
                SELECT 
                    ID_Reporte AS [N° Reporte], 
                    Fecha, 
                    Observaciones AS [Vehículo y Falla], 
                    ISNULL(Estado_Servicio, 'En Espera') AS [Estado Actual]
                FROM T_tReporte_Averia 
                WHERE IdCliente = ?
            """
            return pd.read_sql(query, conn, params=(id_cliente,))
        except Exception as e:
            st.error(f"Error al obtener los reportes: {e}")
    return pd.DataFrame()

def insertar_reporte_cliente(id_cliente, placa, modelo, tipo, falla):
    conn = iniciar_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT ID_Vehiculo FROM T_tVehiculo WHERE Placa = ?", (placa,))
            vehiculo = cursor.fetchone()
            if not vehiculo:
                query_vehiculo = """
                    INSERT INTO T_tVehiculo (ID_Vehiculo, Placa, Modelo, Tipo) 
                    VALUES ((SELECT ISNULL(MAX(ID_Vehiculo), 0) + 1 FROM T_tVehiculo), ?, ?, ?)
                """
                cursor.execute(query_vehiculo, (placa, modelo, tipo))
                
            observacion_completa = f"VEHÍCULO: {modelo} | PLACA: {placa} | TIPO: {tipo} || FALLA: {falla}"
            query_reporte = """
                INSERT INTO T_tReporte_Averia 
                (ID_Reporte, Fecha, Hora, Observaciones, IdCliente, T_tCliente_IdCliente, 
                 ID_Suministro, T_tSuministro_T_tCliente_IdCliente, T_tSuministro_IdCliente, T_tSuministro_ID_Suministro,
                 ID_Canal, T_tCanal_Reporte_ID_Canal, ID_Tipo, T_tTipo_Averia_ID_Tipo, 
                 ID_prioridad, T_tPrioridad_ID_prioridad, ID_Estado, T_tEstado_Reporte_ID_Estado)
                VALUES (
                    (SELECT ISNULL(MAX(ID_Reporte), 0) + 1 FROM T_tReporte_Averia),
                    CAST(GETDATE() AS DATE), CAST(GETDATE() AS TIME), ?, ?, ?,
                    1, ?, ?, 1,
                    1, 1, 1, 1,
                    1, 1, 1, 1
                )
            """
            cursor.execute(query_reporte, (observacion_completa, id_cliente, id_cliente, id_cliente, id_cliente))
            conn.commit()
            return True
        except Exception as e:
            st.error(f"Error al enviar reporte: {e}")
            return False

def obtener_catalogo_materiales():
    conn = iniciar_conexion()
    if conn:
        try:
            query = "SELECT ID_Material, Nombre FROM T_tMaterial"
            return pd.read_sql(query, conn)
        except Exception as e:
            st.error(f"Error al cargar el catálogo de materiales: {e}")
    return pd.DataFrame()

def agregar_material_orden(id_orden, id_material, cantidad):
    conn = iniciar_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            # Guardamos en tu tabla T_tDetalle_Material
            query = """
                INSERT INTO T_tDetalle_Material (ID_Orden, ID_Material, Cantidad) 
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (id_orden, id_material, cantidad))
            conn.commit()
            return True
        except pyodbc.IntegrityError:
            st.error("Error: Esa Orden de Trabajo no existe o el material ya fue agregado.")
            return False
        except Exception as e:
            st.error(f"Error al asignar repuesto: {e}")
            return False
        
def actualizar_estado_reporte(id_reporte, nuevo_estado):
    conn = iniciar_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE T_tReporte_Averia SET Estado_Servicio = ? WHERE ID_Reporte = ?", (nuevo_estado, id_reporte))
            conn.commit()
            return True
        except Exception as e:
            st.error(f"Error al actualizar estado: {e}")
            return False
        
def obtener_historial_vehiculo(placa):
    conn = iniciar_conexion()
    if conn:
        try:
            # Buscamos todas las órdenes previas asociadas a la placa
            query = """
                SELECT 
                    O.ID_Orden AS [N° Orden],
                    R.Fecha AS [Fecha Servicio],
                    R.Observaciones AS [Falla Original],
                    O.Diagnostico,
                    O.Solucion_Aplicada
                FROM T_tOrden_Trabajo O
                INNER JOIN T_tReporte_Averia R ON O.ID_Reporte = R.ID_Reporte
                INNER JOIN T_tVehiculo V ON O.ID_Vehiculo = V.ID_Vehiculo
                WHERE V.Placa = ?
                ORDER BY R.Fecha DESC
            """
            return pd.read_sql(query, conn, params=(placa,))
        except Exception as e:
            st.error(f"Error al cargar historial: {e}")
    return pd.DataFrame()

def obtener_repuestos_orden(id_orden):
    conn = iniciar_conexion()
    if conn:
        try:
            # Trae los repuestos, su cantidad, el precio unitario y calcula el subtotal
            query = """
                SELECT 
                    M.Nombre AS Repuesto, 
                    D.Cantidad, 
                    M.Precio AS [Precio Unit. (S/)], 
                    (D.Cantidad * M.Precio) AS [Subtotal (S/)]
                FROM T_tDetalle_Material D
                INNER JOIN T_tMaterial M ON D.ID_Material = M.ID_Material
                WHERE D.ID_Orden = ?
            """
            return pd.read_sql(query, conn, params=(id_orden,))
        except Exception as e:
            pass
    return pd.DataFrame()

def cerrar_orden_facturacion(id_orden, costo_mano_obra):
    conn = iniciar_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            # 1. Calculamos cuánto suman todos los repuestos usados en esta orden
            cursor.execute("""
                SELECT ISNULL(SUM(D.Cantidad * M.Precio), 0)
                FROM T_tDetalle_Material D
                INNER JOIN T_tMaterial M ON D.ID_Material = M.ID_Material
                WHERE D.ID_Orden = ?
            """, (id_orden,))
            total_repuestos = cursor.fetchone()[0]
            
            # 2. Calculamos el Gran Total
            gran_total = float(total_repuestos) + float(costo_mano_obra)
            
            # 3. Actualizamos la orden
            query_update = """
                UPDATE T_tOrden_Trabajo 
                SET Costo_Mano_Obra = ?, Costo_Total = ?, FechaSolucion = GETDATE()
                WHERE ID_Orden = ?
            """
            cursor.execute(query_update, (costo_mano_obra, gran_total, id_orden))
            conn.commit()
            return gran_total
        except Exception as e:
            st.error(f"Error en facturación: {e}")
            return None

def obtener_recibos_cliente(id_cliente):
    conn = iniciar_conexion()
    if conn:
        try:
            query = """
                SELECT 
                    O.ID_Orden AS [N° Orden],
                    V.Placa,
                    V.Modelo,
                    R.Fecha AS [Fecha de Ingreso],
                    O.FechaSolucion AS [Fecha de Salida],
                    O.Diagnostico,
                    O.Costo_Mano_Obra AS [Mano de Obra (S/)],
                    (O.Costo_Total - O.Costo_Mano_Obra) AS [Costo Repuestos (S/)],
                    O.Costo_Total AS [TOTAL A PAGAR (S/)]
                FROM T_tOrden_Trabajo O
                INNER JOIN T_tReporte_Averia R ON O.ID_Reporte = R.ID_Reporte
                INNER JOIN T_tVehiculo V ON O.ID_Vehiculo = V.ID_Vehiculo
                WHERE R.IdCliente = ? AND O.Costo_Total > 0
            """
            return pd.read_sql(query, conn, params=(id_cliente,))
        except Exception as e:
            st.error(f"Error al cargar recibos: {e}")
    return pd.DataFrame()

# ==========================================
# 4. MÓDULO DE AUTENTICACIÓN Y REGISTRO (DIRECTO A T_tCliente)
# ==========================================
def mostrar_login():
    st.title("Sistema de Gestión de Averías")
    st.markdown("---")
    
    tab_login, tab_registro = st.tabs(["🔒 Iniciar Sesión", "📝 Registrarse"])
    
    # --- PESTAÑA: INICIAR SESIÓN ---
    with tab_login:
        with st.container():
            st.subheader("Acceso a tu cuenta")
            
            rol_login = st.radio("Selecciona tu perfil de ingreso:", ["Cliente", "Técnico"], horizontal=True)
            usuario_login = st.text_input("DNI (Cliente) o Código (Técnico)", key="login_user")
            password_login = st.text_input("Contraseña", type="password", key="login_pass")
            
            if st.button("Ingresar", use_container_width=True):
                if not usuario_login or not password_login:
                    st.warning("Por favor, ingresa tus credenciales.")
                else:
                    conn = iniciar_conexion()
                    if conn:
                        try:
                            cursor = conn.cursor()
                            
                            # Validar según la tabla correspondiente
                            if rol_login == "Cliente":
                                query = "SELECT PasswordHash, Nombre, IdCliente FROM T_tCliente WHERE DNI = ?"
                            else:
                                query = "SELECT PasswordHash, Nombre, T_tTecnico_ID FROM T_tTecnico WHERE Codigo = ?"
                                
                            cursor.execute(query, (usuario_login,))
                            row = cursor.fetchone()
                            
                            if row:
                                if row[0] is None:
                                    st.error("Esta cuenta no tiene contraseña configurada.")
                                else:
                                    hash_guardado = row[0].encode('utf-8')
                                    if bcrypt.checkpw(password_login.encode('utf-8'), hash_guardado):
                                        st.session_state.autenticado = True
                                        st.session_state.rol = "Cliente" if rol_login == "Cliente" else "Mecanico"
                                        # Se guarda el ID real (IdCliente o T_tTecnico_ID) para hacer las consultas
                                        st.session_state.usuario = row[2] 
                                        st.rerun()
                                    else:
                                        st.error("Contraseña incorrecta.")
                            else:
                                st.error("El usuario no existe en la base de datos.")
                        except Exception as e:
                            st.error(f"Error de consulta: {e}")

# --- PESTAÑA: REGISTRO ---
    with tab_registro:
        st.subheader("Registrar nueva cuenta")
        with st.form("formulario_registro"):
            
            rol_registro = st.selectbox("Perfil", ["Cliente", "Técnico"]) 
            
            if rol_registro == "Cliente":
                identificador_input = st.text_input("Número de DNI (Será tu usuario de acceso)")
            else:
                identificador_input = st.text_input("Código de Técnico (Será tu usuario de acceso)")
                
            nombre_input = st.text_input("Nombre Completo")
            telefono_input = st.text_input("Teléfono de contacto")
            
            # Campos exclusivos si elige ser Técnico
            if rol_registro == "Técnico":
                cargo_input = st.text_input("Cargo (Ej. Mecánico Junior)")
                especialidad_input = st.text_input("Especialidad (Ej. Electricidad)")
            
            nueva_password = st.text_input("Crea una contraseña", type="password")
            confirmar_password = st.text_input("Confirma tu contraseña", type="password")
            
            btn_registrar = st.form_submit_button("Registrarme", use_container_width=True)
            
            if btn_registrar:
                if nueva_password != confirmar_password:
                    st.error("Las contraseñas no coinciden.")
                elif len(nueva_password) < 6:
                    st.warning("La contraseña debe tener al menos 6 caracteres.")
                elif not identificador_input or not nombre_input or not telefono_input:
                    st.warning("Por favor, completa los campos básicos.")
                else:
                    # Encriptación
                    password_bytes = nueva_password.encode('utf-8')
                    salt = bcrypt.gensalt()
                    hash_password = bcrypt.hashpw(password_bytes, salt)
                    hash_str = hash_password.decode('utf-8')
                    
                    conn = iniciar_conexion()
                    if conn:
                        try:
                            cursor = conn.cursor()
                            
                            if rol_registro == "Cliente":
                                query_insert = """
                                    INSERT INTO T_tCliente (IdCliente, DNI, Nombre, Telefono, PasswordHash) 
                                    VALUES ((SELECT ISNULL(MAX(IdCliente), 0) + 1 FROM T_tCliente), ?, ?, ?, ?)
                                """
                                cursor.execute(query_insert, (identificador_input, nombre_input, telefono_input, hash_str))
                            else:
                                # Insertar Técnico
                                query_insert = """
                                    INSERT INTO T_tTecnico (IdTecnico, Codigo, Nombre, Cargo, Especialidad, Telefono, PasswordHash) 
                                    VALUES ((SELECT ISNULL(MAX(IdTecnico), 0) + 1 FROM T_tTecnico), ?, ?, ?, ?, ?, ?)
                                """
                                cursor.execute(query_insert, (identificador_input, nombre_input, cargo_input, especialidad_input, telefono_input, hash_str))
                                
                            conn.commit()
                            st.success(f"✅ ¡{rol_registro} registrado con éxito! Ya puedes iniciar sesión.")
                        except Exception as e:
                            st.error(f"Error al guardar en la base de datos: {e}")

# ==========================================
# 5. INTERFACES POR ROL (UX)
# ==========================================
def cerrar_sesion():
    st.session_state.autenticado = False
    st.session_state.rol = None
    st.session_state.usuario = None

def interfaz_mecanico():
    st.sidebar.title(f"🛠️ Técnico ID: {st.session_state.usuario}")
    opcion = st.sidebar.radio("Navegación:", ["🔍 Reportes Pendientes", "📋 Mis Órdenes de Trabajo", "📂 Historial Vehicular"])
    st.sidebar.markdown("---")
    st.sidebar.button("Cerrar Sesión", on_click=cerrar_sesion)
    
    if opcion == "🔍 Reportes Pendientes":
        st.title("Reportes de Clientes (Sin Asignar)")
        st.markdown("---")
        
        df_pendientes = obtener_reportes_pendientes()
        if not df_pendientes.empty:
            st.dataframe(df_pendientes, use_container_width=True, hide_index=True)
            
            st.subheader("Asignarme un Reporte")
            with st.form("form_asignar_reporte", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with col1:
                    id_orden_input = st.number_input("Crear ID para la nueva Orden", min_value=1, step=1)
                    id_reporte_input = st.number_input("Escribe el ID_Reporte a tomar", min_value=1, step=1)
                with col2:
                    diagnostico_input = st.text_area("Diagnóstico Preliminar")
                    solucion_input = st.text_area("Solución a Aplicar")
                    
                if st.form_submit_button("Tomar Reporte y Crear Orden"):
                    if diagnostico_input and solucion_input:
                        exito = insertar_orden(id_orden_input, id_reporte_input, st.session_state.usuario, diagnostico_input, solucion_input)
                        if exito:
                            st.success("✅ ¡Te has asignado el reporte correctamente!")
                            st.rerun()
                    else:
                        st.warning("⚠️ Completa los campos de diagnóstico y solución.")
        else:
            st.info("No hay reportes nuevos pendientes de revisión.")
            
    elif opcion == "📋 Mis Órdenes de Trabajo":
            st.title("Mis Trabajos Asignados")
            st.markdown("---")
            
            df_mis_ordenes = obtener_mis_ordenes(st.session_state.usuario)
            
            if not df_mis_ordenes.empty:
                st.dataframe(df_mis_ordenes, use_container_width=True, hide_index=True)
                
                # Extraemos la lista de órdenes activas del técnico para los menús desplegables
                lista_ordenes_activas = df_mis_ordenes['N° Orden'].tolist()
                
                # --- Módulo 1: Gestión de Repuestos (Mejorado) ---
                st.markdown("### 🔧 Gestión de Insumos")
                with st.expander("➕ Asignar y Ver Repuestos", expanded=False):
                    df_materiales = obtener_catalogo_materiales()
                    
                    if not df_materiales.empty:
                        with st.form("form_asignar_repuesto", clear_on_submit=False):
                            col1, col2, col3 = st.columns([1, 2, 1])
                            with col1:
                                # Ahora es un desplegable, imposible equivocarse de ID
                                orden_seleccionada = st.selectbox("Selecciona tu Orden", lista_ordenes_activas, key="rep_ord")
                            with col2:
                                opciones_mat = dict(zip(df_materiales['Nombre'], df_materiales['ID_Material']))
                                material_seleccionado = st.selectbox("Selecciona el Repuesto", list(opciones_mat.keys()))
                            with col3:
                                cantidad_input = st.number_input("Cantidad", min_value=1, step=1)
                                
                            if st.form_submit_button("Añadir a la Orden"):
                                id_mat_real = opciones_mat[material_seleccionado]
                                if agregar_material_orden(orden_seleccionada, id_mat_real, cantidad_input):
                                    st.success(f"✅ Añadido a la Orden {orden_seleccionada}.")
                                    
                        # Visualización de los repuestos ya agregados a la orden seleccionada
                        st.markdown(f"**Inventario asignado a la Orden {orden_seleccionada}:**")
                        df_repuestos_usados = obtener_repuestos_orden(orden_seleccionada)
                        if not df_repuestos_usados.empty:
                            st.dataframe(df_repuestos_usados, use_container_width=True, hide_index=True)
                        else:
                            st.info("Aún no se han asignado repuestos a esta orden.")
                    else:
                        st.warning("El catálogo de materiales está vacío.")
                
                # --- Módulo 2: Trazabilidad y Estados ---
                st.markdown("### 🚦 Semáforo de Reparación")
                with st.expander("Actualizar Estado del Vehículo", expanded=False):
                    with st.form("form_estado", clear_on_submit=True):
                        col_est1, col_est2 = st.columns(2)
                        with col_est1:
                            rep_input = st.number_input("N° de Reporte a actualizar", min_value=1, step=1)
                        with col_est2:
                            nuevo_estado = st.selectbox("Fase de Reparación", 
                                ["En Revisión", "Esperando Repuestos", "Reparación en Curso", "Listo para Entrega"])
                        
                        if st.form_submit_button("Transmitir Estado"):
                            if actualizar_estado_reporte(rep_input, nuevo_estado):
                                st.success(f"✅ Señal enviada. El cliente ahora verá que su auto está '{nuevo_estado}'.")
                                st.rerun()

                # --- Módulo 4: Liquidación y Facturación ---
                st.markdown("### 💰 Liquidación de Orden")
                with st.expander("Cerrar Orden y Generar Cobro", expanded=False):
                    with st.form("form_facturacion", clear_on_submit=True):
                        st.info("Al cerrar la orden, se sumará el costo de los repuestos asignados más la mano de obra.")
                        col_fac1, col_fac2 = st.columns(2)
                        with col_fac1:
                            orden_a_cerrar = st.selectbox("Orden a Liquidar", lista_ordenes_activas, key="fac_ord")
                        with col_fac2:
                            mano_obra_input = st.number_input("Costo de Mano de Obra (S/)", min_value=0.0, step=10.0, format="%.2f")
                        
                        if st.form_submit_button("Liquidar Orden"):
                            total = cerrar_orden_facturacion(orden_a_cerrar, mano_obra_input)
                            if total is not None:
                                st.success(f"✅ Orden {orden_a_cerrar} liquidada exitosamente. Costo Total a cobrar: **S/ {total:.2f}**")
                                # Aquí también podríamos cambiar el estado del reporte a "Finalizado"
                                
            else:
                st.info("Aún no tienes órdenes de trabajo asignadas.")

    elif opcion == "📂 Historial Vehicular":
        st.title("📂 Archivo Histórico de Vehículos")
        st.markdown("---")
        
        placa_busqueda = st.text_input("Ingresa la placa del vehículo para ver su historial:")
        
        # Al poner todo esto dentro del 'if', evitamos el UnboundLocalError
        if placa_busqueda:
            st.subheader(f"Historial registrado para la placa: {placa_busqueda.upper()}")
            df_historial = obtener_historial_vehiculo(placa_busqueda.upper())
            
            if not df_historial.empty:
                st.dataframe(df_historial, use_container_width=True, hide_index=True)
            else:
                st.warning("No se encontraron registros previos para esta placa.")

def interfaz_cliente():
    st.sidebar.title(f"👤 Cliente ID: {st.session_state.usuario}")
    st.sidebar.button("Cerrar Sesión", on_click=cerrar_sesion)
    
    st.title("📱 Mi Portal de Averías")
    st.markdown("---")
    
    # --- Módulo de Reportes Nuevos ---
    with st.expander("➕ Solicitar Reparación (Nuevo Reporte)", expanded=False):
        with st.form("form_nuevo_reporte", clear_on_submit=True):
            st.info("Ingresa los datos de tu vehículo y el problema que presenta.")
            
            col1, col2 = st.columns(2)
            with col1:
                placa_input = st.text_input("Placa del Vehículo (Ej. ABC-123)")
                modelo_input = st.text_input("Modelo y Marca (Ej. Toyota Yaris)")
            with col2:
                tipo_input = st.selectbox("Tipo de Vehículo", ["Sedán", "SUV", "Camioneta", "Hatchback", "Deportivo", "Otro"])
                
            observaciones_input = st.text_area("Detalles de la falla:")
            
            if st.form_submit_button("Enviar Solicitud al Taller"):
                if not placa_input or not modelo_input or not observaciones_input:
                    st.warning("Por favor, completa los datos de la placa, modelo y la falla de tu auto.")
                else:
                    exito = insertar_reporte_cliente(st.session_state.usuario, placa_input, modelo_input, tipo_input, observaciones_input)
                    if exito:
                        st.success("✅ ¡Reporte y vehículo registrados! Un técnico lo revisará pronto.")
                        st.rerun() 

    # --- Módulo de Seguimiento de Estados ---
    st.subheader("🚦 Mis Reportes Activos")
    df_mis_reportes = obtener_reportes_cliente(st.session_state.usuario)
    if not df_mis_reportes.empty:
        st.dataframe(df_mis_reportes, use_container_width=True, hide_index=True)
    else:
        st.info("No tienes reportes de averías registrados actualmente.")
        
    st.markdown("---")
    
    # --- Módulo de Facturación y Recibos ---
    st.subheader("💰 Mis Recibos y Pagos")
    df_recibos = obtener_recibos_cliente(st.session_state.usuario)
    
    if not df_recibos.empty:
        # Iteramos sobre cada recibo para crear una vista tipo "Boleta"
        for index, row in df_recibos.iterrows():
            with st.expander(f"🧾 Orden N° {row['N° Orden']} | {row['Placa']} | Total: S/ {row['TOTAL A PAGAR (S/)']:.2f}", expanded=False):
                st.markdown("### 🏢 Comprobante de Servicio Vehicular")
                st.write(f"**Vehículo:** {row['Modelo']} ({row['Placa']})")
                st.write(f"**Fecha de Ingreso:** {row['Fecha de Ingreso']} | **Fecha de Salida:** {row['Fecha de Salida']}")
                st.write(f"**Diagnóstico Técnico:** {row['Diagnostico']}")
                st.write("---")
                
                # Desglose de costos usando métricas visuales
                col_r1, col_r2, col_r3 = st.columns(3)
                col_r1.metric(label="Repuestos e Insumos", value=f"S/ {row['Costo Repuestos (S/)']:.2f}")
                col_r2.metric(label="Mano de Obra", value=f"S/ {row['Mano de Obra (S/)']:.2f}")
                col_r3.metric(label="Total a Pagar", value=f"S/ {row['TOTAL A PAGAR (S/)']:.2f}")
                
                # Botón de simulación de pago
                if st.button(f"💳 Procesar Pago - Orden {row['N° Orden']}", key=f"btn_pago_{row['N° Orden']}"):
                    st.success("✅ ¡Pago procesado con éxito! Gracias por confiar en nuestro servicio.")
                    st.balloons() # Animación visual de celebración de Streamlit
    else:
        st.info("No tienes recibos pendientes de pago en este momento.")

# ==========================================
# 6. ENRUTADOR PRINCIPAL
# ==========================================
if not st.session_state.autenticado:
    mostrar_login()
else:
    if st.session_state.rol == "Mecanico":
        interfaz_mecanico()
    elif st.session_state.rol == "Cliente":
        interfaz_cliente()