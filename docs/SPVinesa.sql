USE [TEST_VINESA]
GO
/****** Object:  StoredProcedure [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS]    Script Date: 05/03/2021 17:58:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS]
(
	@Opcion nvarchar(3),
	@EstadoDoc nvarchar(10),
	@Establecimiento nvarchar(3),
	@PtoEmision nvarchar(3),
	@FechaInicial datetime,
	@FechaFinal datetime,
	@CardCode nvarchar(50),
	@FolioIni nvarchar(9),
	@FolioFin nvarchar(9),
	@PdfCreado nvarchar(10),
	@MailEnviado nvarchar(10),
	@Branch nvarchar(3),
	@UserCode nvarchar(50),
	@IncNoDec nvarchar(1),
	@IsCreateDate nvarchar(1)
)
-- =============================================
-- Autor           : Germán Quintero Muñoz
-- Fecha Creación  : 14/06/2017
-- Nombre SP       : EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS
-- Tabla Principal : DOCUMENTOS EMITIDOS
-- Descripción     : LISTA LOS DOCUMENTOS EMITIDOS
-- =============================================
AS

SET @EstadoDoc = NULLIF(@EstadoDoc,'')
SET @Establecimiento = NULLIF(@Establecimiento,'')
SET @PtoEmision = NULLIF(@PtoEmision,'')
SET @CardCode = NULLIF(@CardCode,'')
SET @FolioIni = NULLIF(@FolioIni,'')
SET @FolioFin = NULLIF(@FolioFin,'')
SET @PdfCreado = NULLIF(@PdfCreado,'')
SET @MailEnviado = NULLIF(@MailEnviado,'')
SET @Branch = NULLIF(@Branch,'')
SET @UserCode = NULLIF(@UserCode,'')
SET @IncNoDec = NULLIF(@IncNoDec,'')

BEGIN

	CREATE TABLE #Documentos
	(
		NomDocSap varchar(50),
		RowNumber bigint,
		DocEntry int,
		DocNum int,
		Folio varchar(20),
		CardCode varchar(15),
		CardName varchar(100),
		DocTotal numeric(19,6),
		CreateDate datetime,
		TaxDate datetime,
		FolioRec varchar(20),
		EstadoDoc varchar(50),
		CodEstado varchar(10),
		ObjType varchar(20),
		DocSubType varchar(2),
		PdfCreado varchar(10),
		MailEnviado varchar(10),
		BranchId varchar(3),
		BranchName varchar(100),
		Canceled varchar(2),
		CheckBox varchar(1),
		ClaveAcceso varchar(50),
		CodEntidad varchar(4),
		TipoComp varchar(4),
		Tabla varchar(20)
	)

	IF @Opcion = 'FV' OR @Opcion = 'FVT' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FV] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate

	IF @Opcion = 'FVP' OR @Opcion = 'FVT' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FVP] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate

	IF @Opcion = 'FVA' OR @Opcion = 'FVT' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FVA] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate

	IF @Opcion = 'FVR' OR @Opcion = 'FVT' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FVR] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	IF @Opcion = 'NCV' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_NCV] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	IF @Opcion = 'NDV' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_NDV] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate

	IF @Opcion = 'GS' OR @Opcion = 'GR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_GS] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	IF @Opcion = 'TS' OR @Opcion = 'GR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_TS] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate

	IF @Opcion = 'FC' OR @Opcion = 'CR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FC] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	IF @Opcion = 'FCA' OR @Opcion = 'CR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FCA] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate

	IF @Opcion = 'FCR' OR @Opcion = 'CR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_FCR] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	IF @Opcion = 'NDC' OR @Opcion = 'CR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_NDC] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	IF @Opcion = 'LC' OR @Opcion = 'CR' OR @Opcion = 'LT'
		INSERT #Documentos EXEC [dbo].[EXX_FE_LISTAR_DOCUMENTOS_EMITIDOS_LC] @EstadoDoc, @Establecimiento, @PtoEmision, @FechaInicial, @FechaFinal, @CardCode, @FolioIni, @FolioFin, @PdfCreado, @MailEnviado, @Branch, @UserCode, @IncNoDec, @IsCreateDate
	
	SELECT * FROM #Documentos
	DROP TABLE #Documentos

END