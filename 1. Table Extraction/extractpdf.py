import camelot

tables = camelot.read_pdf('table.pdf', pages='1', flavor='lattice')
print(tables)
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')  # converting table0 to a csv file
