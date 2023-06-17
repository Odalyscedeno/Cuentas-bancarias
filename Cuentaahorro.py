de  cuenta  import  Cuenta_Bancaria

clase  Cuenta_ahorro ( Cuenta_Bancaria ):
    def  _init_ ( self , interes : float =  0 , numero =  None , nombrepropietario =  None , saldo : float = 0 ):
        uno mismo _interés  =  interés
        súper ( Cuenta_ahorro , autoservicio ). _init_ ( numero = numero , nombrepropietario = nombrepropietario , saldo = saldo )

        @ propiedad
        def  interes ( auto ):
            devolverse  a uno mismo . _interes

        @ interés . setter
        def  interés ( auto , interés ):
            uno mismo _interés  =  interés


        def  pagar_interes ( self ):
            uno mismo _saldo  =  yo . _saldo  + (( float ( self . _saldo ) *  int ( self . _interes )) / 100 )
            devolverse  a uno mismo . _saldo
si  _nombre_  ==  '_principal_' :
            Cuentas_ahorros  =  Cuenta_ahorro ( 5 , '0930651690' , 'odalys' , '540' )

            Cuentas_ahorros . mostrar_saldo ()
            Cuentas_ahorros . crédito ( 2400 )

            Cuentas_ahorros . mostrar_saldo ()
            Cuentas_ahorros . débito ( 600 )

            imprimir ( Cuentas_ahorros )
