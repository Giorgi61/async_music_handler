import argparse

parser = argparse.ArgumentParser(description='Download songs from any sources!',
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-dd',
                    '--download-directory',
                    help="specify the directory you want to store the downloaded music. default: %(default)smusic",
                    default='../')

parser.add_argument('-s',
                    '--song-urls',
                    help="list of song URLs.\nIMPORTANT: wrap each URL in quotes to avoid shell parsing issues.",
                    nargs='+')

parser.add_argument('-c',
                    '--config',
                    help='specify the configuration json file. default: %(default)s',
                    default='./config.json')

parser.add_argument('-t',
                    '--timer',
                    help="display total execution time upon completion",
                    action='store_true')

parser.add_argument('-w',
                    '--workers',
                    type=int,
                    help='specify the number of worker threads. default: %(default)s\nIMPORTANT: Don\'t increase the number of workers if your cpu or internet is slow!',
                    default=4)

if __name__ == '__main__':
    parser.parse_args()

