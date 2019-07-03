duplicate_free_list = []

with open("emails.txt") as file_object:
  email_list = file_object.read()

no_space = email_list.replace("\n", " ")
split_emails = no_space.split(", ")

for email in split_emails:
  if email not in duplicate_free_list:
    duplicate_free_list.append(email)
  
with open("duplicate-free-email-list.txt", "w") as file_object:
  file_object.write(",".join(duplicate_free_list))