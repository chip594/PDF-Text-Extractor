# formatter.py

class TextFormatter(object):

    def name_tab_title(self, text):
        # stores contents of the input text into a list
        name_badge = text.split('\n')

        badges = []

        # strip the whitepsace from every element
        for element in name_badge:
            badges.append(element.strip())

            