'''
Text Formatter Module

This module will format the string input to match the desired output.
'''

class TextFormatter(object):

    # takes in a string parameter
    # returns the string formatted as: 'name TAB title'
    def name_tab_title(self, text):
        # stores contents of the input text into a list
        name_badge = text.split('\n')

        badges = []

        # strip the whitepsace from every element
        for element in name_badge:
            badges.append(element.strip())

        # return true from as long as the badge has a blank line
        while badges.count(''):
            badges.remove('')

        # stores the last string added to the badge list as the title
        title = badges.pop()

        # stores the first string added to the badge list as the name
        name = badges.pop()

        # formats the string as 'name TAB title'
        name_badge = ('%s\t%s\n' % (name, title))
        
        return name_badge
