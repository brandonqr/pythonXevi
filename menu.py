#encoding:utf-8
import os
from exercicis import *
def main_menu():
  os.system('clear')
  print "1.--------------"
  print "2.Random Classic"
  print "3.Salir"
  print "-------------"
  opcio=raw_input(">>")
  if opcio=='1':
    exercici1()
  elif opcio=='2':
    exercici2()
  elif opcio='3':
    return
  else:
    print "Error."
