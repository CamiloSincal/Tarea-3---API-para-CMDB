CREATE TABLE tipo_ci (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE entorno (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE data_del_item (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo_ci_id INTEGER NOT NULL REFERENCES tipo_ci(id),
    decstipcion TEXT,
    num_serial VARCHAR(100),
    version VARCHAR(50),
    fecha_adquisicion DATE,
    estado VARCHAR(50),
    localizacion VARCHAR(255),
    propietario VARCHAR(255),
    enlace_documentacion TEXT,
    enlace_incidente TEXT,
    nivel_seguridad VARCHAR(50),
    cumplimiento VARCHAR(100),
    estado_configuracion VARCHAR(50),
    numero_licencia VARCHAR(100),
    fecha_expiracion DATE,
    fecha_creacion_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultima_actualizacion_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE entorno_ci (
    id SERIAL PRIMARY KEY,
    ci_id INTEGER NOT NULL REFERENCES data_del_item(id),
    entorno_id INTEGER NOT NULL REFERENCES entorno(id),
    UNIQUE (ci_id, entorno_id)
);

CREATE TABLE ci_relacion (
    id SERIAL PRIMARY KEY,
    padre_id INTEGER NOT NULL REFERENCES data_del_item(id),
    hijo_id INTEGER NOT NULL REFERENCES data_del_item(id),
    tipo_relacion VARCHAR(100),
    CONSTRAINT no_autoreferencia CHECK (padre_id <> hijo_id)
);

CREATE TABLE ci_log (
    id SERIAL PRIMARY KEY,
    ci_id INTEGER NOT NULL REFERENCES data_del_item(id),
    description TEXT NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CARGA DE DATOS IMPORTANTES
INSERT INTO tipo_ci (nombre) VALUES 
    ('Servidor'),
    ('Base de Datos'),
    ('Aplicación');

INSERT INTO entorno (nombre) VALUES 
    ('DEV'),
    ('QA'),
    ('PROD');


-- VALORES DE PRUEBA
INSERT INTO data_del_item (
    nombre, tipo_ci_id, decstipcion, num_serial, version,
    fecha_adquisicion, estado, localizacion, propietario,
    enlace_documentacion, enlace_incidente, nivel_seguridad,
    cumplimiento, estado_configuracion, numero_licencia,
    fecha_expiracion
) VALUES

('Servidor Web 1', 1, 'Servidor Apache en Ubuntu', 'SN123456', '2.4.57',
 '2023-01-15', 'Activo', 'Data Center 1', 'Equipo 1',
 'http://docs/servidor1', 'http://incidentes/123', 'Media',
 'ISO 27001', 'Completado', 'LIC-SRV-001', '2027-01-14'),

('Base de Datos Principal', 2, 'PostgreSQL principal', 'SN789456', '14.9',
 '2022-06-01', 'Activo', 'Data Center 1', 'Equipo 2',
 'http://docs/db1', 'http://incidentes/456', 'Alta',
 'PCI DSS', 'Validado', 'LIC-DB-002', '2026-06-01'),

('App Corporativa', 3, 'Aplicación interna para empleados', 'SN654321', '1.0.3',
 '2023-03-22', 'Desplegado', 'Nube AWS', 'Equipo 3',
 'http://docs/app', 'http://incidentes/789', 'Media',
 'SOX', 'En progreso', 'LIC-APP-003', '2025-03-21');
