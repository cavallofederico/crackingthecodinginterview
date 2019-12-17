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
                logging.info('There are repeated characters')
                return True
            characters.add( character )
        logging.info('There are not repeated characters.')
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
    chapter1.exercise1_areRepeatedCharacters('abc')
    chapter1.exercise1_areRepeatedCharacters('aac')

main()