import argparse

# This starts building up our own little parser that does what we want
def create_parser():
    parser = argparse.ArgumentParser()

    # These will add some arguments to the parser. First is the path to the export file.
    # Second is the format of the export file. The default will be JSON, with csv as another option we can pick. The second argument also turns whatever we type (when prompted) to lowercase letters. So if we type CSV or JSON, they will make it in to the parser as csv or json, respectively.
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser

