import pandas as pd
pd.options.mode.chained_assignment = None
from Funciones.empresa import empresa
import os
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
import time
from datetime import datetime
import numpy as np
import sys

os.system('cls')
while True:
    print('Cargando archivos (Cartera, Base Telefónica, Validador de Teléfonos)...')

    #----------Archivos a cargar CARTERA, BASE TELEFÓNICA Y VALIDAR TELÉFONOS-----------------------#

    cartera = 'REPORTE CARTERAS FINANCIERAS 0606.xlsx'
    base_telefonos = 'TELEFONOS FINANCIERAS 0606.xlsx'
    validar_telefonos = 'Reporte Movilgate 1306.xlsx'
    daily = 'Mas Cobranzas Daily Junio.xlsx'

    #----------------------------------------------------------------------------#

    #----------6. Función Formación Mensaje----------#
    def formacionMensaje(df_m, empresa, edenorEdesur, opcion1):
        documentos = df_m['DOCUMENTO']
        saldos = df_m['DEUDA_VDA'] #Antina Especial

        #Empresas
        empresas = ['FERTIL', 'CONSUMAX',
        'ANTINA COMUN', 'PLENTI TEMPRANA',
        'QIDA TARDIA', 'PLENTI TARDIA', 'TARJETA FARO', 
        'CORDIAL', 'CREDIN', 'CREDITO DEL VALLE (CREDIN)',
        'AQUATRO S.A. (CREDIN)', 'MEJOR CREDITO RECOVERY', 
        'FIAT', 'ANTINA ESPECIAL', 'PRESTI', 'CRISTAL CASH',
        'COOP CUENCA', 'ARGENPESOS', 'ITALCRED', 
        'CLIN CASH', 'ITALCRED MASTERCARD', 'CRED NOW', 'CREDICUOTAS',
        'MOOVITECH', 'MAYCOOP', 'CRED NOW JUDICIAL',
        'QIDA TEMPRANA', 'CREDISOL', 'EDERSA']

        empresas_2 = ['EDESUR', 'EDESUR JUDICIALES','EDENOR', 
        'EDELAP', 'EDEMSA']

        #Links 
        edesur_1 = 'https://bit.ly/3pKqUOX'
        edesur_2 = 'https://bit.ly/3JUtxpG'
        edenor_1 = 'https://bit.ly/3L7KNrP'
        edenor_2 = 'https://bit.ly/3iociRl'
        fertil = 'https://bit.ly/3uDQGWs'
        consumax = 'https://bit.ly/3FyWiqr'
        antina_comun = 'https://bit.ly/36qVFlF' #Antina Común
        plenti = 'https://bit.ly/34Z79Mc'
        qida = 'https://bit.ly/34Z79Mc' #Qida tardía
        tarjeta_faro = 'https://bit.ly/3uDQGWs'
        cordial = 'https://bit.ly/3xrrEgc'
        credin = 'link'
        mejor_credito = 'https://bit.ly/3MKgYhB'
        fiat = 'https://wa.link/6jxxy2'
        antina_especial = 'https://tg.antina.com.ar/pagos/'
        presti = 'link' 
        cristal_cash = 'https://bit.ly/3MWza7M'
        cuenca = 'link'
        argenpesos = 'https://bit.ly/3HM7Rep'
        italcred = 'https://bit.ly/3xF48g1'
        edelap_1 = 'https://bit.ly/3icPpAt'
        edelap_2 = 'https://bit.ly/3uq97OX' 
        edemsa_1 = 'https://bit.ly/3N4L6Fg'
        edemsa_2 = 'https://bit.ly/3jZX0TH'
        clin_cash = 'https://bit.ly/3MWza7M'
        cred_now = 'https://bit.ly/3N07sai'
        credicuotas = 'https://bit.ly/3swx8DR'
        moovitech = 'link'
        maycoop = 'https://bit.ly/3mEgC0W'
        credisol = 'link'
        edersa = 'link'
        
        if empresa == 'EDESUR':
            link_1 = edesur_1
            link_2 = edesur_2
        elif empresa == 'FERTIL':
            link = fertil
        elif empresa == 'CONSUMAX':
            link = consumax
        elif empresa == 'EDENOR':
            link_1 = edenor_1
            link_2 = edenor_2
        elif empresa == 'ANTINA COMUN':
            link = antina_comun
        elif empresa == 'PLENTI TEMPRANA':
            link = plenti
        elif empresa == 'QIDA TARDIA':
            link = qida 
        elif empresa == 'PLENTI TARDIA':
            link = plenti
        elif empresa == 'TARJETA FARO':
            link = tarjeta_faro
        elif empresa == 'CORDIAL':
            link = cordial
        elif empresa == 'CREDIN':
            link = credin
        elif empresa == 'MEJOR CREDITO RECOVERY':
            link = mejor_credito
        elif empresa == 'FIAT':
            link = fiat
        elif empresa == 'ANTINA ESPECIAL':
            link = antina_especial
        elif empresa == 'PRESTI':
            link = presti
        elif empresa == 'CRISTAL CASH':
            link = cristal_cash
        elif empresa == 'COOP CUENCA':
            link = cuenca
        elif empresa == 'ARGENPESOS':
            link = argenpesos
        elif empresa == 'ITALCRED':
            link = italcred 
        elif empresa == 'EDELAP':
            link_1 = edelap_1
            link_2 = edelap_2
        elif empresa == 'EDEMSA':
            link_1 = edemsa_1
            link_2 = edemsa_2
        elif empresa == 'CLIN CASH':
            link = clin_cash
        elif empresa == 'EDESUR JUDICIALES':
            link_1 = edesur_1
            link_2 = edesur_2
        elif empresa == 'ITALCRED MASTERCARD':
            link = italcred 
        elif empresa == 'CRED NOW':
            link = cred_now
        elif empresa == 'CREDICUOTAS':
            link = credicuotas 
        elif empresa == 'MOOVITECH':
            link = moovitech
        elif empresa == 'MAYCOOP':
            link = maycoop
        elif empresa == 'CRED NOW JUDICIAL':
            link = cred_now
        elif empresa == 'QIDA TEMPRANA':
            link = qida 
        elif empresa == 'CREDISOL':
            link = credisol
        elif empresa == 'EDERSA':
            link = edersa

        #1 link general
        if empresa in empresas:
            mensaje_gral = []
            for index, i in enumerate(documentos):    
                mensaje = f'Cliente {i} Regularice de manera urgente su deuda con {empresa}. Escribanos via Whats al {link} MAS Cobranzas S.A.'
                mensaje_gral.append(mensaje)

            df_m['TEXTO'] = mensaje_gral 

            if empresa == 'ANTINA COMUN':
                mensaje_gral = []
                for index, i in enumerate(documentos):    
                    mensaje = f'Deuda ANTINA TELEVISIÓN DIGITAL. Comuníquese para poder pactar un acuerdo de pago Whats {link} MAS Cobranzas S.A.'
                    mensaje_gral.append(mensaje)

                df_m['TEXTO'] = mensaje_gral 

            elif empresa == 'ANTINA ESPECIAL':
                mensaje_gral = []
                for index, i in enumerate(saldos):    
                    mensaje = f'Antina informa que esta proximo al vencimiento de su factura por ${i}. Abone hoy en los centros de pagos habilitados o https://tg.antina.com.ar/pagos/'
                    mensaje_gral.append(mensaje)

                df_m['TEXTO'] = mensaje_gral 
        
        #En empresas con 2 link. General
        elif empresa in empresas_2:
            if empresa == 'EDENOR' or empresa == 'EDESUR':
                if edenorEdesur == 'WHATSAPP':
                    mensajes_wp = []
                    for index, i in enumerate(documentos):
                        #Índices Pares incluyendo el 0 -> m_1 
                        #Índices Impares -> m_2
                        if (index % 2 == 0) or (index == 0):
                            m_1 = f'Cliente Nro {i} Regularice de manera urgente su deuda con {empresa}. Escribanos via Whats al {link_1} MAS Cobranzas S.A.'
                            #m_1 = f'Cliente {i} Mantiene incumplimiento con {empresa}. Llame al 01152170510 o Whats https://bit.ly/3pKqUOX Mas Cobranzas'
                            mensajes_wp.append(m_1)
                        else:
                            m_2 = f'Cliente Nro {i} Regularice de manera urgente su deuda con {empresa}. Escribanos via Whats al {link_2} MAS Cobranzas S.A.'
                            #m_2 = f'Cliente {i} Mantiene incumplimiento con {empresa}. Llame al 01152170510 o Whats https://bit.ly/3JUtxpG Mas Cobranzas'
                            mensajes_wp.append(m_2)

                    df_m['TEXTO'] = mensajes_wp
                
                if edenorEdesur == 'PAGO FACIL':
                    mensajes_pf = []
                    for index, i in enumerate(documentos):  
                        mensaje = f'Cliente Nro {i} Regularice de manera urgente su deuda con {empresa}. Escribanos via Whats al https://bit.ly/3qpZpZb MAS Cobranzas S.A.'  
                        #mensaje = f'Cliente {i} Mantiene incumplimiento con {empresa}. Llame al 01152170510 o ingresa a https://bit.ly/3qpZpZb para el pago de tu servicio.'
                        mensajes_pf.append(mensaje)

                    df_m['TEXTO'] = mensajes_pf 
                    
            elif empresa == 'EDEMSA' or empresa == 'EDELAP':
                mensaje_gral = []
                for index, i in enumerate(documentos):
                    #Índices Pares incluyendo el 0 -> m_1 
                    #Índices Impares -> m_2
                    if (index % 2 == 0) or (index == 0):
                        m_1 = f'Cliente Nro {i} Regularice de manera urgente su deuda con {empresa}. Escribanos via Whats al {link_1} MAS Cobranzas S.A.'
                        #m_1 = f'Cliente {i} Mantiene incumplimiento con {empresa}. Llame al 01152170510 o Whats https://bit.ly/3pKqUOX Mas Cobranzas'
                        mensaje_gral.append(m_1)
                    else:
                        m_2 = f'Cliente Nro {i} Regularice de manera urgente su deuda con {empresa}. Escribanos via Whats al {link_2} MAS Cobranzas S.A.'
                        #m_2 = f'Cliente {i} Mantiene incumplimiento con {empresa}. Llame al 01152170510 o Whats https://bit.ly/3JUtxpG Mas Cobranzas'
                        mensaje_gral.append(m_2)

                df_m['TEXTO'] = mensaje_gral
            
        return df_m

    #----------5. Función Monto----------#
    hoy = datetime.today()
    hoy = str(hoy)
    dia = hoy[8:10]
    mes = hoy[5:7]
    formato = f'{dia}{mes}'

    def monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur):
        while True: 
            os.system('cls')
            print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
            print(f'Tramo de Días de Mora: {desde}-{hasta}')
            print(f'Cantidad de Registros: {df_t.shape[0]}\n')
            print('Filtro por Monto:')
            while True:
                try:
                    desde_monto = int(input('Desde $ '))
                    break
                except:
                    print('Ingresar valor entero')

            while True:
                try:
                    hasta_monto = int(input('Hasta $ '))
                    break 
                except:
                    print('Ingresar valor entero')

            #Error con archivos csv. 
            #Descubrir el error. str int
            #df_t['DEUDA_VDA'] está en str ✔

            #La columna viene con comas, intento pasar a float:
            # df_t['DEUDA_VDA'] = df_t['DEUDA_VDA'].str.replace(',','.')
            # df_t['DEUDA_VDA'] = df_t['DEUDA_VDA'].astype(float) 

            #Hacer la prueba con el daily en csv para ver si toma los valores
            #------------------------------------------------#

            df_m = df_t[(df_t['DEUDA_VDA']>=desde_monto) & (df_t['DEUDA_VDA']<=hasta_monto)]

            #Realizar un excel a este nivel para evaluar dónde se borra el segundo tel del documento 3097868331
            #El siguiente bloque llevarlo al filtro inicial para luego poder filtrar en algún menú de opciones:
            telefonos = list(df_m['TEL NORMALIZADO'])
            df_m = df_m.reset_index(drop=True)
            df_m['TIPO'] = 'x' #Defino nueva columna con valor x
            for index, i in enumerate(telefonos):
                i = str(i)
                if len(i) > 4:
                    if len(i) == 12:
                        df_m['TIPO'][index] = 'FIJO'
                    elif len(i) == 13:
                        df_m['TIPO'][index] = 'CELULAR'

            #df_m.to_excel('df_m luego del monto filtrado.xlsx', index=False)

    #----------------------------------------------------------------------------------------#

            if opcion1 != 'IVR VOZ':
                formacionMensaje(df_m, empresa, edenorEdesur, opcion1)

            if opcion1 == 'IVR VOZ' and opcion_campaña == 'TEL FIJO':
                #df_m = df_m[df_m['TIPO'].str.contains("FIJO", case=False)]
                def ultimos(i):
                    i = str(i)
                    if len(i) > 4:
                        i = i[2:]
                        return int(i)
                df_m['TEL NORMALIZADO']=df_m['TEL NORMALIZADO'].apply(ultimos)

                df_m = df_m[['DOCUMENTO', 'TEL NORMALIZADO']]

                df_m[['tel2', 'tel3', 'tel4', 'tel5', 'dato2', 'dato3', 'dato4', 'dato5']] = np.nan
                df_m.rename(columns = {'DOCUMENTO':'id', 'TEL NORMALIZADO':'tel1', 'TEXTO':'dato1'}, inplace = True)
                df_m.dropna(subset=['tel1'], inplace=True)


            elif opcion1 == 'IVR VOZ' and opcion_campaña == 'CELULAR':
                def ultimos(i):
                    i = str(i)
                    if len(i) > 4:
                        i = i[3:]
                        return int(i)

                df_m['TEL NORMALIZADO']=df_m['TEL NORMALIZADO'].apply(ultimos)

                df_m = df_m[['DOCUMENTO', 'TEL NORMALIZADO']]

                df_m[['tel2', 'tel3', 'tel4', 'tel5', 'dato2', 'dato3', 'dato4', 'dato5']] = np.nan
                df_m.rename(columns = {'DOCUMENTO':'id', 'TEL NORMALIZADO':'tel1', 'TEXTO': 'dato1'}, inplace = True)
                df_m.dropna(subset=['tel1'], inplace=True)

            elif opcion1 == 'IVR VOZ' and opcion_campaña == 'FIJO Y CELULAR':
                def ultimos(i):
                    i = str(i)
                    if len(i) == 12:
                        i = i[2:] #Fijo
                        return int(i)
                    elif len(i) == 13:
                        i = i[3:] #Celular
                        return int(i)

                df_m['TEL NORMALIZADO']=df_m['TEL NORMALIZADO'].apply(ultimos)

                df_m = df_m[['DOCUMENTO', 'TEL NORMALIZADO']]

                df_m[['tel2', 'tel3', 'tel4', 'tel5', 'dato2', 'dato3', 'dato4', 'dato5']] = np.nan
                df_m.rename(columns = {'DOCUMENTO':'id', 'TEL NORMALIZADO':'tel1', 'TEXTO':'dato1'}, inplace = True)
                df_m.dropna(subset=['tel1'], inplace=True)

            elif opcion1 == 'SMS CORTO MOVILGATE':
                df_m = df_m[df_m['TIPO'].str.contains("CELULAR", case=False)]
                df_m = df_m[['DOCUMENTO', 'TEL NORMALIZADO', 'TEXTO']]
                def ultimos(i):
                    i = str(i)
                    if len(i) > 4:
                        i = i[3:]
                        return int(i)
                df_m['TEL NORMALIZADO']=df_m['TEL NORMALIZADO'].apply(ultimos)                
                df_m[['Carrier', 'Fecha desde', 'Fecha hasta']] = np.nan
                df_m.rename(columns = {'DOCUMENTO':'Ref_id_ext', 'TEL NORMALIZADO':'Numero de celular', 'TEXTO':'Texto'}, inplace = True)
                df_m = df_m[['Numero de celular', 'Texto', 'Carrier', 'Ref_id_ext', 'Fecha desde', 'Fecha hasta']]
                df_m.dropna(subset=['Numero de celular'], inplace=True)

            elif opcion1 == 'SMS CORTO TELEPROM':
                df_m = df_m[df_m['TIPO'].str.contains("CELULAR", case=False)]
                df_m = df_m[['DOCUMENTO', 'TEL NORMALIZADO', 'TEXTO']]
                def ultimos(i):
                    i = str(i)
                    if len(i) > 4:
                        i = i[3:]
                        return int(i)
                df_m['TEL NORMALIZADO']=df_m['TEL NORMALIZADO'].apply(ultimos)                
                #df_m['DATO1'] = np.nan
                df_m.rename(columns = {'DOCUMENTO':'DNI', 'TEL NORMALIZADO':'TEL', 'TEXTO':'DATO1'}, inplace = True)
                print(f'columnas: {df_m.columns}')
                df_m = df_m[['DNI', 'TEL', 'DATO1']]
                df_m.dropna(subset=['TEL'], inplace=True)
                
            elif opcion1 == 'SMS LARGO':
                df_m = df_m[df_m['TIPO'].str.contains("CELULAR", case=False)]
                df_m = df_m[['DOCUMENTO', 'TEL NORMALIZADO', 'TEXTO']]
                def ultimos(i):
                    i = str(i)
                    if len(i) > 4:
                        i = i[3:]
                        return int(i)
                df_m['TEL NORMALIZADO']=df_m['TEL NORMALIZADO'].apply(ultimos)                
                df_m[['tel2', 'tel3', 'tel4', 'tel5', 'dato2', 'dato3', 'dato4', 'dato5']] = np.nan
                df_m.rename(columns = {'DOCUMENTO':'id', 'TEL NORMALIZADO':'tel1', 'TEXTO': 'dato1'}, inplace = True)
                df_m = df_m[['id', 'tel1', 'tel2', 'tel3', 'tel4', 'tel5', 'dato1', 'dato2', 'dato3', 'dato4', 'dato5']]
                df_m.dropna(subset=['tel1'], inplace=True)
                
                
    #----------------------------------------------------------------------------------------#
            while True:
                os.system('cls')
                print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                print(f'Tramo de Días de Mora: {desde}-{hasta}')    
                print(f'Tramo de Monto: ${desde_monto}-${hasta_monto}')
                print(f'Cantidad de teléfonos: {df_m.shape[0]}\n')
    
                print('Ingresar una opción: ')
                print('1. Generar Excel')
                print('2. Volver a ingresar Monto')
                print('0. Volver atrás')
                print('')
                respuesta = input('Opción: ')

                if respuesta == '1':                 
                    try:
                        df_m.to_excel(f'./2. Campañas/{opcion1}_{opcion_campaña}_{empresa}_{formato}.xlsx', index=False)
                        os.system('cls')
                        print(f'Cantidad de teléfonos: {df_m.shape[0]}')
                        print('✔ Archivo creado correctamente ✔')
                        print('--------------------------------------------------')
                    except:
                        print('❌ Error al crear el archivo ❌')

                    while True:
                        print('')
                        print('Ingresar una opción: ')
                        print('1. Volver a generar un archivo')
                        print('0. Salir del programa')
                        print('')
                        respuesta = input('Opción: ')

                        if respuesta == '1':
                            os.system('cls')
                            break
                
                        elif respuesta == '0':
                            os.system('cls')
                            time.sleep(0.5)
                            sys.exit()
                        else:
                            print('Respuesta incorrecta')

                    if respuesta == '1':
                        respuesta = 'inicio'
                        break

                elif respuesta == '2':
                    os.system('cls')
                    print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                    break
                elif respuesta == '0':
                    os.system('cls')
                    break
                
                else:
                    os.system('cls')
                    print('Respuesta incorrecta.')

            if respuesta == 'inicio':
                break

        return 'inicio'
    #----------4. Función Estado Positivos----------#
    def estadosPositivos(df, opcion1, opcion2, empresa, opcion_campaña, edenorEdesur):
        os.system('cls')

        while True:
            print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
            df_e = df[df['ESTADO OPERACION'].str.contains("CC-|DD-|EG-|NO-|NQP-|PI-|SE-|ST-|VA-|CA-|PBC-|PF-|DA-|SI-|IC-|RP-|NP-|CO-", case=False)]

            while True:
                print('')
                print('Filtro por Días de Mora: ')
                while True:
                    try:
                        desde = int(input('Desde: '))
                        break
                    except:
                        print('Ingresar valor entero')

                while True:
                    try:
                        hasta = int(input('Hasta: '))
                        break 
                    except:
                        print('Ingresar valor entero')
        
                df_t = df_e[(df_e['DIAS_ATRASO']>=desde) & (df_e['DIAS_ATRASO']<=hasta)]

                while True:
                    os.system('cls')
                    print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                    print(f'Tramo de Días de Mora: {desde}-{hasta}')
                    print(f'Cantidad de Registros: {df_t.shape[0]}\n')
                    print('Ingresar una opción:')
                    print('1. Continuar filtrando por Monto')
                    print('2. Volver a ingresar Días de Mora')
                    print('0. Volver atrás')
                    print('')
                    respuesta = input('Opción: ')

                    if respuesta == '1':
                        monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) #Excel filtrado por dias de mora
                    elif respuesta == '2':
                        os.system('cls')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        break
                    elif respuesta == '0':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Respuesta incorrecta.')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        print(f'Tramo de días: {desde}-{hasta}\n')    
                if respuesta == '0':
                    break
            break

        if monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) == 'inicio':
            return 'inicio'

    #----------4. Función Estado Negativos----------#
    def estadosNegativos(df, opcion1, opcion2, empresa, opcion_campaña, edenorEdesur):
        os.system('cls')

        while True:
            print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
            df_e = df[df['ESTADO OPERACION'].str.contains("EG-|NC-|SG-", case=False)]

            while True:
                print('')
                print('Filtro por Días de Mora: ')
                while True:
                    try:
                        desde = int(input('Desde: '))
                        break
                    except:
                        print('Ingresar valor entero')

                while True:
                    try:
                        hasta = int(input('Hasta: '))
                        break 
                    except:
                        print('Ingresar valor entero')
                df_t = df_e[(df_e['DIAS_ATRASO']>=desde) & (df_e['DIAS_ATRASO']<=hasta)]

                while True:
                    os.system('cls')
                    print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                    print(f'Tramo de Días de Mora: {desde}-{hasta}')
                    print(f'Cantidad de Registros: {df_t.shape[0]}\n')
                    print('Ingresar una opción:')
                    print('1. Continuar filtrando por Monto')
                    print('2. Volver a ingresar Días de Mora')
                    print('0. Volver atrás')
                    print('')
                    respuesta = input('Opción: ')

                    if respuesta == '1':
                        monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) #Excel filtrado por dias de mora
                        
                    elif respuesta == '2':
                        os.system('cls')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        break
                    elif respuesta == '0':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Respuesta incorrecta.')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        print(f'Tramo de días: {desde}-{hasta}\n')    
                if respuesta == '0':
                    break
            break

        if monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) == 'inicio':
            return 'inicio'
    #----------4. Función Estado SG----------#
    def estadosSg(df, opcion1, opcion2, empresa, opcion_campaña, edenorEdesur):
        os.system('cls')

        while True:
            print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
            df_e = df[df['ESTADO OPERACION'].str.contains("SG-", case=False)]

            while True:
                print('')
                print('Filtro por Días de Mora: ')
                while True:
                    try:
                        desde = int(input('Desde: '))
                        break
                    except:
                        print('Ingresar valor entero')

                while True:
                    try:
                        hasta = int(input('Hasta: '))
                        break 
                    except:
                        print('Ingresar valor entero')

                df_t = df_e[(df_e['DIAS_ATRASO']>=desde) & (df_e['DIAS_ATRASO']<=hasta)]

                while True:
                    os.system('cls')
                    print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                    print(f'Tramo de Días de Mora: {desde}-{hasta}')
                    print(f'Cantidad de Registros: {df_t.shape[0]}\n')
                    print('Ingresar una opción:')
                    print('1. Continuar filtrando por Monto')
                    print('2. Volver a ingresar Días de Mora')
                    print('0. Volver atrás')
                    print('')
                    respuesta = input('Opción: ')

                    if respuesta == '1':
                        monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) #Excel filtrado por dias de mora
                        
                    elif respuesta == '2':
                        os.system('cls')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        break
                    elif respuesta == '0':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Respuesta incorrecta.')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        print(f'Tramo de días: {desde}-{hasta}\n')    
                if respuesta == '0':
                    break
            break

        if monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) == 'inicio':
            return 'inicio'
    #----------4. Función Estados TODOS----------#
    def estadosTodos(df, opcion1, opcion2, empresa, opcion_campaña, edenorEdesur):
        os.system('cls')

        while True:
            print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
            df_e = df[df['ESTADO OPERACION'].str.contains("CC-|DD-|EG-|NO-|NQP-|PI-|SE-|ST-|VA-|CA-|PBC-|PF-|DA-|SI-|IC-|RP-|NP-|CO-|NC-|SG-", case=False)]

            while True:
                print('')
                print('Filtro por Días de Mora: ')
                while True:
                    try:
                        desde = int(input('Desde: '))
                        break
                    except:
                        print('Ingresar valor entero')

                while True:
                    try:
                        hasta = int(input('Hasta: '))
                        break 
                    except:
                        print('Ingresar valor entero')
                df_t = df_e[(df_e['DIAS_ATRASO']>=desde) & (df_e['DIAS_ATRASO']<=hasta)]

                while True:
                    os.system('cls')
                    print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                    print(f'Tramo de Días de Mora: {desde}-{hasta}')
                    print(f'Cantidad de Registros: {df_t.shape[0]}\n')
                    print('Ingresar una opción:')
                    print('1. Continuar filtrando por Monto')
                    print('2. Volver a ingresar Días de Mora')
                    print('0. Volver atrás')
                    print('')
                    respuesta = input('Opción: ')

                    if respuesta == '1':
                        monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) #Excel filtrado por dias de mora
                        
                    elif respuesta == '2':
                        os.system('cls')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        break
                    elif respuesta == '0':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Respuesta incorrecta.')
                        print(f'-----------------{opcion_campaña} -> {empresa} -> {opcion1} -> {opcion2}---------------')
                        print(f'Tramo de días: {desde}-{hasta}\n')    
                if respuesta == '0':
                    break
            break

        if monto(df_t, opcion1, opcion2, desde, hasta, empresa, opcion_campaña, edenorEdesur) == 'inicio':
            return 'inicio'
    
    #----------3. Función Estados----------#
    def estados(df, opcion_principal, empresa, opcion_campaña, edenorEdesur):
        os.system('cls')
        while True:
            print(f'----------{opcion_campaña} -> {empresa} -> {opcion_principal}----------')
            print('')
            print('Filtro por Estado De Operación: ')
            print('1. Estados Positivos')
            print('2. Estados Negativos')
            print('3. SG')
            print('4. Todos')
            print('0. Para volver al Menú Principal')
            print('')
            respuesta = input('Opción: ')

            if respuesta == '1':
                os.system('cls')
                opcion_estados = 'ESTADOS POSITIVOS'
                estadosPositivos(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur)
                
            elif respuesta == '2':
                os.system('cls')
                opcion_estados = 'ESTADOS NEGATIVOS'
                estadosNegativos(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur)
                
            elif respuesta == '3':
                os.system('cls')
                opcion_estados = 'ESTADOS SG'
                estadosSg(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur)
                
            elif respuesta == '4':
                os.system('cls')
                opcion_estados = 'TODOS LOS ESTADOS'
                estadosTodos(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur)
                
            elif respuesta == "0":
                os.system('cls')
                break
            else:
                os.system('cls')
                print('Opción incorrecta. Ingrese una Opción válida.\n')

        if estadosPositivos(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur) == 'inicio' or estadosNegativos(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur) == 'inicio' or estadosSg(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur) == 'inicio' or estadosTodos(df, opcion_principal, opcion_estados, empresa, opcion_campaña, edenorEdesur) == 'inicio':
            return 'inicio'
        
    
    #----------2. Función Menú Principal----------#
    def menuPrincipal(empresa, cod, daily, df_c, df_t, opcion_campaña, edenorEdesur): 
    
        while True:
            os.system('cls')
            print('Filtrando por Código de Empresa...')
            cod_empresa = f'{cod}-'
            df_c = df_c[df_c['COMPANIA'].str.contains(cod_empresa, case=False)]
            #df_c.to_excel('df_c filtrado por compania.xlsx', index=False)

            df_t['COMPANIA'] = df_t['COMPANIA'].astype(str)
            df_t = df_t[df_t['COMPANIA'].str.contains(cod, case=False)]
            #df_t.to_excel('df_t filtrado por compania.xlsx', index=False)

            df_c.rename(columns={'NRO_ DOC':'DOCUMENTO'}, inplace=True) #Renombro columna para hacer merge

            print('Uniendo Cartera y Base de Teléfonos...')
            df_merge = pd.merge(left=df_c, right=df_t, how='left', on='DOCUMENTO')

            #df_merge.to_excel('df_merge.xlsx', index=False)

            df_merge = df_merge.reset_index(drop=True) 
            df_merge['FECHA ULT.TRAM.'] = df_merge['FECHA ULT.TRAM.'].fillna('-') #fillna por -

            df_merge.dropna(subset=['TIPOCARGA'], inplace=True) #Elimino los registros que no me sirven (no tienen tel)
            df_merge.drop_duplicates(subset=['TEL NORMALIZADO'], inplace=True) #Elimino los registros con números repetidos
            df_merge.reset_index(drop=True, inplace=True) #Reinicio los índices

            #df_merge.to_excel('df_merge.xlsx', index=False)

            documentos = df_merge['DOCUMENTO']
            
            contador=0
            for indice, i in enumerate(documentos):
                if indice > 0 and indice < (len(documentos)-1):
                    if i == df_merge['DOCUMENTO'][indice+1]:
                        contador+=1
                    else:
                        contador=0
                    
                    if contador >= 2:
                        df_merge = df_merge.drop([indice], axis=0)

            #----------------Filtrar por Daily--------------#
            print('Cargando Daily...')
            df_daily = pd.read_excel(f'1. Archivos a cargar/{daily}', sheet_name='Pagos')
            #df_daily = pd.read_csv(f'1. Archivos a cargar/{daily}', sep=';', encoding='latin-1', low_memory=False)

            print('Filtrando registros del Daily...')
            lista_d = list(df_daily['DOCUMENTO'])
            lista_m = list(df_merge['DOCUMENTO'])

            lista_match = []
            for i in lista_d:
                if i in lista_m:
                    lista_match.append(i)

            df_dicc = pd.DataFrame({'docs':lista_match})
            #unicos = df_dicc['docs'].unique()
            lista_unicos = list(df_dicc['docs'].unique())

            df_merge["DOCUMENTO"] = df_merge["DOCUMENTO"].astype(str)
            for i in lista_unicos:
                if i in lista_m:
                    i = str(i)
                    df_merge = df_merge[df_merge["DOCUMENTO"].str.contains(i) == False]

            df_merge["DOCUMENTO"] = df_merge["DOCUMENTO"].astype('int64')

            df_merge.to_excel('Filtro por Daily.xlsx', index=False)
            
            #---------------------------------------------------------------#
            print('')
            print('Preparando programa...')
            df = pd.read_excel('Filtro por Daily.xlsx')


            os.system('cls')
            print(f'-------------Menú Principal - {opcion_campaña} -> {empresa}-------------')
            print('')
            print('Ingresar una opción:')
            print('1. IVR VOZ')
            print('2. SMS CORTO MOVILGATE')
            print('3. SMS CORTO TELEPROM')
            print('4. SMS LARGO')
            print('0. Para ingresar otro Código de Empresa')
            print('')
            n = input('Opción: ')
            
            if n == '1':
                os.system('cls')
                opcion_principal = 'IVR VOZ'
                estados(df, opcion_principal, empresa, opcion_campaña, edenorEdesur)
                
            elif n == '2':
                os.system('cls')
                opcion_principal = 'SMS CORTO MOVILGATE'
                estados(df, opcion_principal, empresa, opcion_campaña, edenorEdesur)

            elif n == '3':
                os.system('cls')
                opcion_principal = 'SMS CORTO TELEPROM'
                estados(df, opcion_principal, empresa, opcion_campaña, edenorEdesur)
                
            elif n == '4':
                os.system('cls')
                opcion_principal = 'SMS LARGO'
                estados(df, opcion_principal, empresa, opcion_campaña, edenorEdesur)

            elif n == '0':
                os.system('cls')
                break

            else: 
                os.system('cls')
                print('Opción incorrecta. Ingrese una Opción válida.\n')
        
        if estados(df, opcion_principal, empresa, opcion_campaña, edenorEdesur) == 'inicio':
            return 'inicio'

    #----------1. Función Empresa----------#
    lista_codigos = ['45', 'EDESUR', '49', 'FERTIL', '50', 'CONSUMAX',
    '52', 'EDENOR', '57', 'ANTINA COMUN', '59', 'PLENTI TEMPRANA',
    '60', 'QIDA TARDIA', '61', 'PLENTI TARDIA', '62', 'TARJETA FARO', 
    '63', 'CORDIAL', '64', 'CREDIN', '65', 'CREDITO DEL VALLE (CREDIN)',
    '66', 'AQUATRO S.A. (CREDIN)', '67', 'MEJOR CREDITO RECOVERY', 
    '75', 'FIAT', '76', 'ANTINA ESPECIAL', '78', 'PRESTI', '79', 'CRISTAL CASH',
    '80', 'COOP CUENCA', '86', 'ARGENPESOS', '89', 'ITALCRED', '94', 'EDELAP', 
    '95', 'EDEMSA', '96', 'CLIN CASH', '97', 'EDESUR JUDICIALES',
    '99', 'ITALCRED MASTERCARD', '100', 'CRED NOW', '103', 'CREDICUOTAS',
    '104', 'MOOVITECH', '105', 'MAYCOOP', '106', 'CRED NOW JUDICIAL',
    '107', 'QIDA TEMPRANA', '108', 'CREDISOL', '110', 'EDERSA']

    def empresa(daily, df_c, df_t, opcion_campaña):
        while True:
            os.system('cls')
            print(f'-------------Empresa - {opcion_campaña}------------')
            cod = input('Ingresar Código de Empresa o 0 para volver atrás: ')

            if cod in lista_codigos:
                for index, i in enumerate(lista_codigos):
                    if cod == i:
                        empresa = lista_codigos[index+1] 

                while True:
                    os.system('cls')
                    print(f'-------------Campaña {opcion_campaña}------------')
                    print(f'Empresa: {empresa}\n')
                    print('1. Continuar')
                    print('0. Volver a ingresar el Código de Empresa')
                    print('')
                    n = input('Opción: ')

                    if n == '1':
                        edenorEdesur = ''
                        if empresa == 'EDENOR' or empresa == 'EDESUR':
                            while True:
                                os.system('cls')
                                print(f'-----------------{opcion_campaña} -> {empresa}---------------')
                                print('')
                                print('Ingresar una opción:')
                                print('1. Link Whatsapp')
                                print('2. Link Pago Fácil')
                                print('3. Sin Link (IVR VOZ)')
                                print('0. Volver atrás')
                                print('')
                                mensaje = input('Opción: ')

                                if mensaje == '1':
                                    edenorEdesur = 'WHATSAPP'
                                    menuPrincipal(empresa, cod, daily, df_c, df_t, opcion_campaña, edenorEdesur)
            
                                elif mensaje == '2':
                                    edenorEdesur = 'PAGO FACIL'
                                    menuPrincipal(empresa, cod, daily, df_c, df_t, opcion_campaña, edenorEdesur)
            
                                elif mensaje == '3':
                                    edenorEdesur = ''
                                    menuPrincipal(empresa, cod, daily, df_c, df_t, opcion_campaña, edenorEdesur)
            
                                elif mensaje == '0':
                                    os.system('cls')
                                    break
                        else:
                            menuPrincipal(empresa, cod, daily, df_c, df_t, opcion_campaña, edenorEdesur)

                    elif n == '0':
                        os.system('cls')
                        break
                    else: 
                        os.system('cls')
                        print('Opción incorrecta. Ingrese una Opción válida.\n')
                                        
            elif cod == '0':
                os.system('cls')
                break
            else: 
                os.system('cls')
                print('El valor ingresado no corresponde a un Código de Compañía. Ingrese una opción válida.\n')

        if menuPrincipal(empresa, cod, daily, df_c, df_t, opcion_campaña, edenorEdesur) == 'inicio':
            pass


    #----------------------------------------------------------------------------------#
    df_c = pd.read_excel(f'1. Archivos a cargar/{cartera}', usecols=['NRO_ DOC', 'NOMBRE', 'DEUDA_VDA', 'DIAS_ATRASO', 'ESTADO OPERACION', 'FECHA ULT.TRAM.', 'COMPANIA'])
    #df_c = pd.read_csv(f'1. Archivos a cargar/{cartera}', sep=';', encoding='latin-1', usecols=['NRO_ DOC', 'NOMBRE', 'DEUDA_VDA', 'DIAS_ATRASO', 'ESTADO OPERACION', 'FECHA ULT.TRAM.', 'COMPANIA'], low_memory=False)
    print('')
    print('Carga de Cartera OK')
    df_t = pd.read_excel(f'1. Archivos a cargar/{base_telefonos}', usecols=['DOCUMENTO', 'OPERADOR', 'TIPOCARGA', 'ESTADO', 'TEL NORMALIZADO', 'COMPANIA'])
    #df_t = pd.read_csv(f'1. Archivos a cargar/{base_telefonos}', sep=';', encoding='latin-1', usecols=['DOCUMENTO', 'OPERADOR', 'TIPOCARGA', 'ESTADO', 'TEL NORMALIZADO', 'COMPANIA'], low_memory=False)
    print('Carga de Base Telefónica OK')
    df_v = pd.read_excel(f'1. Archivos a cargar/{validar_telefonos}', usecols=['Teléfono', 'Estado'])
    #df_v = pd.read_csv(f'1. Archivos a cargar/{validar_telefonos}', sep=';', encoding='latin-1', usecols=['Teléfono', 'Estado'], low_memory=False)
    print('Carga de Validador de Teléfonos OK')
    print('')
    print('Preparando programa...')

    #--------------------------Bloque nuevo------------------------------#
    telefonos = list(df_t['TEL NORMALIZADO'])
    #df_t = df_t.reset_index(drop=True)
    df_t['TIPO'] = 'x' #Defino nueva columna con valor x
    for index, i in enumerate(telefonos):
        i = str(i)
        if len(i) > 4:
            if len(i) == 14:
                df_t['TIPO'][index] = 'FIJO' #A los números de largo 14 les defino el valor FIJO
            elif len(i) == 15:
                df_t['TIPO'][index] = 'CELULAR' #A los números de largo 15 les defino el valor CELULAR
    #---------------------------------------------------------------------#

    #Primer filtro. Todos los Estados de Operación necesarios. Filtros para luego mergear
    df_c['ESTADO OPERACION'] = df_c['ESTADO OPERACION'].astype(str) #Evitar error al detectar NaN
    df_c = df_c[df_c['ESTADO OPERACION'].str.contains("CC-|DD-|EG-|NC-|NO-|NQP-|PI-|SE-|SG-|ST-|VA-|CA-|PBC-|PF-|DA-|SI-|IC-|RP-|NP-|CO-", case=False)]
    #Filtro por TIPOCARGA --> Todo menos "baja"
    df_t = df_t[~df_t['TIPOCARGA'].str.contains("BAJA", case=False, na=False)]
    #Filtro por ESTADO --> Todo menos "Inválido" y "No contactado"
    df_t = df_t[~df_t['ESTADO'].str.contains("INVALIDO|NO CONTACTADO", case=False, na=False)]
    #Generar el archivo con la columna TIPO con los valores de FIJO Y CELULAR
    #df_t.to_excel('Filtro por columna TIPO.xlsx', index=False)
    #----------------------------------------------------------------------#

    #Filtro para el Validador de Teléfonos:
    #Sólo mantengo los números que NO fueron recibidos (~MT_DELIVERED)

    #--------------------df_n--------------------#
    #Sólo mantengo los números que NO fueron recibidos (~MT_DELIVERED)
    df_n = df_v[~df_v['Estado'].str.contains("MT_DELIVERED", case=False)]
    #print(f'Registros de teléfonos negativos: {df_n.shape[0]}')
    df_n = pd.DataFrame(df_n['Teléfono']) #Del df_n sólo quiero la columna de Teléfono

    df_t.rename(columns = {'TEL NORMALIZADO':'Teléfono'}, inplace = True) #Cambiar nombre de col para concatenar

    #----------Archivo Concatenado----------#
    df_t = pd.concat([df_n, df_t]) #Concatenar los negativos con los telefonos
    #print(f'Cantidad de registros del df_concatenado: {df_concatenado.shape[0]}')
    #Borro los tel duplicados (negativos) quedando los válidos
    df_t.drop_duplicates(inplace=True, subset=['Teléfono']) 
    #print(df_concatenado.columns)
    df_t.dropna(subset=['DOCUMENTO'], inplace=True)
    #print(f'Cantidad final de registros sin negativos: {df_t.shape[0]}')

    df_t.rename(columns = {'Teléfono':'TEL NORMALIZADO'}, inplace = True) #Cambiar nombre de col para concatenar
    #-----#

    os.system('cls')
    print('-------------Campaña-------------')
    print('')
    print('Ingresar una opción:')
    print('1. Celular')
    print('2. Teléfono Fijo')
    print('3. Teléfono Fijo y Celular')
    print('0. Salir del programa')
    print('')
    n = input('Opción: ')

    if n == '1':
        df_t = df_t[df_t['TIPO'].str.contains("CELULAR", case=False)]
        opcion_campaña = 'CELULAR'
        empresa(daily, df_c, df_t, opcion_campaña) #Nombre del daily, df cartera, df telefono
    elif n == '2':
        df_t = df_t[df_t['TIPO'].str.contains("FIJO", case=False)]
        opcion_campaña = 'TEL FIJO'
        empresa(daily, df_c, df_t, opcion_campaña) #Nombre del daily, df cartera, df telefono
    elif n == '3':
        #Sólo para IVR VOZ
        opcion_campaña = 'FIJO Y CELULAR'
        empresa(daily, df_c, df_t, opcion_campaña)
    elif n == '0':
        os.system('cls')
        break
    else: 
        os.system('cls')
        print('Opción incorrecta. Ingrese una Opción válida.\n')