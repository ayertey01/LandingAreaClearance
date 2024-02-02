Save the script with a .py extension (e.g., clear_old_files.py).

Open Task Scheduler. You can find it in the Control Panel or by searching in the Start menu.

In Task Scheduler, click on "Create Basic Task" in the right-hand Actions panel.

Follow the wizard to set up a basic task. Specify the name and description.

Choose the trigger type. For a daily trigger, select "Daily" and set the recurrence frequency.

Choose the action type. Select "Start a program" and browse to the Python executable and your script. For example:

Program/script: C:\Path\To\python.exe (replace with the path to your Python executable)
Add arguments: C:\Path\To\clear_old_files.py (replace with the path to your script)
Complete the wizard, review your settings, and click "Finish."

Now, the script will run automatically based on the schedule you set. Keep in mind that you need to adjust paths according to your system and Python installation.