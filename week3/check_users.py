current_users = ['jamie', 'adam', 'michael', 'amanda', 'Lyla']
new_users = ['katelyn', 'Josh', 'ABBIE', 'ryan', 'Brian']
current_users_lower = [user.lower() for user in current_users

for new_user in new_users:
  if new_user.lower() in current_users_lower:
  print("Sorry" + new_user "username unavailable.")
  else:
  print("Awesome" + new_user + "username available.")
