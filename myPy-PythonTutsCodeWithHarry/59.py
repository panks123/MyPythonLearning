#regular expressions---Module Regular Expressions(RE) specifies a set of strings(pattern) that matches it.

# MetaCharacters
#  characters       Description                                                      Example

#   \               Used to drop the special meaning of character following it
#   []              Represent a character class                                       "[a-m]"
#   ^               Matches the beginning (Starts with)                               "^hello"
#   $               Matches the end(Ends with)                                        "world$"
#   .               Matches any character except newline                              "he..o"
#   ?               Matches zero or one occurrence.
#   |               Means OR                                                          "falls|stays"
#   *               Any number of occurrences (including 0 occurrences)               "aix*"
#   +               One or more occurrences                                           "aix+"
#   {}              Indicate number of occurrences of a preceding RE to match.        "al{2}"
#   ()              Enclose a group of REs


# Metacharacter backslash ‘\’ has a very important role as it signals various sequences.
# If the backslash is to be used without its special meaning as metacharacter, use’\\’

#   \d   Matches any decimal digit, this is equivalent to the set class [0-9].
#   \D   Matches any non-digit character.
#   \s   Matches any whitespace character.
#   \S   Matches any non-whitespace character
#   \w   Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
#   \W   Matches any non-alphanumeric character.

# Set class [\s,.] will match any whitespace character, ‘,’, or,’.’ .


# Function compile()
# Regular expressions are compiled into pattern objects, which have methods for various operations
# such as searching for pattern matches or performing string substitutions.
# functions for pattern object: findall,sesrch,sub,split, finditer

import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.


