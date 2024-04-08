import covid
virus = covid()
x = input('Enter the Country Name : ')
cases=virus.get_status_by_country_name(x)
for x in cases:
   print(x,':',cases[x])                       #pip install covid
