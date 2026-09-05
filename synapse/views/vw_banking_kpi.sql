USE banking_gold_dw;
GO

-- 4. View: Banking KPI Summary
CREATE OR ALTER VIEW dbo.vw_banking_kpi AS
SELECT *
FROM OPENROWSET(
    BULK 'https://bankingdelakevishal.dfs.core.windows.net/gold/banking_kpi_summary/',
    FORMAT = 'DELTA'
) AS [result];
GO