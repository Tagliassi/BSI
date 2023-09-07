-- Lab 01

CREATE DATABASE lab_02;
Use lab_02;

DROP DATABASE lab_02

/* Lógico_1: */

CREATE TABLE Empregado (
    Matricula int PRIMARY KEY,
    Nome varchar(100),
    Data_Nascimento date,
    Cpf varchar(11)
);

CREATE TABLE Dependente (
    Id_Dependente int PRIMARY KEY,
    Data_Nascimento date,
    Nome varchar(100),
    fk_Empregado_Matricula_Empregado int
);
 
ALTER TABLE Dependente ADD CONSTRAINT FK_Dependente_2
    FOREIGN KEY (fk_Empregado_Matricula_Empregado)
    REFERENCES Empregado (Matricula)
    ON DELETE CASCADE;
    
drop table Empregado;
 ---------------------   
 
INSERT INTO Empregado (Matricula, Nome, Data_Nascimento, Cpf) VALUES
(123, 'Maria Silva', '1990-02-10','11645325598'),
(234, 'Rafael Santos', '1990-02-10','18925503392'),
(456, 'Antônico Castro', '1990-02-10','56048925238');

INSERT INTO Dependente (Id_Dependente, Data_Nascimento, Nome, fk_Empregado_Matricula_Empregado) VALUES 
(1, '2021-01-05', 'Thiago', 123),
(2, '2020-04-11', 'Aninha', 123),
(3, '2017-11-09', 'João', 234);

SELECT * FROM Empregado AS e, Dependente AS d
WHERE e.Matricula = d.fk_Empregado_Matricula_Empregado;
;

SELECT 
	e.Matricula AS Matricula, 
    e.Nome as Empregado,
    d.Nome as Dependente,
    TIMESTAMPDIFF(year, d.Data_Nascimento, CURDATE()) AS 'Idade do Depedente',
    TIMESTAMPDIFF(year, e.Data_Nascimento, CURDATE()) AS 'Idade do Empregado'
FROM 
	Empregado AS e, Dependente AS d
WHERE e.Matricula = d.fk_Empregado_Matricula_Empregado;