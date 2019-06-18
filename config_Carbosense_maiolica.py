# for Maiolica Swiss inventory, unit m, x is easterly, y is northly
input_path = "/project/jae/MaiolicaSynthesisCH4"
ch_xn = 704 
ch_yn = 442
ch_xll = 484000
ch_yll = 75000
ch_cell = 500
nodata_value = -9999

origin = 'maiolica'
gridname = origin + '_CH4_1km'

species = ['CH4']

ch_cat = ['ara', 'dep_scaled', 'forest', 'gas_scaled', 'lakes', 'lwi_scaled',
           'wetlands', 'wildanimals']






year = 2018

output_path ="./testdata"

offline=False

# Carbosense COSMO-1 Domain
dx = 0.01
dy = 0.01
pollon = -170.0
pollat = 43.0
xmin = -4.92
ymin = -3.18
nx = 900
ny = 600

if offline:
    xmin -= 2 * dx
    ymin -= 2 * dy
    nx += 4
    ny += 4

# Don't scale for CH4 (i.e., use time and height constant category 'I')
mapping = { 'ara': 'I', 
            'dep_scaled': 'I',
            'forest': 'I',
            'gas_scaled': 'I',
            'lakes': 'I',
            'lwi_scaled': 'I',
            'wetlands': 'I',
            'wildanimals': 'I',
          }