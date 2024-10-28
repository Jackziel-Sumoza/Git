Comenzamos este archivo en el comentario `5be7e17`.

Iniciamos insertando la estrategia de branches en Git, vamos a utilizar Git Flow.

1. Crear una rama feature para agregar la explicación del funcionamiento de Git Flow.
   1. `$ git flow feature start gitflow-explanation`
2. Nos dirigimos a la rama develop.
   1. `$ git switch develop`
3. Creamos un commit en la rama develop, con el archivo .gitignore modificado y historial-manual.md actualizado.
   1. `$ git add historial-manual.md .gitignore`
   2. `$ git commit` más mensaje con editor
4. Cerrar una rama feature para terminar de agregar la explicación del funcionamiento de Git Flow al master.
   1. `$ git flow feature finish gitflow-explanation` 
5. Subir la rama develop con sus cambios y modificaciones al repositorio remoto
   1. `$ git fetch` 
   2. `$ git push origin develop` 
6. Desde GitHub, hicimos un pull request y luego ejecutamos un Merge para combinar la rama develop, con la rama master, al hacer pull request nos saltamos el release (es lo mismo que el pull request).
7. Creamos una nueva rama para explicar como funciona el git hooks.
   1. `$ git flow feature start git-hooks` 
8. Para utilizar git bisect, primero creamos un archivo, luego creamos una rama con el nombre de git-bisect, que es lo que estamos probando y luego ejecutamos unos problemas para corregirlos con git bisect.
   1. `$ git flow feature git-bisect-init` 
   2. `$ git add .` 
   3. `$ git bisect start` 
   4. `$ git bisect bad código_bad` 
   5. `$ git bisect good código_good` 
   6. `$ git add .` 
   7. `$ git commit --amend` 
   8. `$ git bisect reset`
   9. > con esto logramos depurar el código y mantener el historial limpio y de forma correcta.