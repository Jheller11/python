# Script to open Chrome with preset tabs depending on task.

import webbrowser
import sys

script, command = sys.argv

job_search_array = ["https://mail.google.com/mail/u/0/",
                    "https://www.indeed.com/",
                    "https://www.linkedin.com/in/jeffreyaheller/",
                    "https://www.monster.com/jobs/advanced-search/",
                    "https://www.builtinnyc.com/"]

print("Running {} script: ".format(script))
# use command to determine what to open
if command == "jobs":
    print("opening job search tabs...")
    for site in job_search_array:
        webbrowser.open(site, 2)
elif command == "mail":
    print("opening gmail...")
    webbrowser.open(job_search_array[0], 2)
else:
    print("command not found, opening chrome...")
    webbrowser.open("https://www.google.com/", 2)

print("finished.")
