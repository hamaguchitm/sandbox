#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback

def make_list(n, m):
    # nをm分割した長さmのリストの配列を返す
    if m == 1:
        return [[n]]
    else:
        lists = []
        for i in range(n + 1):
            sub_lists = make_list(n - i, m - 1)

            for list in sub_lists:
                list.append(i)

            lists += sub_lists

        return lists
    

if __name__ == "__main__":

    if len(sys.argv) > 2:
        total_price = int(sys.argv[1])

        stamp_prices = []
        for i in range(2, len(sys.argv)):
          stamp_prices.append(int(sys.argv[i]))

        count = 1
        answer_list = []
        
        while len(answer_list) == 0 and count <= total_price:
            
            count_list = make_list(count, len(stamp_prices))

            for list in count_list:
                price = 0
                for i in range(len(list)):
                    price += stamp_prices[i] * list[i]

                if price == total_price:
                    answer_list.append(list)

            count += 1

        for answer in answer_list:
            print answer
                          
            
            
