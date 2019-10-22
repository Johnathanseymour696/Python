#Getting Where To Save File
where = raw_input('Where Do You Want To Save Your File? ')

#Getting What To Write To File
text = raw_input('What Do You Want To Write To Your File? ')

#Actually Writing It
saveFile = open(where, 'w')
saveFile.write(text)
saveFile.close()