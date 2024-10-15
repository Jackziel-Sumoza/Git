# Todo sobre Git

Este repositorio es un compendio invaluable de herramientas y conocimientos prácticos sobre Git. Contiene una variedad de scripts y ejemplos que demuestran cómo aplicar las mejores prácticas en el control de versiones, desde la gestión de ramas hasta la resolución de conflictos. Es un recurso esencial para aquellos que buscan mejorar su productividad y colaborar de manera eficiente en proyectos de desarrollo.

Este repositorio es tu compañero de trabajo rápido y confiable. Aquí encontrarás una colección de códigos, extraídos de fuentes oficiales y verificadas, diseñados para que puedas aplicarlos directamente a tus proyectos. Olvídate de largas explicaciones teóricas: nos centramos en mostrarte cómo utilizar cada código de forma efectiva en tu día a día.

[Documentación y Sitios Webs Oficiales](#links-para-más-información-de-git)

---

## Tabla de contenido

- [Todo sobre Git](#todo-sobre-git)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Conceptos Básicos en Git:](#conceptos-básicos-en-git)
      - [Directorio](#directorio)
      - [Staging Area](#staging-area)
      - [Repositorio](#repositorio)
      - [Flujo de Git](#flujo-de-git)
  - [Comandos Básicos:](#comandos-básicos)
    - [Moverse entre carpetas](#moverse-entre-carpetas)
    - [Interacciones en consola](#interacciones-en-consola)
  - [Instalar Git](#instalar-git)
  - [Configuraciones Personales del Entorno:](#configuraciones-personales-del-entorno)
    - [Configuraciones iniciales](#configuraciones-iniciales)
    - [Configurar el editor de código y consola](#configurar-el-editor-de-código-y-consola)
  - [Comenzar Con Comandos de Git](#comenzar-con-comandos-de-git)
    - [Deshacer commits](#deshacer-commits)
    - [Ramas de Git](#ramas-de-git)
    - [Git Merge](#git-merge)
    - [Merge conflic](#merge-conflic)
    - [ALIAS](#alias)
    - [Recuperación de commits](#recuperación-de-commits)
  - [GIT Y GITHUB](#git-y-github)
    - [Git Remote](#git-remote)
    - [Ejemplo Pagina Web:](#ejemplo-pagina-web)
    - [git stash, git stash apply git stash pop](#git-stash-git-stash-apply-git-stash-pop)
    - [estudiar git cherry-pick](#estudiar-git-cherry-pick)
    - [estudiar rebase y squash](#estudiar-rebase-y-squash)
    - [estudiar estrategias de branching](#estudiar-estrategias-de-branching)
      - [Git Flow](#git-flow)
        - [Introducción](#introducción)
        - [Descripción general de la estrategia de Git Flow](#descripción-general-de-la-estrategia-de-git-flow)
        - [Herramientas e integraciones de flujo de trabajo](#herramientas-e-integraciones-de-flujo-de-trabajo)
        - [Desafíos comunes](#desafíos-comunes)
        - [¿Cómo utilizar GitFlow?](#cómo-utilizar-gitflow)
  - [Conventional Commits](#conventional-commits)
    - [Resumen](#resumen)
    - [El commit contiene los siguientes elementos estructurales, para comunicar la intención a los consumidores de tu librería:](#el-commit-contiene-los-siguientes-elementos-estructurales-para-comunicar-la-intención-a-los-consumidores-de-tu-librería)
    - [Especificación](#especificación)
    - [estudiar submodulos](#estudiar-submodulos)
    - [¿Qué es Git bisect?](#qué-es-git-bisect)
    - [¿Qué es Git Hooks?](#qué-es-git-hooks)
      - [Pasos para activar un Hook](#pasos-para-activar-un-hook)
      - [Pasos para crear un Hook personalizado](#pasos-para-crear-un-hook-personalizado)
    - [estudiar gitflow, githubflow](#estudiar-gitflow-githubflow)
  - [Links, para más información de Git:](#links-para-más-información-de-git)

## Conceptos Básicos en Git:

#### Directorio

El área de trabajo (working directory) es efectivamente la carpeta donde se encuentran los archivos con los que estás trabajando actualmente en un proyecto bajo control de versiones. Es como tu escritorio personal, pero con la ventaja de estar conectado a un sistema que registra todos los cambios que realizas.

#### Staging Area

El staging area no es donde modificamos los archivos, sino donde preparamos los cambios para ser guardados en el repositorio.

#### Repositorio

Un repositorio es un sistema de control de versiones que almacena de manera organizada y eficiente todos los archivos de un proyecto, junto con el historial completo de cambios realizados en ellos.

#### Flujo de Git

**Proceso explicado con una tienda de batidos:**

1. Área de trabajo (working directory): Es la barra donde preparas los batidos. Aquí es donde mezclas los ingredientes, añades hielo y decoras los vasos etc.

2. Bandeja (staging area): Una vez que tienes un vaso listo, lo colocas en la bandeja. La bandeja es como un lugar de espera temporal antes de llevar los vasos a la mesa.

3. Mesa (repositorio): La mesa representa el lugar final donde se sirven las bebidas a los clientes. Al llevar la bandeja a la mesa y dejar los vasos, estás guardando un registro permanente de las bebidas que se han servido.

> Aun tenemos que saber más cosas, pero podemos comenzar con esto.

---

Antes de comenzar a utilizar Git te recomiendo aprender unos comandos básicos que nos facilitan la vida.

## Comandos Básicos:

### Moverse entre carpetas

`cd [para mover hacia adelante]`

`cd ../ [para mover hacia atrás]`

`cd .. [para mover hacia atrás]`

### Interacciones en consola

**Ver los archivos de carpeta actual:**

`$ ls`

**Ver los archivos ocultos**

`$ ls -a` es importante cuando deseamos modificar algún archivo privado de los lenguajes o del mismo Git.

**Ver la dirección donde estamos posicionados:**

`$ pwd` también se puede visualizar desde la misma consola.

**Crear una carpeta**

`$ mkdir nombre_de_la_carpeta`

**Eliminar una carpeta o archivo**

`$ rmdir nombre_de_carpeta`

**Cambiar el nombre de un archivo**

`$ git mv archivo_a_renombrar archivo_renombrado`

**Limpiar la consola con**

`$ clear`

**Abrir VS-Code**

`$ code .`

Con este comando logramos abrir visual studio code en el directorio que nos encontremos posicionados. Por ejemplo, si estamos en `C:/Users/User/Desktop/Git/` y desde el `Git Bash` o el `Power Sell` iniciaremos en la carpeta Git

## Instalar Git

Instalar git en la pagina oficial [git-scm.com](https://git-scm.com/downloads).

**Verificar la instalación con:**

`$ git --version` o `$ git -v` (es el resumen)

## Configuraciones Personales del Entorno:

**Alcance de las configuraciones:**

Todas las configuraciones pueden ser realizadas de distintas formas, para que su alcance sea diferente, ya queda en su gusto determinar con cuales configuraciones quiere trabajar.

-   Sistema: Todos los usuarios y repositorios contenidos en el ordenador.
-   Global: Solo el usuario desde el que se registra git.
-   Local: Solo los repositorios en el que se inicia git.

---

### Configuraciones iniciales

**Nombre de usuario:**

-   `$ git config --system user.name "Nombre"`
-   `$ git config --global user.name "Nombre"`
-   `$ git config --local user.name "Nombre"`

**Correo electrónico del usuario:**

-   `$ git config --system user.email "xxxxxx@gmail.com"`
-   `$ git config --global user.email "xxxxxx@gmail.com"`
-   `$ git config --local user.email "xxxxxx@gmail.com"`

---

### Configurar el editor de código y consola

**Dar color a la interface (consola)**

`$ git config --global color.ui true`

**Activa tu editor de código por defecto:**
(en este caso es VSCODE)

`$ git config --global core.editor "code --wait"`

Lo que significa --wait, es para que cuando modifiquemos algo en visual studio code, se envié y confirme al cerrar visual studio code.

**Activar el CRLF en consola:**

`$ git config --global core.autocrlf true`

Con esto vas a evitar que siga escribiendo en la consola en usa sola linea indefinidamente. Cuando actives esta configuración, el texto se ajustara a tu pantalla automáticamente.

**Para ver todas las configuraciones que realizamos en Git:**

`$ git config --list`

## Comenzar Con Comandos de Git

Antes de inicializar Git en tu proyecto, primero debes estar posicionado en la dirección del mismo. Para lograr esto puedes acceder a tu carpeta, dal clic derecho y seleccionar `Open Git Bash` o entrar en la consola y dirigirte a la carpeta con los comandos explicados anteriormente, ejemplo:

```
$ cd users/user-name/desktop/example-project <GIT BASH>
> cd users/user-name/desktop/example-project <CMD>
```

Luego de estar en la carpeta donde vamos a utilizar git, escribir el comando de iniciar de Git.

**Inicializar Git:**

`$ git init`

Luego de iniciar git, veremos que en la consola nos aparece lo siguiente `users/user-name/desktop/example-project (master_or_main)` quiere decir que la instalación ha sido exitosa.

Para comenzar a utilizar Git debemos saber, el proceso que debemos pasar para utilizar Git. Siguiendo con el ejemplo de los batidos:

> Supongamos que queremos prepara un batido, para la mesa numero 1, en la mesa numero 1 hay 5 personas y cada una quiere un batido diferente.
>
> Fresa, Patilla, Naranja, Limón y Mango

Cada batido contiene sus ingredientes correspondientes; por ejemplo el de fresa debe de llevar más azúcar que el de patilla y así con los demás. 

Cuando estamos programando sucede exactamente lo mismo y Git nos ayuda a llevar las ordenes y las recetas de preparación.

**Proceso de trabajo:**

> 1. Para preparar el primer batido, no utilizamos Git (working directory).
> 2. Una vez listo el primer batido, debemos subirlo a la bandeja (staging area).
> 3. Al terminar todos los batidos de uno en uno debemos enviarlo a la mesa (repositorio).
> 4. Atender a las demás mesas y repetir el proceso.

Este es el proceso que deberíamos replicar con nuestro flujo de trabajo en Git.

**Subir al staging area:**

`$ git add nombre_del_archivo`

Si en vez de ``nombre_del_archivo`` colocamos `.` se suben todos los archivos. 

**Ver la el contenido de la bandeja (staging area) y el area de trabajo (working directory):**

El código `$ git status` nos permite visualizar como se encuentra el código, por ejemplo, si eliminamos un archivo, esto nos dirá cual es el archivo que eliminamos, si agregamos un archivo nos dirá cual agregamos y así sucesivamente.

Si queremos hacer mas cortos los mensajes de `$ git status`, podemos utilizar `$ git status -s` -s de -short.

>Ya que has entendido el contexto, pongámonos técnicos.

**Remover cambios del staging area:**

`$ git rm --cached nombre_de_archivo_a_remover`

`rm` de remove

Ahora tenemos un nuevo concepto y es commit, ya sabes lo que es un commit, el commit es el proceso de llevar la bandeja a la mesa numero 1. 

A este proceso se le llama commit.

**Enviar cambios del staging area al commit:**

El commit enviara todo lo que tengamos en el staging area, por esto es importante mantener en el staging area solo "los batidos" terminados.

Con `$ git commit` nos abrirá en nuestro editor de código una ventana, solicitando un mensaje clave, para identificar los cambios que están haciendo, en el caso del ejemplo **"Batido de Fresa"**.

Con `$ git commit -m "Batido de Fresa"` podemos agregar el comentario desde la consola.

`$ git commit -m "Batido de Fresa" -a` 

`-a` lo utilizamos si no hemos subido los archivos al staging area, con -a lo que hacemos es hacer un `git add .` y luego `git commit -m "Batido de Fresa"`

SI QUEREMOS RECUPERAR UN ARCHIVO BORRADO

`$ git restore nombre_de_archivo`

SI QUEREMOS DEVOLVER LOS CAMBIOS A COMO ESTÁN EN REMOTO

`$ git restore código_commit`

SI QUEREMOS DEVOLVER TODO A COMO ESTA EN EL STAGE Y NO LO SUBIMOS AL AREA DE STAGE (pierde los cambios)

`$ git checkout nombre_de_archivo`

MOSTRAR LOS CAMBIOS RESUMIDO

`$ git status -s`

PARA VER EL HISTORIAL DE CAMBIOS DE UN ARCHIVO

`$ git show nombre_de_archivo`

Busca directamente el commit y pinta los cambios directamente del archivo.

PARA VER LA DIFERENCIA ENTRE NUESTRO ARCHIVO ACTUAL Y EL QUE ESTA EN COMMIT

`$ git diff --staged`

Muestra primero todo el archivo anterior y luego el actual.

PARA VER LOS COMMIT QUE HAY Y SUS DATOS

`$ git log`

`$ git log --oneline`

Muestra un resumen del identificador del commit sin datos de usuarios etc. Hay posibilidades que al resumir la forma en la que se identifica el commit se repita cuando hay miles de commits, para ello se debe cambiar el resumido a 10 caracteres.

`$ git config --global core.abbrev "cantidad de caracteres"`

PARA VER LAS DIFERENCIAS PUNTUALES ENTRE LOS COMMIT

`$ git diff "código de commit" "código de commit"`

PARA VER SOLO EL NOMBRE DE LOS ARCHIVOS CAMBIADOS

`$ git diff --name-only "código de commit" "código de commit"`

PARA VER LAS LINEAS DE LOS ARCHIVOS QUE CAMBIARON

`$ git diff --word-diff "código de commit" "código de commit"`

PARA MODIFICAR UN COMMIT

`$ git commit --amend`

Modificar el comentario dentro del commit

si lo que queremos es subir cosas nuevas al commit, tenemos que preparar todo como si fuéramos a hacer un nuevo commit y luego hacemos lo mismo que en lo anterior.

El (HEAD-MASTER) lo que quiere decir es donde estamos posicionados con respecto a las ramas, en que commit estamos posicionados

Si lo que queremos es modificar un commit anterior, lo que sucederá es que se eliminaran todos los que estén después de ese commit.

SI AUN ASI QUIERES MODIFICAR UN COMMIT ANTERIOR

`$ git rebase -i head~número_de_indices_a_retroceder`

LUEGO PARA DEVOLVER LOS COMMIT QUE CARGAMOS

`$ git rebase --continue`

---

### Deshacer commits

FORMAS DE DESHACER COMMITS

`$ git reset --soft código_de_commit o head~números_a_volver`

Forma de borrado suave, agarra los archivos del borrado y lo envía al area de staging.

`$ git reset --mixex código_de_commit o head~números_a_volver`

Forma de borrado media, lo que sucede es que eliminamos y no agrega ni elimina nada del area de staging.

`$ git reset --hard código_de_commit o head~números_a_volver`

Forma de borrado fuerte, elimina y sobrescribe todo, desde area de trabajo, staging y commit.

---

### Ramas de Git

-   Volver de una rama diferente a la master, se llama merge

PARA MOSTRAR LOS BRANCH

`$ git branch`

PARA CREAR UN NUEVO BRANCH

`$ git branch nombre-de-la-rama`

La forma de nombrar las ramas es quebap-case

MOVER ENTRE RAMAS

`$ git checkout rama-a-la-que-nos-moveremos`

`$ git swith rama-a-la-que-nos-moveremos`

Utilizar esta, es nueva pero esta optimizada.

FORMA DE CREAR Y MOVER A ELLA

`$ git checkout -b rama-nueva`

Creamos una rama con -b y nos movemos a ella inmediatamente.

`$ git switch -c rama-nueva`

Creamos una rama con -c y nos movemos a ella inmediatamente.

BORRAR LAS RAMAS

`$ git branch -d rama-que-queremos-borrar`

Tenemos que estar en otra rama para borrarla.

MODIFICAR RAMAS (si no estoy en la rama)

`$ git branch -m nombre-de-rama nombre-de-la-rama-modificada`

`$ git branch -m nuevo-nombre-de-rama-actual`

Si estoy en la rama.

FORZAR EL MOVER LAS RAMAS

`$ git branch -f name-branch código_commit (or HEAD~Index)`

Este código funciona, sin la necesidad de estar posicionado en la rama, que se desea mover.

`$ git checkout HEAD~Index`

Con este código podemos mover el head de la rama en la que estamos posicionados.

`$ git checkout HEAD^`

Podemos retroceder un espacio y con más `^^^` retrocedemos mas espacios.

---

### Git Merge

`$ git merge nombre-de-la-rama`

Tengo que estar en la rama que voy a la que voy a unir; las ramas seguirán existiendo, solo que se une a la otra.

---

### Merge conflic

Es ese conflicto que se da cuando al trabajar sobre otra rama, la rama master se modifica y luego nosotros queremos hacer un merge y no se sabe que modificación hacer.

MOSTRAR LOS COMMITS DE TODAS LAS RAMAS

`$ git log --oneline --all`

SI NO PUSIMOS CONTINUAR AL RESOLVER EL CONFLICTO

`$ git merge --continue`

ACCEDER A LOS ARCHIVOS

`$ git lsr-tee -r --name-only código_de_commit`

Lo que hacemos con este es acceder a los archivos que posee un commit.

MOSTRAR TODOS LOS COMMITS Y ADEMAS GRAFICARLOS POR LAS RAMAS

`$ git log --oneline --all --graph`

---

### ALIAS

Los alias no llevan git

`$ git config --global alias.nombre-del-alias "todo el código que queremos resumir en alias"`

---

### Recuperación de commits

PARA RECUPERAR UN COMMIT BORRADO

-   Se necesita tener el código_commit

`$ git reset --hard código_commit`

RECUPERAR TODAS LAS REFERENCIAS DEL HEAD Y SUS MOVIMIENTO

`$ git reflog`

## GIT Y GITHUB

### Git Remote

GUARDAR EL ENLACE DEL REPOSITORIO REMOTO

`git remote add origin https://remote-repo-url`

CLONAR UN REPOSITORIO EN LA NUBE

En github se visualiza como fork, que es crear un clon del repositorio.

Origin hace referencia al repositorio en la nube

`$ git clone https://estedebeserelenlacecopiadodelrepositorio.com`

SUBIR EL REPOSITORIO A LA NUBE

`$ git push origin(donde) master(rama)`

El clon mantiene la referencia al repositorio remoto.

ACTUALIZAR EL CÓDIGO, TRAER EL CÓDIGO DEL REMOTO A MI REPOSITORIO LOCAL SE ACTUALIZA Y LE VALE MADRE LO QUE TENGAS, NO USAR SIN PENSAR

`$ git pull`

ACTUALIZAR EL CÓDIGO, TRAER EL CÓDIGO DEL REMOTO Y EVALUAR COMO LO VAS A UTILIZAR (GIT PULL HACE GIT FETCH Y LUEGO GIT MERGE)

`$ git fetch`

CREAR UN ARCHIVO

`$ touch archivo.txt`

SABER SI ESTOY CONECTADO A UN SERVIDOR REMOTO Y QUE PUEDO HACER

`$ git remote -v`

AGREGAR UN REPOSITORIO A LA NUBE

`$ git remote add origin(puede ser cualquier nombre) https://........`

CREAR UNA RAMA REMOTA DIRECTAMENTE DEL Local

`$ git branch -M main`

HACER UN PUSH A LA NUBE DIRECTAMENTE DEL LOCAL

`$ git push origin main`

si queremos configurar el push con todo eso por defecto agregar -u

`$ git push -u origin main`

---

-   Un fork es hacer una copia de un repositorio en mi repositorio de Github.

-   Un issue es una lista de tareas de un proyecto completo.

-   Una rama, un objetivo.

-   Rama debe ser descriptiva escrita con kevap-case.

-   No trabajar nunca en la rama principal, NUNCA.

-   Estrategias de branching.

-   Los commits deben de ser significativos; los commits deben de ser atomicos pero significativo, cambios importantes a nivel micro.

-   Los commits deben ser descriptivos.

-   Utilizar tags en el proyecto, debe ser importantes.

-   Mantener el historial limpios.

-   Commits innecesarios y no relacionables no se hacen
    piensa lo siguiente, que haces mucho en un proyecto, haces cambios importante y al finalizar todo el proyecto es que haces el commit, lo que sucede es que si una parte de ese proyecto la quieres mover y usarla en otros lugares tendrás que moverla completa y eso no es lo que quieres directamente.

-   ahora si haces muchos pequeños commits innecesarios, para hacer algo simple tendrás que trasladar muchos commits para poder hacer algo simple como aplicar una funcionalidad a otra rama entonces se debe encontrar un equilibro ahi.

-   ejemplo: cambio importante y significativo pequeño.

### Ejemplo Pagina Web:

-   rama-master
    -   header-de-la-Web
        -   header-de-la-web-responsive
            -   botón-hamburguesa
            -   stage cambios-del-botón
                -   commit "creación del diseño del botón hamburguesa"
                -   commit "funcionalidad del botón hamburguesa"
                -   commit "Solución de problemas del botón hamburguesa inicial y cambios de colores en el diseño"

---

### git stash, git stash apply git stash pop

Si tenemos cambios que necesitamos guardar para cambiarnos a una rama que necesitamos trabajar lo solucionamos con stash (stash es un lugar temporal en el que guardamos los cambios pero estos no son directamente formalmente terminados) stash es un borrador

`$ git stash`

Guarda los cambios en una zona de borrador.

`$ git stash list`

Nos muestran los archivos guardados en el stash

`$ git stash show`

Nos muestra el archivo preciso en el que se modifico el código del stash.

`$ git stash show -p`

Nos muestra las lineas que fueron modificadas por este stash.

`$ git stash apply indice-del-cambio(si no agrego nada, devuelve todo)`

Devolvemos los cambios al area de trabajo.

`$ git stash push -m "comentario al stash"`

Agregamos un comentario al stash para identificarlo mejor.

`$ git stash pop indice-del-cambio(si no lo agrego borra el primero)`

Elimina el stash que seleccionamos.

`$ git stash drop indice-del-cambio`

Elimina el stash que seleccionamos.

---

### estudiar git cherry-pick

Un cherry pick es un proceso de traer los cambios de un commit a un merge, lo que sucede es que no hacemos un merge completo y el commit que hicimos se duplica ya que no elimina el de la rama secundaria, lo que sucede en ese caso es que tendremos dos commits identicos, si luego hacemos un merge completo de la rama.

`$ git cherry-pick código_de_commit ...`

Otra forma de crear un cherry-pick es con rebase, con esto logramos tener una ventana interactiva que nos permite elegir de multiples commits, cual queremos utilizar, y cuales no, reordenarlos etc, es mas simple si no queremos trabajar tan profundamente con los hashes.

`$ git rebase -i HEAD~Index (or código_commit)`

<!--
### estudiar milesthons

***

### estudiar tags

*** -->

### estudiar rebase y squash

Lo que hacemos con Git rebase, es tomar toda la rama x y colocarla por delante de la rama y, lo que pasa es que se sobre escribe el historial de las ramas y cambian los códigos de los commits, afectamos los historiales, si no se quiere modificar el historial lo mejor seria hacer un merge.

`$ git rebase nombre-de-la-rama`

Lo que hace Git squash es unir todos los commits en uno solo, pero no se hace el commit automatico sino que se queda en el stage area y para terminarlo, se debe hacer un commit nuevo, que contiene todos los commits anteriores.

`$ git merge --squash nombre-de-la-rama`

Debe acompañarse con un nuevo commit

### estudiar estrategias de branching

---

#### Git Flow

##### Introducción

Este documento proporciona una descripción general de la estrategia de control de versiones de Git Flow, diseñada para administrar el desarrollo de funciones de manera eficaz.

##### Descripción general de la estrategia de Git Flow

La estrategia de Git Flow es un modelo de ramificación que ayuda a optimizar el desarrollo de funciones y la administración de versiones. Los componentes clave de esta estrategia incluyen:

-   **Ramas de funciones**: se utilizan para desarrollar nuevas funciones.
-   **Ramas de versiones**: se utilizan para preparar una nueva versión de producción.
-   **Ramas de revisión**: se utilizan para parches rápidos para producción.
-   **Rama maestra**: contiene código listo para producción.
-   **Rama de desarrollo**: integra funciones para la próxima versión.

##### Herramientas e integraciones de flujo de trabajo

Para mejorar la estrategia de Git Flow, se utilizan las siguientes herramientas e integraciones:

-   **Herramientas de integración continua/implementación continua (CI/CD)**: automatizan las pruebas y la implementación.
-   **Plataformas de revisión de código**: facilitan las revisiones por pares y mantienen la calidad del código.
-   **Sistemas de seguimiento de problemas**: administran tareas y realizan un seguimiento del progreso.
-   **Herramientas de documentación**: garantiza una documentación completa y accesible.

##### Desafíos comunes

Los usuarios pueden encontrar los siguientes desafíos al implementar la estrategia de Git Flow:

-   Comprender la gestión de ramas
-   Resolver conflictos de fusión
-   Mantener las ramas actualizadas
-   Cumplir con las pautas de los mensajes de confirmación

![Imagen de Flujo Git](assets/gitflow-diagram.png)

##### ¿Cómo utilizar GitFlow?

PARA INICIAR GITFLOW EN GIT

` $ git flow init`

Dar enter en todo lo que nos pregunta, por convención se recomienda no editarlo, si la estrategia que utilizamos es GitFlow, lo ideal es utilizar este código ya que con pocos comandos, nos permite hacer lo que hariamos con el doble de comandos.

La información que utilizare para explicar estos comandos los extrage del sitio web [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) si quiere revisar de forma más detallada.

PARA CREAR CUALQUIER RAMA CON GITFLOW

`$ git flow feature start nombre-de-la-rama`

PARA CERRAR LA RAMA

`$ git flow feature finish nombre-de-la-rama`

En nosotros queda el utilizar correctamente la creación y terminación de las ramas.

La rama se elimina automáticamente después de realizar el merge de la misma con `develop`.

El flujo general de Gitflow es:

1. A `develop` la rama se crea a partir de `main`

2. A `release` la rama se crea a partir de `develop`

3. Feature las ramas se crean a partir de `develop`

4. Cuando a feature está completo se fusiona en el `develop` rama

5. Cuando el `release` la rama se hace en la que se fusiona `develop` y `main`

6. Si un problema en `main` se detecta a `hotfix` la rama se crea a partir de `main`

7. Una vez que el `hotfix` está completo, se fusiona con ambos `develop` y `main`

## Conventional Commits

### Resumen

La especificación de Commits Convencionales es una convención ligera sobre los mensajes de commits. Proporciona un conjunto sencillo de reglas para crear un historial de commits explícito; lo que hace más fácil escribir herramientas automatizadas encima del historial. Esta convención encaja con [SemVer](http://semver.org/lang/es/), al describir en los mensajes de los commits las funcionalidades, arreglos, y cambios de ruptura hechos.

El mensaje del commit debe ser estructurado de la siguiente manera:

> <tipo>[ámbito opcional]: <descripción>
>
> [cuerpo opcional]
>
> [nota(s) al pie opcional(es)]

### El commit contiene los siguientes elementos estructurales, para comunicar la intención a los consumidores de tu librería:

-   fix: un commit de tipo fix corrige un error en la base del código (se correlaciona con PATCH en el Versionado Semántico).

-   feat: un commit de tipo feat introduce una nueva funcionalidad en la base del código (se correlaciona con MINOR en el Versionado Semántico).

-   BREAKING CHANGE: un commit que contiene la nota al pie BREAKING CHANGE:, o que agrega un ! después del tipo/ámbito, introduce un cambio de ruptura de API (se correlaciona con MAJOR en el Versionado Semántico). Un BREAKING CHANGE puede ser parte de commits de cualquier tipo.

-   tipos distintos a fix: y feat: están permitidos, por ejemplo @commitlint/config-conventional (basados en la convención de Angular) que recomienda build:, chore:, ci:, docs:, style:, refactor:, perf:, test:, y otros.

-   notas al pie distintas de BREAKING CHANGE: <descripción> pueden ser añadidas y siguen una convención similar al formato Git trailer.

Tipos adicionales no son obligatorios en la especificación de Commits Convencionales, y no tienen un efecto implícito en el Versionado Semántico (al menos que incluyan un BREAKING CHANGE). Un ámbito puede ser añadido al tipo de un commit, para proveer información adicional contextual y debe ser contenido entre paréntesis, ej., feat(parser): add ability to parse arrays.

> #### Ejemplos
>
> -   Mensaje de commit con descripción y cambio de ruptura en la nota al pie
>
> -   feat: allow provided config object to extend other configs

BREAKING CHANGE: extends key in config file is now used for extending other config files

Mensaje de commit con ! para llamar la atención al cambio de ruptura

> refactor!: drop support for Node 6

Mensaje de commit con ambos ! y BREAKING CHANGE en la nota al pie

> refactor!: drop support for Node 6
>
> BREAKING CHANGE: refactor to use JavaScript features not available in Node 6.

Mensaje de commit sin cuerpo

> docs: correct spelling of CHANGELOG

Mensaje de commit con ámbito

> feat(lang): added polish language

Mensaje de commit con cuerpo multi-párrafo y múltiples notas al pie

> fix: correct minor typos in code
>
> see the issue for details
>
> on typos fixed.
>
> Reviewed-by: Z
>
> Refs #133

### Especificación

Las palabras clave “DEBE” (“MUST”), “NO DEBE” (“MUST NOT”), “REQUERIDO” (“REQUIRED”), “DEBERÁ” (“SHALL”), “NO DEBERÁ” (“SHALL NOT”), “DEBERÍA” (“SHOULD”), “NO DEBERÍA” (“SHOULD NOT”), “RECOMIENDA” (“RECOMMENDS”), “PUEDE” (“MAY”) y “OPCIONAL” (“OPTIONAL”) en este documento se deben interpretar como se describe en RFC 2119.

Los commits DEBEN iniciarse con un prefijo de tipo que consiste en un sustantivo, feat, fix, etc., seguido del ámbito OPCIONAL, !OPCIONAL, y dos puntos y un espacio REQUERIDO.

El tipo feat DEBE ser usado cuando un commit agrega una nueva funcionalidad a la aplicación o librería.

El tipo fix DEBE ser usado cuando el commit representa una corrección a un error en el código de la aplicación (bug).

Un ámbito PUEDE ser añadido después de un tipo. Un ámbito DEBE consistir en un sustantivo que describa una sección de la base del código encerrado entre paréntesis, ej., fix(parser):.

Una descripción DEBE ir inmediatamente después de los dos puntos y el espacio del prefijo de tipo/ámbito. La descripción es resúmen corto de los cambios realizados en el código, ej., fix: array parsing issue when multiple spaces were contained in string..

Un cuerpo de commit más extenso PUEDE agregarse después de la descripción corta, dando información contextual adicional acerca de los cambios en el código. El cuerpo DEBE iniciar después de una línea en blanco después de la descripción.

Un cuerpo de commit es de forma-libre y PUEDE consistir de cualquier número de párrafos separados por una nueva línea.

Una o más notas al pie PUEDEN ser añadidas una línea en blanco después del cuerpo. Cada nota al pie DEBE consistir de una palabra clave, seguida ya sea por un separador :<espacio> o <espacio>#, seguido por un valor cadena (string) (esto está inspirado por la convención Git trailer).

Una palabra clave de una nota al pie DEBE usar - en lugar de caracteres de espacios en blanco, ej., Acked-by (esto ayuda a diferenciar la sección de la nota al pie de un cuerpo multi párrafo). Se hace una excepción para BREAKING CHANGE, que también PUEDE ser usada como palabra clave.

Una nota al pie PUEDE contener espacios y líneas en blanco, y el parseo DEBE terminar cuando se observe el siguiente separador/clave.

Los cambios de ruptura DEBEN ser indicados en el prefijo de tipo/ámbito de un commit, o como una entrada en la nota al pie.

Si se incluye como una nota al pie, un cambio de ruptura DEBE consistir del texto en mayúsculas BREAKING CHANGE, seguido de dos puntos, y una descripción, ej., BREAKING CHANGE: environment variables now take precedence over config files.

Si se incluye en el prefijo de tipo/ámbito, cambios de ruptura DEBEN ser indicados por un ! inmediatamente después de :. Si ! es usado, BREAKING CHANGE: PUEDE ser omitido de la sección de la nota al pie, y la descripción del commit DEBERÁ ser usada para describir el cambio de ruptura.

Tipos diferentes a feat y fix PUEDEN ser usados en los mensajes de commit, ej., docs: updated ref docs..

Las unidades de información que componen Commits Convencionales NO DEBEN ser tratados como implementadores sensitivos de caso, con la excepción de BREAKING CHANGE que DEBE ir en mayúsculas.

BREAKING-CHANGE DEBE ser sinónimo de BREAKING CHANGE, cuando se usa en una nota al pie.

---

### estudiar submodulos

---

### ¿Qué es Git bisect?

**Git bisect** es una herramienta de depuración útil que se utiliza en Git para encontrar qué commit específico fue el primero en introducir un bug o problema en tu código.

**Funcionamiento**

Al tener una rama de Git con muchos commits y donde en uno de ellos se produce un error. Git bisect utiliza un algoritmo de búsqueda binaria para dividir eficientemente el historial de commits en dos partes:

1. **Inicio:** Identificas un commit "bueno" (sin el error) y un commit "malo" (con el error).
2. **Búsqueda binaria:** Git bisect selecciona un commit intermedio y te pregunta si ese commit es "bueno" o "malo".
3. **Iteración:** Basándose la respuesta, Git bisect descarta la mitad del historial donde no se encuentra el error y repite el proceso con un nuevo commit intermedio.
4. **Resultado:** Este proceso se repite hasta que se encuentra el commit exacto donde se introdujo el error.

**Ventajas de usar git bisect:**

-   **Eficiencia:** Al utilizar una búsqueda binaria, encuentra rápidamente el commit culpable, incluso en grandes historiales.
-   **Automatización:** Gran parte del proceso es automatizado, lo que ahorra tiempo y reduce la posibilidad de errores humanos.
-   **Precisión:** Identifica el commit exacto donde se introdujo el error, lo que facilita la depuración.

**¿Cuándo usar git bisect?**

-   Cuando tienes un bug difícil de reproducir y necesitas encontrar su origen.
-   Cuando quieres entender cómo evolucionó una determinada característica en tu código.
-   Cuando necesitas revertir un cambio que introdujo un error sin afectar otros cambios.

**Ejemplo básico:**

```bash
git bisect start
git bisect bad <hash del commit malo>
git bisect good <hash del commit bueno>
```

A partir de ahí, Git bisect te irá mostrando diferentes commits. Tú simplemente tienes que indicar si cada commit es "bueno" o "malo".

En la **documentación oficial de git** [git-scm.com/docs/git-bisect](https://git-scm.com/docs/git-bisect) puede encontrar más información.

Bisect significa (dividir en dos partes). Este es un metodo avanzado de depuración de código mediante Git con el que se pueden encontrar bugs y otros problemas en el código de forma rapida, puede resultar tedioso en un proyecto grande, a continuación solo se presentan unos comandos rapidos para utilizar git bisect

COMANDOS PARA UTILIZAR GIT BISECT

`$ git bisect start`

Esto iniciara la depuración, luego se debe identificar un rango, donde evaluaremos los problemas, para ellos debemos introducir.

1. Donde tenemos los problemas de software `$ git bisect bad código_commit_actual` puede ser otro commit, solo es donde detectamos el problema.
2. Donde sabemos que el código estaba bien `$ git bisect good código_commit_version_anterior` o donde sabemos que el código estaba bien.

Esto iniciara una depuración donde nos ira mostrando multiples commits y nosotros debemos determinar uno a uno si es bueno o malo e ir corrigiendo. Esto lo hacemos con `$ git bisect bad` o `$ git bisect good`.

Una vez se termina la depuración se utiliza el comando `$ git bisect reset`

Git bisect es mucho más complejo por ello se recomienda al momento de utilizar leer la documentación oficial.

---

### ¿Qué es Git Hooks?

#### Pasos para activar un Hook

#### Pasos para crear un Hook personalizado

---

### estudiar gitflow, githubflow

## Links, para más información de Git:

1. [Ejemplos interactivos y documentación](https://antonz.org/git-by-example/)
2. [Juegos para aprender Git](https://learngitbranching.js.org/?locale=es_ES)
3. [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
