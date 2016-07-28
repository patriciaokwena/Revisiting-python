from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

#I get SyntaxError: invalid syntax when I run this script.
#Again, you have to run it right on the command line, not inside Python. If you type python, and then try to type python ex14.py Zed it will fail because you are running Python inside Python. Close your window and then just type python ex14.py Zed.