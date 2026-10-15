-- CREAR BD
CREATE DATABASE tienda_online_db;

-- CREAR UN USUARIO Y SU CONTRASEÑA
CREATE USER admin_tienda WITH PASSWORD 'admin123';

-- CONFIGURAR PARAMETROS DJANGO
ALTER ROLE admin_tienda SET client_encoding TO 'utf8';
ALTER ROLE admin_tienda SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin_tienda SET timezone TO 'UTC';

-- ASIGNAR PERMISOS
GRANT ALL PRIVILEGES ON DATABASE tienda_online_db TO admin_tienda;