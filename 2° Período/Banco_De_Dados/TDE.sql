-- Criação da database
CREATE DATABASE TDE_TRANSACTION;
USE TDE_TRANSACTION;

-- Criação da tabela "Contas"
CREATE TABLE Contas (
    IDConta INT AUTO_INCREMENT PRIMARY KEY,
    NomeCliente VARCHAR(255) NOT NULL,
    Saldo DECIMAL(10, 2) NOT NULL
);

-- Inserir algumas contas de exemplo
INSERT INTO Contas (NomeCliente, Saldo) VALUES
    ('ClienteA', 1000.00),
    ('ClienteB', 1500.00);
    
-- Mostra a tabela Contas
SELECT * FROM Contas;

DELIMITER //
CREATE PROCEDURE RealizarTransferencia()
BEGIN
    -- Declarar as variáveis de conta de origem e destino
    DECLARE ContaOrigem INT;
    DECLARE ContaDestino INT;
    DECLARE ValorTransferencia DECIMAL(10, 2);
    DECLARE SaldoContaOrigem DECIMAL(10, 2); 

    -- Iniciar uma transação
    START TRANSACTION;
    
    -- Definir as contas de origem e destino
    SET ContaOrigem = 1;
    SET ContaDestino = 2;
    SET ValorTransferencia = 100.00;

    -- Verificar se a conta de origem tem saldo suficiente
    SELECT Saldo INTO SaldoContaOrigem FROM Contas WHERE IDConta = ContaOrigem;

    IF SaldoContaOrigem >= ValorTransferencia THEN
        -- Atualizar o saldo da conta de origem
        UPDATE Contas
        SET Saldo = Saldo - ValorTransferencia
        WHERE IDConta = ContaOrigem;

        -- Atualizar o saldo da conta de destino
        UPDATE Contas
        SET Saldo = Saldo + ValorTransferencia
        WHERE IDConta = ContaDestino;

        -- Confirmar a transação
        COMMIT;
        SELECT 'Transferência de dinheiro concluída com sucesso.';
    ELSE
        -- A conta de origem não tem saldo suficiente, reverter a transação
        ROLLBACK;
        SELECT 'Transferência de dinheiro não foi concluída devido a saldo insuficiente.';
    END IF;
END;
//
DELIMITER ;

-- Chama o procedimento 
CALL RealizarTransferencia();

-- Mostra a tabela Contas
SELECT * FROM Contas;

