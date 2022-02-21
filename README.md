# ProyectoFinal 
La url de inicio es http://127.0.0.1:8000/, para la cual siempre solicita login

Partes del proyecto
- Login
    - Home
    - Servicios
        - Listado
        - Ver detalle de items
        - Editar item
        - Eliminar item
    - Tecnicos
        - Listado
        - Ver detalle de items
        - Editar item
        - Eliminar item
    - Stock
        - Listado
        - Ver detalle de items
        - Editar item
        - Eliminar item
    - Nosotros
        - Pagina estática con texto e imagen
    - Logout

- Registro
    - Alta usuario
    - Ir al login

- Edición de usuario
- Asignar avatar

Las URLs especificas, que no se encuentran dentro de la navegación son:
- Edición de usuario (tiene control de login): http://127.0.0.1:8000/user/editar
- Alta usuario (tiene control de login): http://127.0.0.1:8000/registro
- Asignar avatar (solo en caso de no tener ya uno asignado, de lo contrario se accede desde el mismo avatar): http://127.0.0.1:8000/user/avatar


Inconveniente conocido que no pude resolver: 

Pasando la clase AvatarView en este orden "class TecnicoDetailView(LoginRequiredMixin, DetailView, AvatarView):",
    - cuando el usr tiene avatar asignado, se pierde al navegar por el sitio
    - cuando el usr no tiene avatar asignado
Pasandola en este orden "class TecnicoDetailView(LoginRequiredMixin, AvatarView, DetailView):"
    - cuando el usr tiene avatar asignado, se muestra correctamente en todo el sitio
    - cuando el usr no tiene avatar asignado, arroja un error. ('NoneType' object has no attribute 'imagen')