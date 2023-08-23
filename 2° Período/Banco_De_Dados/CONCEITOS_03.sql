CREATE DATABASE CONCEITOS;
USE CONCEITOS;

CREATE TABLE Departamento (
    ID_Depto INT PRIMARY KEY,
    Nome VARCHAR(100),
    Descricao TEXT
);
CREATE TABLE Empregado (
    ID_Emp INT PRIMARY KEY,
    Nome VARCHAR(100),
    CPF VARCHAR(20),
    fk_Departamento_ID_Depto INT
);
 
ALTER TABLE Empregado ADD CONSTRAINT FK_Empregado_2
    FOREIGN KEY (fk_Departamento_ID_Depto)
    REFERENCES Departamento (ID_Depto)
    ON DELETE RESTRICT;
    
    
INSERT INTO Departamento (ID_Depto, Nome, Descricao)
VALUES
   (111, 'Vendas', 'Depto Vendas'),
   (222, 'RH', 'Depto Recursos Humanos'),
   (333, 'Financeiro', 'Depto Financeiro');
SELECT * FROM Departamento;
INSERT INTO Empregado (ID_Emp, Nome, CPF, fk_Departamento_ID_Depto)
VALUES
   (1, 'Maria', '1234567890',111),
   (2, 'João', '2345678901',111),
   (3, 'José', '3456789012',333);
SELECT * FROM Empregado;

CREATE TABLE Projeto (
    ID_Proj INT PRIMARY KEY,
    Nome VARCHAR(100),
    Sigla VARCHAR(10)
);
CREATE TABLE Trabalha (
    ID_Trab INT PRIMARY KEY,
    fk_Empregado_ID_Emp INT,
    fk_Projeto_ID_Proj INT,
    Dt_Fim DATE,
    Dt_Inicio DATE
);
 
ALTER TABLE Trabalha ADD CONSTRAINT FK_Trabalha_1
    FOREIGN KEY (fk_Empregado_ID_Emp)
    REFERENCES Empregado (ID_Emp)
    ON DELETE RESTRICT;
 
ALTER TABLE Trabalha ADD CONSTRAINT FK_Trabalha_2
    FOREIGN KEY (fk_Projeto_ID_Proj)
    REFERENCES Projeto (ID_Proj)
    ON DELETE RESTRICT;
    
INSERT INTO Projeto (ID_Proj, Nome, Sigla)
VALUES
       (1000, 'Sistema X', 'SX'),    
       (2000, 'Sistema ABC', 'SABC');
INSERT INTO Trabalha (ID_Trab, fk_Empregado_ID_Emp, fk_Projeto_ID_Proj, Dt_Inicio, DT_Fim)
VALUES
      (1, 1, 1000, '2020-10-20', NULL), 
      (2, 3, 1000, '2019-05-03', NULL);
       
SELECT * FROM Empregado;          
SELECT * FROM Projeto;
SELECT * FROM Trabalha;

INSERT INTO Trabalha (ID_Trab, fk_Empregado_ID_Emp, fk_Projeto_ID_Proj, Dt_Inicio, DT_Fim)
VALUES
      (3, 1, 2000, '2009-10-20', '2020-10-20'), 
      (4, 3, 2000, '2022-02-01', NULL);

SELECT *
FROM Trabalha AS T, Projeto AS P, Empregado AS E
WHERE T.fk_Empregado_ID_Emp = E.ID_Emp AND 
T.fk_Projeto_ID_Proj = P.ID_Proj;

SELECT E.Nome AS 'Nome Empregado', 
P.Nome AS 'Nome Projeto', P.Sigla, T.DT_Inicio, T.DT_Fim
FROM Trabalha AS T, Projeto AS P, Empregado AS E
WHERE T.fk_Empregado_ID_Emp = E.ID_Emp AND 
T.fk_Projeto_ID_Proj = P.ID_Proj;

SELECT timestampdiff(YEAR,'2020-03-16', NOW()) AS 'Total de Anos'; -- Calcula diferença entre datas
SELECT timestampdiff(MONTH,'2020-03-16', NOW()) AS 'Total de Meses'; -- Calcula diferença entre datas
SELECT timestampdiff(DAY,'2020-03-16', NOW()) AS 'Total de Dias'; -- Calcula diferença entre datas

SELECT DATE_FORMAT(DT_Inicio, '%d/%m/%y') AS 'DT_Inicio', 
DATE_FORMAT(DT_Fim, '%d/%m/%y') AS 'DT_Fim', 
DATE_FORMAT(if(isnull(DT_Fim), NOW(), DT_Fim), '%d/%m/%y') AS 'Fim para calculo'
FROM TRABALHA;

SELECT E.Nome AS 'Nome Empregado', 
P.Nome AS 'Nome Projeto', P.Sigla, T.DT_Inicio, T.DT_Fim,
IF(Isnull(T.DT_Fim), 'Projeto Atual', 'Projeto Passado') AS 'Status'
FROM Trabalha AS T, Projeto AS P, Empregado AS E
WHERE T.fk_Empregado_ID_Emp = E.ID_Emp AND 
T.fk_Projeto_ID_Proj = P.ID_Proj
ORDER BY E.Nome;

SELECT E.Nome AS 'Nome Empregado', 
P.Nome AS 'Nome Projeto', P.Sigla, 
DATE_FORMAT(DT_Inicio, '%d/%m/%y') AS 'DT_Inicio', 
DATE_FORMAT(DT_Fim, '%d/%m/%y') AS 'DT_Fim', 
DATE_FORMAT(if(isnull(DT_Fim), NOW(), DT_Fim), '%d/%m/%y') AS 'Fim para calculo',
timestampdiff(YEAR, T.DT_Inicio, IF(ISNULL(T.DT_Fim), NOW(), T.DT_FIM)) AS 'Total de Anos',-- Calcula diferença entre datas
IF(Isnull(T.DT_Fim), 'Projeto Atual', 'Projeto Passado') AS 'Status'
FROM Trabalha AS T, Projeto AS P, Empregado AS E
WHERE T.fk_Empregado_ID_Emp = E.ID_Emp AND 
T.fk_Projeto_ID_Proj = P.ID_Proj
ORDER BY E.Nome;
