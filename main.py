import struct
import os
import sys

thfsFile = sys.argv[1]
thfsFileName = thfsFile.replace('.thfs', '') + '/'
inFile = open(thfsFile, 'rb')
fileContent = inFile.read()
inFile.close()

if fileContent[0:4] != b'THFS':
    raise SystemExit('This is not a THFS file!')

fileSize = struct.unpack('<I', fileContent[4:8])[0]
numFiles = struct.unpack('<I', fileContent[8:12])[0]
print('THFS Filesize: ' + str(fileSize))
print('Number of files: ' + str(numFiles))

try:
    os.mkdir(thfsFileName)
except:
    pass

for fileNum in range(0, numFiles):
    fileTableData = fileContent[fileNum*64+16:fileNum*64+96]
    fileName = struct.unpack('40s', fileTableData[8:48])[0].decode('ascii').strip('\0')
    fileOffset = struct.unpack('<I', fileTableData[48:52])[0]
    fileSize = struct.unpack('<I', fileTableData[52:56])[0]
    print(fileName + ' : ' + str(fileSize) + ' bytes at offset ' + str(fileOffset))
    outFile = open(thfsFileName+fileName, 'wb')
    outFile.write(fileContent[fileOffset:fileOffset+fileSize])
    outFile.close()
