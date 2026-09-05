USE banking_gold_dw;
GO

-- 2. View: Customer 360
CREATE OR ALTER VIEW dbo.vw_customer_360 AS
SELECT *
FROM OPENROWSET(
    BULK 'https://bankingdelakevishal.dfs.core.windows.net/gold/customer_360/',
    FORMAT = 'DELTA'
) AS [result];
GO