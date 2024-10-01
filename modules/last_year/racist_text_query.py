def racist_text_query(text, bigotry_dict):
  words = text.split()
  for word in words:
    if word in bigotry_dict:
      return True
  return False

def read_text(file_path):
  with open(file_path, 'r') as file:
    return file.read()