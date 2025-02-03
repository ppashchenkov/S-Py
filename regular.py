import re


num_pattern = r'[0-9]'
big_char_pattern = r'[A-Z]'
small_char_pattern = r'[a-z]'
symbol_pattern = r'[\!\@\#\$\%\^\&\*\(\)\_\-\+\~\`\=\:\;\?\,\.\{\}\|\[\]\/]'

def is_exist(pattern, text):
    return re.search(pattern, text) is not None

def is_valid(password):
    return  is_exist(num_pattern, password) and \
            is_exist(big_char_pattern, password) and \
            is_exist(small_char_pattern, password) and \
            is_exist(symbol_pattern, password)

