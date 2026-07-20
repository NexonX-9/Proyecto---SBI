USE proyecto_db
GO
/****** Objeto: Table dbo.T_tCanal_Reporte Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tCanal_Reporte(
	ID_Canal smallint NOT NULL,
	Nombre_Canal smallint NOT NULL,
 CONSTRAINT PK_T_tCanal_Reporte2 PRIMARY KEY NONCLUSTERED 
(
	ID_Canal ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tCliente Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tCliente(
	IdCliente smallint NOT NULL,
	DNI smallint NOT NULL,
	Nombre smallint NOT NULL,
	Telefono smallint NOT NULL,
 CONSTRAINT PK_T_tCliente0 PRIMARY KEY NONCLUSTERED 
(
	IdCliente ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tCuadrilla Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tCuadrilla(
	ID_Cuadrilla smallint NOT NULL,
	Nombre smallint NOT NULL,
 CONSTRAINT PK_T_tCuadrilla7 PRIMARY KEY NONCLUSTERED 
(
	ID_Cuadrilla ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tCuadrilla_Tecnico Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tCuadrilla_Tecnico(
	ID_Cuadrilla smallint NOT NULL,
	T_tTecnico_ID int NOT NULL,
 CONSTRAINT PK_T_tCuadrilla_Tecnico15 PRIMARY KEY NONCLUSTERED 
(
	T_tTecnico_ID ASC,
	ID_Cuadrilla ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tDetalle_Material Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tDetalle_Material(
	Cantidad smallint NOT NULL,
	ID_Orden smallint NOT NULL,
	ID_Material smallint NOT NULL,
 CONSTRAINT PK_T_tDetalle_Material16 PRIMARY KEY NONCLUSTERED 
(
	ID_Material ASC,
	ID_Orden ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tEstado_Orden Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tEstado_Orden(
	ID_est_Orden smallint NOT NULL,
	Nombre smallint NOT NULL,
 CONSTRAINT PK_T_tEstado_Orden9 PRIMARY KEY NONCLUSTERED 
(
	ID_est_Orden ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tEstado_Reporte Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tEstado_Reporte(
	ID_Estado smallint NOT NULL,
	Nombre_Estado smallint NOT NULL,
 CONSTRAINT PK_T_tEstado_Reporte5 PRIMARY KEY NONCLUSTERED 
(
	ID_Estado ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tMaterial Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tMaterial(
	ID_Material smallint NOT NULL,
	Nombre smallint NOT NULL,
 CONSTRAINT PK_T_tMaterial11 PRIMARY KEY NONCLUSTERED 
(
	ID_Material ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tOrden_Trabajo Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tOrden_Trabajo(
	ID_Orden smallint NOT NULL,
	Fecha smallint NOT NULL,
	Hora_Salida smallint NOT NULL,
	Hora_Llegada smallint NOT NULL,
	Hora_Solucion smallint NOT NULL,
	FechaSolucion smallint NOT NULL,
	Diagnostico smallint NOT NULL,
	Solucion_Aplicada smallint NOT NULL,
	ID_Reporte smallint NOT NULL,
	T_tReporte_Averia_ID_Reporte smallint NOT NULL,
	ID_Cuadrilla smallint NOT NULL,
	T_tCuadrilla_ID_Cuadrilla smallint NOT NULL,
	T_tTecnico_ID int NOT NULL,
	T_tTecnico_T_tTecnico_ID int NOT NULL,
	ID_Vehiculo smallint NOT NULL,
	T_tVehiculo_ID_Vehiculo smallint NOT NULL,
	ID_est_Orden smallint NOT NULL,
	T_tEstado_Orden_ID_est_Orden smallint NOT NULL,
 CONSTRAINT PK_T_tOrden_Trabajo10 PRIMARY KEY NONCLUSTERED 
(
	ID_Orden ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY,
 CONSTRAINT TC_T_tOrden_Trabajo13 UNIQUE NONCLUSTERED 
(
	ID_Reporte ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY,
 CONSTRAINT TC_T_tOrden_Trabajo15 UNIQUE NONCLUSTERED 
(
	T_tReporte_Averia_ID_Reporte ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tPrioridad Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tPrioridad(
	ID_prioridad smallint NOT NULL,
	Nom_Pri smallint NOT NULL,
 CONSTRAINT PK_T_tPrioridad4 PRIMARY KEY NONCLUSTERED 
(
	ID_prioridad ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tReporte_Averia Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tReporte_Averia(
	ID_Reporte smallint NOT NULL,
	Fecha smallint NOT NULL,
	Hora smallint NOT NULL,
	Observaciones smallint NOT NULL,
	T_tCliente_IdCliente smallint NOT NULL,
	IdCliente smallint NOT NULL,
	ID_Suministro smallint NOT NULL,
	T_tSuministro_T_tCliente_IdCliente smallint NOT NULL,
	T_tSuministro_IdCliente smallint NOT NULL,
	T_tSuministro_ID_Suministro smallint NOT NULL,
	ID_Canal smallint NOT NULL,
	T_tCanal_Reporte_ID_Canal smallint NOT NULL,
	ID_Tipo smallint NOT NULL,
	T_tTipo_Averia_ID_Tipo smallint NOT NULL,
	ID_prioridad smallint NOT NULL,
	T_tPrioridad_ID_prioridad smallint NOT NULL,
	ID_Estado smallint NOT NULL,
	T_tEstado_Reporte_ID_Estado smallint NOT NULL,
 CONSTRAINT PK_T_tReporte_Averia6 PRIMARY KEY NONCLUSTERED 
(
	ID_Reporte ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tSuministro Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tSuministro(
	ID_Suministro smallint NOT NULL,
	Codigo_Siministro smallint NOT NULL,
	Direccion smallint NOT NULL,
	Distrito smallint NOT NULL,
	Referencia smallint NOT NULL,
	IdCliente smallint NOT NULL,
	T_tCliente_IdCliente smallint NOT NULL,
 CONSTRAINT PK_T_tSuministro1 PRIMARY KEY NONCLUSTERED 
(
	T_tCliente_IdCliente ASC,
	IdCliente ASC,
	ID_Suministro ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tTecnico Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tTecnico(
	IdTecnico smallint NOT NULL,
	Codigo smallint NOT NULL,
	Nombre smallint NOT NULL,
	Cargo smallint NOT NULL,
	Especialidad smallint NOT NULL,
	Telefono smallint NOT NULL,
	T_tTecnico_ID int IDENTITY(1,1) NOT NULL,
 CONSTRAINT PK_T_tTecnico12 PRIMARY KEY NONCLUSTERED 
(
	T_tTecnico_ID ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tTipo_Averia Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tTipo_Averia(
	ID_Tipo smallint NOT NULL,
	Nom_Tipo smallint NOT NULL,
 CONSTRAINT PK_T_tTipo_Averia3 PRIMARY KEY NONCLUSTERED 
(
	ID_Tipo ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
/****** Objeto: Table dbo.T_tVehiculo Fecha de script: 19/07/2026 00:05:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE T_tVehiculo(
	ID_Vehiculo smallint NOT NULL,
	Placa smallint NOT NULL,
	Modelo smallint NOT NULL,
	Tipo smallint NOT NULL,
 CONSTRAINT PK_T_tVehiculo8 PRIMARY KEY NONCLUSTERED 
(
	ID_Vehiculo ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
) ON PRIMARY
GO
ALTER TABLE T_tCuadrilla_Tecnico  WITH CHECK ADD  CONSTRAINT FK_T_tCuadrilla_Tecnico20 FOREIGN KEY(T_tTecnico_ID)
REFERENCES T_tTecnico (T_tTecnico_ID)
GO
ALTER TABLE T_tCuadrilla_Tecnico CHECK CONSTRAINT FK_T_tCuadrilla_Tecnico20
GO
ALTER TABLE T_tCuadrilla_Tecnico  WITH CHECK ADD  CONSTRAINT FK_T_tCuadrilla_Tecnico21 FOREIGN KEY(ID_Cuadrilla)
REFERENCES T_tCuadrilla (ID_Cuadrilla)
GO
ALTER TABLE T_tCuadrilla_Tecnico CHECK CONSTRAINT FK_T_tCuadrilla_Tecnico21
GO
ALTER TABLE T_tDetalle_Material  WITH CHECK ADD  CONSTRAINT FK_T_tDetalle_Material28 FOREIGN KEY(ID_Material)
REFERENCES T_tMaterial (ID_Material)
GO
ALTER TABLE T_tDetalle_Material CHECK CONSTRAINT FK_T_tDetalle_Material28
GO
ALTER TABLE T_tDetalle_Material  WITH CHECK ADD  CONSTRAINT FK_T_tDetalle_Material29 FOREIGN KEY(ID_Orden)
REFERENCES T_tOrden_Trabajo (ID_Orden)
GO
ALTER TABLE T_tDetalle_Material CHECK CONSTRAINT FK_T_tDetalle_Material29
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo12 FOREIGN KEY(ID_Reporte)
REFERENCES T_tReporte_Averia (ID_Reporte)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo12
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo13 FOREIGN KEY(T_tReporte_Averia_ID_Reporte)
REFERENCES T_tReporte_Averia (ID_Reporte)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo13
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo14 FOREIGN KEY(ID_Cuadrilla)
REFERENCES T_tCuadrilla (ID_Cuadrilla)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo14
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo16 FOREIGN KEY(T_tCuadrilla_ID_Cuadrilla)
REFERENCES T_tCuadrilla (ID_Cuadrilla)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo16
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo17 FOREIGN KEY(T_tTecnico_ID)
REFERENCES T_tTecnico (T_tTecnico_ID)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo17
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo19 FOREIGN KEY(T_tTecnico_T_tTecnico_ID)
REFERENCES T_tTecnico (T_tTecnico_ID)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo19
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo22 FOREIGN KEY(ID_Vehiculo)
REFERENCES T_tVehiculo (ID_Vehiculo)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo22
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo23 FOREIGN KEY(T_tVehiculo_ID_Vehiculo)
REFERENCES T_tVehiculo (ID_Vehiculo)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo23
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo24 FOREIGN KEY(ID_est_Orden)
REFERENCES T_tEstado_Orden (ID_est_Orden)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo24
GO
ALTER TABLE T_tOrden_Trabajo  WITH CHECK ADD  CONSTRAINT FK_T_tOrden_Trabajo25 FOREIGN KEY(T_tEstado_Orden_ID_est_Orden)
REFERENCES T_tEstado_Orden (ID_est_Orden)
GO
ALTER TABLE T_tOrden_Trabajo CHECK CONSTRAINT FK_T_tOrden_Trabajo25
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia10 FOREIGN KEY(ID_Estado)
REFERENCES T_tEstado_Reporte (ID_Estado)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia10
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia11 FOREIGN KEY(T_tEstado_Reporte_ID_Estado)
REFERENCES T_tEstado_Reporte (ID_Estado)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia11
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia2 FOREIGN KEY(T_tCliente_IdCliente, IdCliente, ID_Suministro)
REFERENCES T_tSuministro (T_tCliente_IdCliente, IdCliente, ID_Suministro)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia2
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia3 FOREIGN KEY(T_tSuministro_T_tCliente_IdCliente, T_tSuministro_IdCliente, T_tSuministro_ID_Suministro)
REFERENCES T_tSuministro (T_tCliente_IdCliente, IdCliente, ID_Suministro)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia3
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia4 FOREIGN KEY(ID_Canal)
REFERENCES T_tCanal_Reporte (ID_Canal)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia4
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia5 FOREIGN KEY(T_tCanal_Reporte_ID_Canal)
REFERENCES T_tCanal_Reporte (ID_Canal)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia5
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia6 FOREIGN KEY(ID_Tipo)
REFERENCES T_tTipo_Averia (ID_Tipo)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia6
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia7 FOREIGN KEY(T_tTipo_Averia_ID_Tipo)
REFERENCES T_tTipo_Averia (ID_Tipo)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia7
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia8 FOREIGN KEY(ID_prioridad)
REFERENCES T_tPrioridad (ID_prioridad)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia8
GO
ALTER TABLE T_tReporte_Averia  WITH CHECK ADD  CONSTRAINT FK_T_tReporte_Averia9 FOREIGN KEY(T_tPrioridad_ID_prioridad)
REFERENCES T_tPrioridad (ID_prioridad)
GO
ALTER TABLE T_tReporte_Averia CHECK CONSTRAINT FK_T_tReporte_Averia9
GO
ALTER TABLE T_tSuministro  WITH CHECK ADD  CONSTRAINT FK_T_tSuministro0 FOREIGN KEY(IdCliente)
REFERENCES T_tCliente (IdCliente)
GO
ALTER TABLE T_tSuministro CHECK CONSTRAINT FK_T_tSuministro0
GO
ALTER TABLE T_tSuministro  WITH CHECK ADD  CONSTRAINT FK_T_tSuministro1 FOREIGN KEY(T_tCliente_IdCliente)
REFERENCES T_tCliente (IdCliente)
GO
ALTER TABLE T_tSuministro CHECK CONSTRAINT FK_T_tSuministro1
GO