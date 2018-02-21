import pyexcel

dic_list = [
    { "title": '1981',
    'link': 'http://www.clueless.much',

    }
]

pyexcel.save_as(records= dic_list, dest_file_name = 'excel.xlsx')
