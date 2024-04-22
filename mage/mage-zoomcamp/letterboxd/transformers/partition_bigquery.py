if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


python
@transformer
def transform(data, *args, *kwargs):
    # Assuming `data` is your DataFrame
    # Write SQL to create a partitioned table
    sql = """
    CREATE OR REPLACE TABLE `project.dataset.table`
    PARTITION BY DATE_TRUNC(date_column, YEAR)
    AS
    SELECT * FROM `project.dataset.source_table`
    """
    # Execute the SQL
    result = data.execute(sql)

    return result


