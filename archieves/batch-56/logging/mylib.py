import logging
import myapp

def main():
    logging.basicConfig(filename='myappy.log', level=logging.INFO)
    logging.info('Started')
    myapp.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
