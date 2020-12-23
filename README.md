Python minimal program for extracting the contents of THFS files from PSP ROMs.

# Usage
    python3 main.py <filename>

# Reverse Engineering
I used a hex editor to reverse engineer the structure of an THFS file. Here it is:

The THFS file starts with a 16 byte header:

  * 4 byte ASCII encoded "THFS" string
  * Little-endian 32bit unsigned integer: the total size of the THFS file.
  * Little-endian 32bit unsigned integer: the number of files in the table of contents.
  * 4 null bytes

After the header there's the table of contents with each entry being 64 bytes:

  * 8 bytes of unknown data that I couldn't identify. Perhaps a hash or cipher of some sort.
  * File name 40 bytes long and padded at the end with nulls.
  * Little-endian 32bit unsigned integer that represents the offset of data in the THFS file.
  * Little-endian 32bit unsigned integer filesize.
  * 4 null bytes.
  * Little-endian 32bit unsigned integer filesize (again for some reason).

After the table of contents there is the data of the files. For some reason the file data offsets start at multiples of 0x1000, I don't know why but it's irrelevant.
