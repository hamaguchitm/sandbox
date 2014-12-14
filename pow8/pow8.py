#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback

def pow8_1(a, x, max):
  # 指数を1ずつ減らす再帰関数
  if x < 1:
    return 1
  else:
    if not a < max:
      a = a % max
    
    return (a * pow8_1(a, x - 1, max)) % max

def pow8(a, x, max):
  # 指数を1/2にする再帰関数
  if x < 1:
    return 1
  elif x == 1:
    return a % max
  else:
    if not a < max:
      a = a % max

    p1 = pow8(a, x / 2, max)
    p2 = pow8(a, x % 2, max)

    return p1 * p1 * p2 % max

if __name__ == "__main__":
  
  max = 100000000
  try:
    if len(sys.argv) == 4 and sys.argv[1] == "-i":
      # 確認用：a, x を引数に渡し、a^x を得る
      a = int(sys.argv[2])
      x = int(sys.argv[3])
      
      print sys.argv[2] + "^" + sys.argv[3] + " = " + str(pow8(a, x, max))

    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
      # 回答用：ファイルを入力として受け取り、ファイル内の数字ペアを順に処理する
 
      f = open(sys.argv[2], "r")
      
      for line in f:
        nums = line.replace("\n", "").split(" ")
        a = int(nums[0])
        x = int(nums[1])
        if a == 0 and x == 0:
          continue
        else:
          print pow8(a, x, max)
    else:
      print "usage: " + sys.argv[0] + " -i <a> <x>"
      print "usage: " + sys.argv[0] + " -f <filename>"

  except:
    print traceback.format_exc(sys.exc_info()[2])
