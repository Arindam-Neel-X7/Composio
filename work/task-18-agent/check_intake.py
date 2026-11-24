with open('tools/intake_human_review.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('for app_id_str, adj_list in records.items():')
print(text[idx:idx+1500])
