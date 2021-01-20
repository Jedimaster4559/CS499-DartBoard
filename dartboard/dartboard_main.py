###################
# dartboard_main.py
#
# The entry point for our dartboard
# application. This should kick off all
# of the main processes of our application.
###################
from backend import django_setup
import painter_example

# Opens a new Painter Example window.
# This should be the last thing executed here or should
# be moved to execute on it's own thread
painter_example.open()
