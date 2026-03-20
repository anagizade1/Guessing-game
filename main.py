def toplama(a,b):
    return a+b
def vurma(a,b):
    return a * b
def bolme(a,b):
    return a/b
def cixma(a,b):
    return a - b

def main():
    while True: 
    
      print('toplamaq ucun 1 ')
      print('cixma ucun 2 ')
      print('bolme ucun 3 ')
      print('vurma ucun 4 ')
      print('cixmaq ucun 5 e basin: ')
      choice=int(input("mentiqi emeli secin: "))
      if choice == 5:
            print('sagolun')
            break
      if choice not in [1, 2, 3, 4]:
          print('zehmet olmasa duzgun reqemi daxil edin: ')
          continue
      a=int(input('1 ci ededi daxil edin: '))

      b=int(input('2 ci ededi daxil edin: '))
      
      if choice == 1:
           print('cavab', toplama(a,b))
      elif choice == 2:
           print("cavab: ", cixma(a,b))
      elif choice == 3:
           print('cavab: ', bolme(a,b) )
      elif choice == 4:
           print('cavab: ', vurma(a,b))

main()
          


     


        