
print "Hello world"
print ("Hello, Python!");
print "Hello world"
# Variables and Characters
print 'I have to learn Python'
print "L"
weight = 34
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print "My weight is,%d, and i am old" %( weight)
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

#Learning Strings and Text %r for Variables

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y #Why do you put ' (single-quotes) around some strings and not others?
#Mostly it's because of style, but I'll use a single-quote inside a string that has double-quotes.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

#More printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#Remember /n
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#Getting input
#The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.
#int(raw_input()) which gets the number as a string from raw_input() then converts it to an integer using int().
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Escape Sequences that Python Supports
#"""ESCAPE	WHAT IT DOES.
#\\	Backslash (\)
#\'	Single-quote (')
#\"	Double-quote (")
#\a	ASCII bell (BEL)
#\b	ASCII backspace (BS)
#\f	ASCII formfeed (FF)
#\n	ASCII linefeed (LF)
#\N{name}	Character named name in the Unicode database (Unicode only)
#\r	Carriage Return (CR)
#\t	Horizontal Tab (TAB)
#\uxxxx	Character with 16-bit hex value xxxx (Unicode only)
#\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v	ASCII vertical tab (VT)
#\ooo	Character with octal value ooo
#\xhh	Character with hex value hh """

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#intead of using print with rawinput
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)