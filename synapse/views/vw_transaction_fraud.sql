USE banking_gold_dw;
GO

-- 3. View: Transaction Fraud Analytics
CREATE OR ALTER VIEW dbo.vw_transaction_fraud AS
SELECT *
FROM OPENROWSET(
    BULK 'https://bankingdelakevishal.dfs.core.windows.net/gold/transaction_fraud_analytics/',
    FORMAT = 'DELTA'
) AS [result];
GO