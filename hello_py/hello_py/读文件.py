

file_object = open('/Users/yangyi/Desktop/text_py.rtf')
try:
    file_context = file_object.read()
    # file_object.write('什么玩意?')
    # file_context = open(file).read().splitlines()

    print(file_context)

finally:
    file_object.close()
