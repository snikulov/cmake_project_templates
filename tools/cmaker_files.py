#
#
#
import os, argparse, fnmatch

def out_files_var(start_path, rel_fold, wildcard, var_name) :
    path = start_path + rel_fold
    files = []
    for root, dirnames, filenames in os.walk(path) :
        for fname in fnmatch.filter(filenames, wildcard) :
            files.append(os.path.relpath(os.path.join(root, fname), start_path).replace('\\', '/'))

    print( 'set(' + var_name + ')' );
    for elm in files :
        print('    ' + elm);
    print(')')


def main():

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-r', '--root', metavar='root', type=str, help='source root dir', default=".")

    args = parser.parse_args()

    start_path = os.path.abspath(args.root)

    out_files_var(start_path, '/include', '*.h*', 'HDR_FILES')
    out_files_var(start_path, '/src', '*.c*', 'SRC_FILES')

if __name__ == '__main__' :
    main()
else:
    print('loaded as module')
