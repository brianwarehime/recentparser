from binplist import binplist
import argparse
import getpass
import sys

parser = argparse.ArgumentParser(description='Parse the LSSharedFileList plist for Recent Items')
parser.add_argument("--docs", action="store_true", help="Lists Recent Documents in LSSharedFileList")
parser.add_argument("--apps", action="store_true", help="Lists Recent Applications in LSSharedFileList")

sharedfilepath = "/Users/%s/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList." % getpass.getuser()

def parse_plist(fd):
	bplist = binplist.BinaryPlist(fd)
	parsed_list = bplist.Parse()
	for item in parsed_list['$objects']:
	    if isinstance(item, (str)):
	        if 'file:///' in item:
	            try:
	                print str(item).encode('utf-8')
	            except:
	                pass

if __name__ == "__main__":
    args = parser.parse_args()

    if len(sys.argv) == 1:
    	parser.print_help()
    	sys.exit(1)

    if args.docs:
		with open(sharedfilepath + "RecentDocuments.sfl", "rb") as fd:
			parse_plist(fd)
		    
    if args.apps:
		with open(sharedfilepath + "RecentApplications.sfl", "rb") as fd:
		    parse_plist(fd)