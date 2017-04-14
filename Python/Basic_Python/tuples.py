def tuple_output(dict):
    info = []
    for key, data in dict.iteritems():
        info.append((key,data))
    print info

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

tuple_output(my_dict)
