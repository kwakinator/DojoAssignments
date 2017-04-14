def odd_even(a, b):
    for num in range(a, b):
        if num %2 ==0:
            result = "even"
        else:
            result = "odd"
        print "Number is {}. This is an {} number".format(num, result)
odd_even(1,2001)



def multiply(arr, num):
    for idx in range(len(arr)):
        arr[idx] *= num
    return arr

c = [2, 4, 10, 16]
b = multiply(c, 5)
print b

def layered_multiples(arr):
  print arr
  new_array = []
  for idx in arr:
      val_arr = []
      for ones in range(0,idx):
          val_arr.append(1)
      new_array.append(val_arr)
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
