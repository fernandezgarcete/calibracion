import os

__author__ = 'Juanjo'

from os.path import expanduser, sep

# lectura de los 4 archivos
def leer(urix1, urix2, uriy1, uriy2):
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    wl = []
    with open(urix1, 'r') as fx1:
        l = fx1.readline().split('\t')
        if l[0] == 'Wavelength':
            for line in fx1:
                try:
                    ref = line.split('\t')
                    wl.append(int(ref[0]))
                    x1.append(float(ref[1].replace(',', '.')))
                except:
                    x1 = 'error-'+urix1
                    return wl, x1, x2, y1, y2
        else:
            x1 = 'error-'+urix1
            return wl, x1, x2, y1, y2
    with open(urix2, 'r') as fx2:
        l = fx2.readline().split('\t')
        if l[0] == 'Wavelength':
            try:
                for line in fx2:
                    ref = line.split('\t')
                    x2.append(float(ref[1].replace(',', '.')))
            except:
                x2 = 'error-'+urix2
                return wl, x1, x2, y1, y2
        else:
            x2 = 'error-'+urix2
            return wl, x1, x2, y1, y2
    with open(uriy1, 'r') as fy1:
        l = fy1.readline().split('\t')
        if l[0] == 'Wavelength':
            for line in fy1:
                try:
                    ref = line.split('\t')
                    y1.append(float(ref[1].replace(',', '.')))
                except:
                    y1 = 'error-'+uriy1
                    return wl, x1, x2, y1, y2
        else:
            y1 = 'error-'+uriy1
            return wl, x1, x2, y1, y2
    with open(uriy2, 'r') as fy2:
        l = fy2.readline().rsplit('\t')
        if l[0] == 'Wavelength':
            for line in fy2:
                try:
                    ref = line.split('\t')
                    y2.append(float(ref[1].replace(',', '.')))
                except:
                    y2 = 'error-'+uriy2
                    return wl, x1, x2, y1, y2
        else:
            y2 = 'error-'+uriy2
            return wl, x1, x2, y1, y2
    return wl, x1, x2, y1, y2


# funcion lineal f(y) = (a*x)+b
# pendiente a = (y2-y1)/(x2-x1)
# ordenada b = y1-(a*x1)
def corregir(wl, x1, x2, y1, y2):
    a = []
    b = []
    cor1 = []
    cor2 = []
    # Obtengo la pendiente
    for i, j in enumerate(wl):
        a.append((y2[i]-y1[i])/(x2[i]-x1[i]))
    # Con la pendiente obtengo la ordenada
    for i, j in enumerate(wl):
        b.append(y1[i]-(a[i]*x1[i]))
    # Con la pendiente y la ordenada aplico la funcion lineal para corregir
    for i, j in enumerate(wl):
        cor1.append((a[i]*x1[i])+b[i])
        cor2.append((a[i]*x2[i])+b[i])
    return cor1, cor2, a, b


# Crea los archivos con los nuevos valores
def crear_archivo(wl, cor1, cor2, nom1, nom2, pends, ords):
    desk = expanduser('~') + '\Desktop'
    with open(desk + sep + nom1 + '-Calibrado.txt', 'a') as c1:
        c1.write('Wavelength\tValor Corregido\n')
        for i, j in enumerate(wl):
            c1.write(str(wl[i])+'\t'+str(cor1[i])+'\n')
    with open(desk + sep + nom2 + '-Calibrado.txt', 'a') as c2:
        c2.write('Wavelength\tValor Corregido\n')
        for i, j in enumerate(wl):
            c2.write(str(wl[i])+'\t'+str(cor2[i])+'\n')

    # escribimos el archivo pendientes
    if os.path.isfile(desk + sep + 'pendientes-a.txt'):
        # leer lineas en un array
        lineas_aux = []
        with open(desk + sep + 'pendientes-a.txt', 'r') as a:
            lineas = a.readlines()
        # agrega contenido a cada linea
        for i, j in enumerate(wl):
            if i == 0:
                lineas_aux.append(lineas[0].split('\n')[0] + '\ta\n')
            else:
                lineas_aux.append(lineas[i].split('\n')[0] + '\t' + str(pends[i]) + '\n')
        # sobreescribe el contenido antiguo de cada linea con el nuevo
        with open(desk + sep + 'pendientes-a.txt', 'w') as a:
            a.write("".join(lineas_aux))
    else:
        with open(desk + sep + 'pendientes-a.txt', 'a') as a:
            a.write('Wavelength\ta\n')
            for i, j in enumerate(wl):
                a.write(str(wl[i]) + '\t' + str(pends[i]) + '\n')
