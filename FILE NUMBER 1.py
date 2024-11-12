import importlib

list_of_banks = [
    'bank_of_india', 
    'bank_of_maharashtra', 
    'canara_bank', 
    'central_bank_of_india',
    'state_bank_of_india',  
    'axis_bank',            
    'bandhan_bank',     
    'federal_bank',     
    'hdfc_bank',            
    'dcb_bank',         
    'indusind_bank',    
    'idfc_bank',      
    'jammu_and_kashmir_bank',   
    'karur_vysya_bank',    
    'kotak_mahindra_bank', 
    'nainital_bank',      
    'rbl_bank',           
    'tamilnad_mercantile_bank',  
    'idbi_bank',           
    'capital_small_finance_bank', 
    'suryoday_small_finance_bank',  
    'ujjivan_small_finance_bank',    
    'utkarsh_small_finance_bank',     
    'esaf_small_finance_bank',        
    'north_east_small_finance_bank', 
    'unity_small_finance_bank',      
    'citibank_india',                 
    'dbs_bank_india',
    'deutsche_bank',                   
    'hsbc_bank',                        
    'standard_chartered_bank']

for bank in list_of_banks:
    print(f"Running {bank}.py...")
    importlib.import_module(bank)
    print(f"Finished running {bank}.py.")
