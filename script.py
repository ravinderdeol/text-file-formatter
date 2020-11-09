# Open The Text File & 'Read' It
# Insert The File Path Between The Brackets & Quotation Marks

with open("  ", "r") as file:

# Read The File & Write The First Replace Method

  remove_1 = file.read().replace(" .", ".")

# Remaining Replace Methods    
  
  remove_2 = remove_1.replace(" , ", ", ")
  remove_3 = remove_2.replace(" ( ", " (")
  remove_4 = remove_3.replace(" )", ")")
  remove_5 = remove_4.replace(" ? ", "? ")
  remove_6 = remove_5.replace(" ‘ ", " ‘")
  remove_7 = remove_6.replace(" ’ ", "’ ")
  remove_8 = remove_7.replace(" : ", ": ")
  remove_9 = remove_8.replace(" (yellow) ", "")
  remove_10 = remove_9.replace("Highlight-","")

# 'Write' To A New Text File (Or Update Existing)
# Insert The File Path Between The Brackets & Quotation Marks

with open (" ", "w") as file:

# Call The Last Replace Method

  file.write(remove_10)
