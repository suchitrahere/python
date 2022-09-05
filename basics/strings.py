import string

def playwithstrings():
  message1 = 'Hey there we learn to escape characters in strings'
  message2 = 'Use a backward slash just before the character you want to escape'
  message3 = 'Example: Hi, I\'am Suchitra'
  print(message3)

def playwithquotessingle_double_triple():
  # You can keep adding stories without worrying about escaping quotes using backward slash by just using triple quotes at the start and end
  message1 = '''This is "Awesome", I do not need to worry about quotes and "" everytime I write content '''
  print(message1)


def replacestring():
    #this demonstrates replace function of string(str) module
    # I need to replace in the below content, word "artist" with word "Technician"
    # Note that the last occurance of artist is not changed because I specified it should be changed only until 4 occurance

    text1 = '''The artist offers the most exotic and relaxing facial service.Before the service, artist checks for any existing health conditions
    .Once artist confirms that client has not major health issues, artist proceeds with the service. Our techinicians prefer to be called as "artist"'''
    text2 = str.replace(text1,'artist','technician',4)
    print(text2)


replacestring()




