let divCartas = document.querySelector("#divCartas");
arrayPosts = [];
let url = "http://127.0.0.1:5000/civilizaciones";
let boton = document.querySelector('#boton')

boton.addEventListener("click",(e) => {
    fetch(url)
    .then((ok) => {
      if (ok.status == 200) {
        return ok.json();
      } else {
        console.log("Conexion correcta, url no codificada");
      }
    })
    .then((ok1) => {
      const arrayPosts = [];
      ok1.civilizaciones.forEach((element) => {
        const post = {
          especialidad: element.especialidad,
          imagen: element.imagen,
          nombre: element.nombre,
          tecnologia_unica: element.tecnologia_unica,
          unidad_unica: element.unidad_unica,
        };
        arrayPosts.push(post);
      });
      return arrayPosts;
    })
    .then((arrayPosts) => {
      arrayPosts.forEach((element) => {
        divCartas.innerHTML += `<div class="card" style="width: 18rem;">
          <img src="${element.imagen}" class="card-img-top" alt="...">
          <div class="card-body">
          <h5 class="card-title">${element.nombre}</h5>
          <p class="card-text">${element.especialidad}, ${element.unidad_unica}, ${element.tecnologia_unica}</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
      </div>`;
      });
    })
    .catch((err) => {
      console.log("La conexion no se ha podido producir");
      console.log(url);
      console.log(arrayPosts);
    });
})