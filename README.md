¿Como funciona?
La idea tras este método para calcular el número Pi es que mediante el área de una circunferencia, se consigue más precisión que mediante el perímetro. Si lo piensas, el área del interior de una circunferencia se puede calcular exactamente, Solamente es en los bordes donde se puede acumular error y precisamente ahí es donde hay que atacarlo.

La idea es minimizar el error cometido al calcular el borde, hasta tal punto que lo aniquilemos. Con este código lo conseguimos, pues a pesar de realizarse millones de operaciones, el resultado no contiene cifras inexactas.

Lo que se calcula con este código es el área de un sector de circunferencia de 30º, en una circunferencia cuyo radio R=1. Haremos barridos horizontales desde Y=0 a Y=H, pero aplicaremos una corrección, tomando la medida en el centro del barrido. De ahí surge el valor 0.5 que aparece en el código. De este modo aumentamos muchísimo la precisión.

La idea es mantener el incremento del valor de Y, entre barridos en 1 por lo que aumentamos el valor del radio una barbaridad, a un valor que en binario sea limpio, para evitar acumulación de errores en las operaciones.

Dentro de cada ciclo del buche, restamos al valor del barrido la parte que sí conocemos con precisión y que se encuentra almacenado en la variable BM (Barrido Mínimo).

Además, para evitar que el valor de SUMA (la suma de las áreas de los barridos) crezca mucho, cuando supera un valor de la variable EXCESO (potencia de 2, para que sea exacto), se lo restamos y acumulamos en la variable CONTADOR, el número de veces que lo hacemos.

Al final, el valor de la variable TOTAL, almacena la suma de todas las áreas implicadas. Debido a que EXCESO * CONTADOR es exacto y mucho mayor que SUMA, aniquilamos completamente el error cometido en SUMA tras los millones de aperaciones acumuladas. EL valor resultante de Pi= 3.141592653589793 es lo máximo que se puede aproximar un double ó un este caso un float, cuya mantisa es de 53 bits

Este código, si no está compilado, tarda en ejecutarse unos segundos y si lo está, menos de 1 segundo.

Este método es de mi cosecha y no sé si existía o no, pero en base a como funciona, creo que lo correcto sería llamarlo "Método Pitágoras"
