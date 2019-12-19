#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import logging

class Chapter1:
    '''
    Resolution of excercises from Arrays and Strings
    '''
    def exercise1_areRepeatedCharacters( self, string ):
        ''' Find if a character is repeated '''
        characters = set()
        for character in string:
            if character in characters:
                logging.info('There are repeated characters. %s repeats in %s', character, string )
                return True
            characters.add( character )
        logging.info('There are not repeated characters in string %s.', string )
        return False
    def exercise1b_areRepeatedCharacters_noDataStructure( self, passedString):
        import string
        for letter in list(string.ascii_lowercase):
            oneTimeApparison = False
            for character in passedString:
                if character == letter:
                    if oneTimeApparison:
                        logging.info('There are repeated characters. %s repeats in %s', character, passedString )
                        return True
                    oneTimeApparison = True 
        logging.info('There are not repeated characters in string %s.', passedString )
        return False
 
        
def main():
    
    import logging 
    import sys 
    root = logging.getLogger() 
    root.setLevel(logging.DEBUG) 
    handler = logging.StreamHandler(sys.stdout) 
    handler.setLevel(logging.DEBUG) 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
    handler.setFormatter(formatter) 
    root.addHandler(handler)
    chapter1 = Chapter1()
    chapter1.exercise1b_areRepeatedCharacters_noDataStructure('abc')
    chapter1.exercise1b_areRepeatedCharacters_noDataStructure('aac')

main()