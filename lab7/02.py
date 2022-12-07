try:
    tf = open(f"f1.txt", "r")
except FileNotFoundError as ex:
    print("Couldnt open file")
    print(str(ex))
except OSError:
    print("OS couldnt open the file")
else:
    f1 = tf.read()
    tf.close()
finally:
    print("Always executed")