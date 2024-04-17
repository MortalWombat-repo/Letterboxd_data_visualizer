--Docs: https://docs.mage.ai/guides/sql-blocks
--Write SQL to create a partitioned table
CREATE OR REPLACE TABLE `core-forklift-412322.letterboxd.movies_partitioned`
PARTITION BY DATE(year)
AS
SELECT *,
       date AS year
FROM {{ df_1 }};
