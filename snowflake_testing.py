import snowflake.connector as sf
import pandas as pd



ctx = sf.connect (
    user = 'ramachandrans410',
    password = 'RPsfaMBp@2023',
    account = 'HZNPDLN-PE83191',
    #warehouse = 'compute_wh',    
    database = 'TASTY_BYTES_SAMPLE_DATA',
    #schema = 'RAW_POS'
)
print("Got the context object")

cursr = ctx.cursor()

cursr.execute("select * from TASTY_BYTES_SAMPLE_DATA.RAW_POS.MENU")
data = cursr.fetchall()
print(type(data))
print(type(data[0]))
