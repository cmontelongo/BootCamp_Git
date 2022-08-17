# Proyecto 1: Calculadora de I.M.C

El presente proyecto es parte del BootCamp Fundamentos de Python C3, impartido por UCamp.
Este primer proyecto me ayuda a reforzar los conocimientos iniciales del lenguaje de programación Python, las primeras instrucciones para mostrar datos en pantalla, así como la entrada de datos son de mucha ayuda cuando se interactúa con el usuario y se debe mostrar parte del proceso para continuar y que esté enterado cuando hay un error controlado, o bien, el resultado de cálculos.

Para la captura de datos hize uso de un ciclo infinito, el cual solo se puede salir con la instrucción ***break***. La condición para salir de este ciclo, es que el dato no sea una cadena vacía para los datos que son cadenas string, y para los valores numéricos igualmente no sea una cadena vacía pero también sea mayor a cero.

Para las cadenas de string se valida que no sean vacías y en caso contrario se muestra un mensaje al usuario para que continúe intentando capturar el dato.

Para los valores numéricos solamente se valida que no sea primero una cadena vacía, y posterior se aplica un ***cast*** para convertirlo a valor ***float***. Este valor es validado para que sea mayor a cero y posteriormente es utilizado para realizar el cálculo solicitado.

Al momento de realizar la impresión de los datos con ***print***, se utilizan formatos de cadenas y numéricos ***float*** con decimales para mejor visualización del usuario.

Este proyecto es importante para comenzar a conocer la programación en Python.
