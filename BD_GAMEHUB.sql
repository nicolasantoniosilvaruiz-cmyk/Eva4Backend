CREATE DATABASE IF NOT EXISTS gamehub_revision
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;

USE gamehub_revision;

CREATE TABLE catalogo_genero (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uq_genero_nombre (nombre)
) ENGINE=InnoDB;

CREATE TABLE catalogo_videojuego (
    id BIGINT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    fecha_lanzamiento DATE NOT NULL,
    disponible BOOLEAN NOT NULL,
    genero_id BIGINT NOT NULL,
    PRIMARY KEY (id),
    KEY idx_videojuego_genero (genero_id),
    CONSTRAINT fk_videojuego_genero
        FOREIGN KEY (genero_id) REFERENCES catalogo_genero (id)
        ON DELETE RESTRICT
) ENGINE=InnoDB;

START TRANSACTION;

INSERT INTO catalogo_genero (id, nombre) VALUES
    (1, 'Accion'),
    (2, 'Estrategia'),
    (3, 'Aventura'),
    (4, 'Simulacion');

INSERT INTO catalogo_videojuego
    (id, titulo, precio, fecha_lanzamiento, disponible, genero_id)
VALUES
    (1, 'Halo: Combat Evolved',             25000.00, '2001-10-05', TRUE, 1),
    (2, 'Halo 2',                           30000.00, '2004-10-09', TRUE, 1),
    (3, 'Halo 3',                           35000.00, '2007-09-25', TRUE, 1),
    (4, 'Halo 4',                           40000.00, '2012-10-06', TRUE, 1),
    (5, 'Rayman Legends',                    5000.00, '2013-08-20', TRUE, 3),
    (6, 'Horizon: Zero Dawn',               60000.00, '2017-03-01', TRUE, 3),
    (7, 'Age of Empires',                   10000.00, '1997-10-26', TRUE, 2),
    (8, 'Sid Meier''s Civilizations VI',   100000.00, '2017-12-21', TRUE, 2),
    (9, 'Los Sims 4',                       60000.00, '2014-05-02', TRUE, 4),
    (10, 'Simcity 2',                       45000.00, '2023-10-24', TRUE, 4);

COMMIT;