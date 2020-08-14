import pandas as pd

def get_data_from_txt_file(txt_path):
    """gets data from text file"""
    txt_lst = []
    try:
        with open(txt_path, 'r', encoding="latin-1") as txt_file:
            for line in txt_file.readlines():
                line = line.strip('\n')
                txt_lst.append(line)
    except (IndexError, ValueError, TypeError, IOError, KeyError, NameError, EOFError,
            OSError, SystemError, AssertionError, RuntimeError):
        pass
    return txt_lst 
    
def get_data_frm_datasheet(db_path, sheet_name):
  """Dataframe manipulations after reading file from excel sheet"""
    df = pd.read_excel(db_path, sheet_name=sheet_name)
    aivc = df.loc[(df['A-IVC']=='R') | (df['A-IVC']=='T') ]
    aivc.to_csv('selected.csv')
    
def get_data_frm_datasheet( db_path, sheet_name):
    """gets data from excel file"""
    datasheet_df = pd.read_excel(db_path, sheet_name=sheet_name, usecols='C,E',
                                      skiprows=0)
    datasheet_df = datasheet_df.dropna()
    dbeventlist = datasheet_df['Event Name'].tolist()
    dbkeywordlist = datasheet_df['Keyword'].tolist()
    return datasheet_df, dbeventlist, dbkeywordlist
