def validate_todo(dict):
  title = dict["title"]  
  if not title:
      raise ValueError("Title cannot be null.")
  if type(title) != str:
      raise ValueError("Title have to be a string")
