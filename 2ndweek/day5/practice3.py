#!/usr/bin/env python


# 1 이라는 객체가 int 또는  str 인가?
out0 = isinstance(1, (int, str))

#'aaa' 라는 객체가 int 또는 str 인가?
out1 = isinstance('aaa', (int,str))


print (out0, out1)
