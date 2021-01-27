import random
size(300, 300)
for x in range(20):
  for y in range(30):
    print(x, y)
    fill(x/10, y/10, 1, 0.5)
    if random.random() > 0.5:
      rect(30*x, 40*y, 20, 20)
    else:
      oval(30*x, 30*y, 20, 20)
      
      saveImage("/Users/squacks/Desktop/myImage.svg")