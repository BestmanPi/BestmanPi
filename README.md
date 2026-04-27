<img width="960" height="768" alt="Cálculo de Pi - mini" src="https://github.com/user-attachments/assets/7e89667a-0f64-409d-b717-4913b464ac56" />
¿Como funciona?
La idea tras este método para calcular el número Pi es que mediante el área de una circunferencia, se consigue más precisión que mediante el perímetro. Si lo piensas, el área del interior de una circunferencia se puede calcular exactamente. Solamente es en los bordes donde se acumular error y precisamente ahí es donde hay que atacarlo.

La idea es minimizar el error cometido al calcular el borde, hasta tal punto que lo aniquilemos. Con este código lo conseguimos, pues a pesar de realizarse millones de operaciones, el resultado no contiene cifras inexactas.

Lo que se calcula con este código es el área de un sector de circunferencia de 30º, en una circunferencia cuyo radio base es R=1, pero trabajamos con un radio mucho mayor y despues del cálculo lo reduciremos al tamaño original, con lo que los errores desaparecen.

Hacemos barridos horizontales desde Y=0 a Y=H-1. Los barridos son de 1 unidad de altura. La corrección de 0.5 que vemos es el código es para tomar el valor en el centro del barrido. De este modo, aumentamos muchísimo la precisión. Una gran parte del error lo eliminamos aquí.

Como la idea es mantener la altura del barrido en 1, como ya cokmenté, aumentamos el valor del radio una barbaridad, a un valor que en binario sea limpio, para evitar acumulación de errores en las operaciones.

Dentro de cada ciclo del buche, restamos al valor del barrido la parte que sí conocemos con precisión y que se encuentra almacenado en la variable BM (Barrido Mínimo).

Además, para evitar que el valor de SUMA (la suma de las áreas de los barridos) crezca mucho, cuando supera el valor de la variable EXCESO (potencia de 2, para que sea exacto), se lo restamos y acumulamos en la variable CONTADOR, el número de veces que lo hacemos.

Al final, el valor de la variable TOTAL, almacena la suma de todas las áreas implicadas. Debido a que EXCESO * CONTADOR es exacto y mucho mayor que SUMA, aniquilamos completamente el error cometido en SUMA tras los millones de aperaciones acumuladas. Lo último que hacemos es multiplicar por 12, para obtener el número Pi. En una circunferencia de radio R=1, el área es Pi. Como hemos calculado el área de un sector de 30º y hay 12 sectores de 30º en 360º, de ahí viene el 12 que he comentado.

El valor resultante de Pi= 3.141592653589793 es lo máximo que se puede aproximar un double ó un este caso un float, cuya mantisa es de 53 bits

Este código, si no está compilado, tarda en ejecutarse unos segundos y si lo está, menos de 1 segundo.

Este método es de mi cosecha y no sé si ya existía o no, pero en base a como funciona, creo que lo correcto sería llamarlo "Método de Pitágoras" y si me quereis dar crédito a mi pues "Metódo Pitágoras/BestmanPi"
