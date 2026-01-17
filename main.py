import sys


if len(sys.argv) >= 2 and sys.argv[1] and sys.argv[1] == "register":
    import gui.register
else:
    import gui.login
