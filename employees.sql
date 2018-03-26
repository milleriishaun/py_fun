PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employees (id integer primary key, name text);
INSERT INTO employees VALUES(1,'Max Eisenhardt');
INSERT INTO employees VALUES(2,'Pietro Maximoff');
INSERT INTO employees VALUES(3,'Wanda Maximoff');
INSERT INTO employees VALUES(4,'Cool Guy');
COMMIT;
