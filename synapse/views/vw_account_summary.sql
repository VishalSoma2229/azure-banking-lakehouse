USE banking_gold_dw;
GO

-- 1. View: Account Summary
CREATE OR ALTER VIEW dbo.vw_account_summary AS
SELECT *
FROM OPENROWSET(
    BULK 'https://bankingdelakevishal.dfs.core.windows.net/gold/account_summary/',
    FORMAT = 'DELTA'
) AS [result];
GO