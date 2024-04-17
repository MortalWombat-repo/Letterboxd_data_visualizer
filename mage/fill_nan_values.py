if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
import pyarrow.parquet as pq


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Define data types for columns to prevent conversion from int to float
    # Assuming 'data' is your DataFrame
    # Assuming 'data' is your DataFrame
    data = data.fillna(0)
    # Create a mask where True indicates the original value was NaN
    mask = data.isnull()

    # Replace 0 values with None where the original value was NaN
    data = data.where(~mask, None)
    return(data)
