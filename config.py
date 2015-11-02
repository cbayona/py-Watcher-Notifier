
# watcher configuration
class Watcher:
   # the path that we want to watch
   path = "/home/[user]/public_html"

   # a value that indicates if we want to watch the folder recursively
   recursively = True

   # a value that indicates if we want to auto add to the watcher the new created folders withing the PATH
   auto_add = True

   # the log filename we are going to use
   log_filename = 'watcher.log'


# email notifier configuration
class Notifier:
   # the users that will receive the notifications
   receivers = ("admin1@gmail.com", "admin2@gmail.com")

   # the sender email
   sender = 'user@email.com'

   # the smpt server username
   username = "user@gmail.com"

   # the smpt server password
   password = "the-password"

   # the subject of the message
   subject = "ALERT!! -> Some files changed"

   # the smpt server hosr
   host = "smtp.gmail.com"

   # the smpt server port
   port = 587
