de  cuenta  import  Cuenta_Bancaria

clase  Cuenta_corriente ( Cuenta_Bancaria ):

    def  _init_ ( self , numero =  Ninguno , nombrepropietario =  Ninguno , saldo : float =  0 , tiene_cheque = bool ):
        uno mismo _tiene_cheque =  tiene_cheque
        súper ( Cuenta_corriente , auto ). _init_ ( numero = numero , nombrepropietario = nombrepropietario , saldo = saldo )

    @ propiedad
    def  tiene_cheque ( auto ):
        devolverse  a uno mismo . _tiene_cheque

    @tiene_cheque . _ setter
    def  tiene_cheque ( self , tiene_cheque ):
        uno mismo _tiene_cheque  =  tiene_cheque
        devolverse  a uno mismo . _saldo

    def  pagar_cheque ( auto ):
        uno mismo _saldo  =  yo . _saldo  + (( float ( self . _saldo ) -  int ( self . _pago_cheque )))
        devolverse  a uno mismo . _saldo

si  _nombre_ == '_principal_' :
    Cuentas_corrientes  =  Cuenta_corriente ( '0930651690' , 'odalys' , '540' , bool )

    Cuentas_corrientes . mostrar_saldo ()
    Cuentas_corrientes . crédito ( 2400 )

    Cuentas_corrientes . mostrar_saldo ()
    Cuentas_corrientes . débito ( 600 )

    imprimir ( Cuentas_corrientes )
