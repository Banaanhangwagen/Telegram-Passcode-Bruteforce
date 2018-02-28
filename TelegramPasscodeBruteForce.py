import hashlib
import base64
import argparse
import binascii
import sys
import string

if __name__ == '__main__':
    # Configuring the arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--salt", help="The salt in base64", required=True)
    parser.add_argument("--hash", help="The passcode hash", required=True)

    # Parse the arguments
    args = parser.parse_args()

    # Decode the passcode salt
    try:
        passcode_salt = base64.b64decode(args.salt)
    except binascii.Error:
        sys.stderr.write("ERROR: the provided base64 is incorrect\n")
        exit(-1)

    # Check the hash
    if len(args.hash) != 64 or not all(c in string.hexdigits for c in args.hash):
        sys.stderr.write("ERROR: the provided hash is incorrect (length or it's not a hexadecimal string)\n")
        exit(-1)

    # We lower the string to be able to do a simple == with the hexdigest()
    passcode_hash = args.hash.lower()

    # The current passcode
    current_passcode = ""

    # Flag to log if the passcode has been found
    found = False

    # Brute force only passcode composed of 4 digits (from 0000 to 9999)
    for i in range(0, 10000):
        # The passcode is the current "i" filled with 0 to have a length of 4
        current_passcode = str(i).zfill(4)

        # We create the hash context
        hash_ctx = hashlib.sha256()

        bytes_arr = bytearray()
        bytes_arr[0:16] = passcode_salt
        bytes_arr[16:20] = current_passcode.encode("utf8")
        bytes_arr[20:36] = passcode_salt

        # We compute the SHA256 hash
        hash_ctx.update(bytes_arr)

        # If the hash matches, the passcode is found
        if hash_ctx.hexdigest() == passcode_hash:
            found = True
            break

    if found:
        sys.stdout.write("Passcode found : %s" % current_passcode)
    else:
        sys.stdout.write("Passcode not found\n")
