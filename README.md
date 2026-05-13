<img width="960" height="768" alt="Cálculo de Pi - mini" src="https://github.com/user-attachments/assets/7e89667a-0f64-409d-b717-4913b464ac56" />

Método geométrico para calcular Pi

¿Como funciona?
La idea tras este método para calcular el número Pi es que mediante el área de una circunferencia, se consigue más precisión que mediante el perímetro. Si lo piensas, el área del interior de una circunferencia se puede calcular exactamente. Solamente es en los bordes donde se acumular error y precisamente ahí es donde hay que atacarlo.

La idea es minimizar el error cometido al calcular el borde, hasta tal punto que lo aniquilemos. Con este código lo conseguimos, pues a pesar de realizarse millones de operaciones, el resultado no contiene cifras inexactas.

Lo que se calcula con este código es el área de un sector de circunferencia de 30º, en una circunferencia cuyo radio base es R=1, pero trabajamos con un radio mucho mayor, definido en SCALE y despues del cálculo lo reducimos al tamaño original, con lo que los errores desaparecen.

Hacemos barridos horizontales desde Y= 0 a Y = RADIUS //2. Los barridos son de 1 unidad de altura. La corrección de 0.5 que vemos en el código es para tomar el valor en el centro del barrido. De este modo, aumentamos muchísimo la precisión. Una gran parte del error lo eliminamos aquí.

Como la idea es mantener la altura del barrido en 1, como ya comenté, aumentamos el valor del radio una barbaridad, a un valor que en binario sea limpio, para evitar acumulación de errores en las operaciones.

El valor de los barridos se almacena en las variables small y big. small es quien de entrada, almacena los barridos, pero cuando supera el valor de RADIUS, se le resta dicha cantidad y se le suma a big.
Debido a que RADIUS es exacto, big siempre es exacto y los posibles errores, se acumulan en small.

La misión de la variable R2 únicamente es almacenar el cuadrado de RADIUS y evitar repetir una operación en cada una de las iteraciones del bucle

Al final, se suman los valores de small y bige y se les resta el valor del área triangular, para quedarnos únicamente con el área del sector de 30º, que multiplicaremos por 12, para obtener Pi.

El valor resultante de Pi= 3.1415926535897936 es lo máximo que se puede aproximar un double ó en este caso un float, cuya mantisa es de 53 bits

Este código, si no está compilado, tarda en ejecutarse unos segundos y si lo está, menos de 1 segundo.

Este método es de mi cosecha y no sé si ya existía o no, pero en base a como funciona, creo que se le puede llamar "Método de Pitágoras" y si me quereis dar crédito a mi, lo más correcto sería llamarlo "Metódo Pitágoras/BestmanPi"
