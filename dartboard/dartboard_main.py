###################
# @package dartboard
#
# The entry point for our dartboard
# application. This should kick off all
# of the main processes of our application.
###################
from backend import django_setup
import painter_example

# Note: this is used to make our workflows actually grab all the classes
# Some classes may not be directly called by our code and adding those
# to the extra_imports file allows those to be picked up by the installer
import extra_imports

# Opens a new Painter Example window.
# This should be the last thing executed here or should
# be moved to execute on it's own thread
painter_example.start_window()
