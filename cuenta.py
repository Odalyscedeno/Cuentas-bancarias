clase  Cuenta_Bancaria :

    def  _init_ ( self , numero =  Ninguno , nombrepropietario =  Ninguno , saldo : float  =  0 ):
        uno mismo _numero  =  numero
        uno mismo _nombrepropietario  =  nombrepropietario
        uno mismo _saldo  =  saldo
    def  _str_ ( uno mismo ):
        return  f' Cuentas Bancarias: { self . _dict_ . _str_ () } '

    @ propiedad
    def  numero ( yo ):
        devolverse  a uno mismo . _numero

    @numero . _ setter
    def  numero ( self , numero ):
        uno mismo _numero  =  numero

    @ propiedad
    def  nombrepropietario ( self ):
        devolverse  a uno mismo . _nombrepropietario

    @ nombrepropietario . setter
    def  nombrepropietario ( self , nombrepropietario ):
        uno mismo _nombrepropietario  =  nombrepropietario

    @ propiedad
    def  saldo ( auto ):
        devolverse  a uno mismo . _saldo

    @saldo . _ setter
    def  saldo ( self , saldo ):
        uno mismo _saldo  =  saldo

    def  credito ( self , valor : float  =  0 ):
        uno mismo _saldo  =  float ( self . _saldo ) +  float ( valor )
        devolverse  a uno mismo . _saldo

    def  debito ( self , valor : float  =  0 ):
        uno mismo _saldo  =  float ( self . _saldo ) -  float ( valor )
        devolverse  a uno mismo . _saldo

    def  mostrar_saldo ( self ):
        imprimir ( self . _saldo )
