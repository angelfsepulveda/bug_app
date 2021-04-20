$(document).ready(function() {

  // Función para cargar el formulario del cuestionario
  $(document).on('click', '.btnIniciar', function() {
    $('#iniciarCuestionario').hide(); // Se oculta el div padre de este botón
    $('#ingresarComo').show('slow'); // Se muestra el div del form para elegir el tipo de cuestionario
  });

  // Función para obtener el tipo de cuestionario elegido
  $(document).on('click', '.btn-tipocuest', function() {
    var tipo = $(this).attr('id'); // Guardamos el id del botón clickeado en la variable tipo
    $(document).find('#inputTipoCuestionario').val(tipo); // Pasamos el valor de tipo al input
    if (tipo == '1' || tipo == '2') {
      $(document).find('#labelClave').html('').html('Ingrese su R.F.C.'); // Cambiamos el texto del label
      $(document).find('#inputClave').attr('name','RFC').attr('placeholder', 'R.F.C.'); // Agregamos RFC como name del input y cambiamos el texto del placeholder
    } else if (tipo == '3') {
      $(document).find('#labelClave').html('').html('Ingrese la C.U.R.P. de su hijo.'); // Cambiamos el texto del label
      $(document).find('#inputClave').attr('name','CURP').attr('placeholder', 'C.U.R.P. del alumno'); // Agregamos CURP como name del input y cambiamos el texto del placeholder
    }
    $(document).find('#clave').show(); // Mostramos el input
  });

  // Función para contar caracteres en inputClave
  $(document).find('#inputClave').on('keyup',function(){
    $(document).find('#btnEnviar').hide(); // Nos aseguramos de que el botón Enviar esté oculto
    $('#clave').removeClass('has-success').removeClass('has-warning').removeClass('has-error'); // Removemos las clases de color que pudiera tener
    var max_char = 0; // Inicializamos la variable para la máxima longitud de caracteres
    var name = $(this).attr('name'); // Obtenemos el valor del atributo name del input
    if (name == 'RFC') { // Si es RFC
      max_char = 13; // La cantidad máxima de caracteres permitidos será de 13
    } else if (name == 'CURP') { // Si es CURP
      max_char = 18; // La cantidad máxima de caracteres permitidos será de 18
    }
    var char = $(this).val().length; // Obtenemos la longitud de los caracteres ingresados en el input
    if (char >= 1 && char <= 4 || char > max_char) { // Mientras el valor de char sea mayor que 0 y menor que 5, o menor que el valor de max_char
      $('#clave').addClass('has-error'); // Agregamos la clase has-error al input
      $('#datosPF').hide();
      $(document).find('#btnEnviar').hide(); // Mantenemos oculto el botón Enviar
    } else if (char <= 9 && char >= 5) { // Mientras el valor de char sea mayor que 4 y menor que 10
      $('#clave').addClass('has-warning'); // Agregamos la clase has-warning al input
      $('#datosPF').hide();
      $(document).find('#btnEnviar').hide(); // Mantenemos oculto el botón Enviar
    } else if (char >= 10 && char <= max_char) { // Mientras el valor de char sea mayor que 9 y menor que el valor de max_char
      $('#clave').addClass('has-success'); // Agregamos la clase has-success al input
      if (name == 'CURP') {
        $('#datosPF').show();
      }
      $(document).find('#btnEnviar').show(); // Mostramos el botón Enviar
    }
  });
  $(document).on('click', '.num-peticion', function() {
      var parent = $(this).closest('tr');
      var statusPet = parent.attr('status');
      var numPet = $(this).attr('num');
      var munPet = parent.find('.munPet').html();
      var zePet = parent.find('.zePet').html();
      var cctPet = parent.find('.cctPet').html();
      var tipoPet = parent.find('.tipoPet').html();
      var fechaPet = parent.find('.fechaPet').html();
      $('#tituloModalPeticiones').html('').html(statusPet);
      $('#CCT').html('').html(cctPet);
      $('#MUN').html('').html(munPet);
      $('#ZE').html('').html(zePet);
      $('#SOL').html('').html(tipoPet);
      $('#FECHA').html('').html(fechaPet);
      if (statusPet == 'Solicitada') {
        $('.titulillo').removeClass('text-primary text-success text-info text-warning text-danger');
        $('#iconillo').removeClass('fa-check fa-check-square-o fa-forward fa-times').addClass('fa-plus');
        $('#btnAutorizar').show();
      } else if (statusPet == 'Autorizada') {
        $('.titulillo').removeClass('text-primary text-success text-warning text-danger').addClass('text-info');
        $('#iconillo').removeClass('fa-plus fa-check-square-o fa-forward fa-times').addClass('fa-check');
        $('#btnProcesar').show();
      } else if (statusPet == 'En proceso') {
        $('.titulillo').removeClass('text-info text-success text-warning text-danger').addClass('text-primary');
        $('#iconillo').removeClass('fa-plus fa-check-square-o fa-check fa-times').addClass('fa-forward');
        $('#btnCompletar').show();
      } else if (statusPet == 'Completada') {
        $('#btnImprimir').show();
        $('.titulillo').removeClass('text-info text-danger text-warning text-primary').addClass('text-success');
        $('#iconillo').removeClass('fa-plus fa-check-square-o fa-forward fa-times').addClass('fa-check-square-o');
        $('#btnRechazar').hide();
      } else if (statusPet == 'Rechazada') {
        $('#btnImprimir').show();
        $('.titulillo').removeClass('text-info text-success text-warning text-primary').addClass('text-danger');
        $('#iconillo').removeClass('fa-plus fa-check-square-o fa-forward fa-times').addClass('fa-times');
        $('#btnRechazar').hide();
      }
      $('#modalPeticiones').modal('show');
    });
    $('#modalPeticiones').on('hidden.bs.modal', function() {
      $('#btnImprimir').hide();
      $('#btnRechazar').show();
      $('#btnAutorizar').hide();
      $('#btnProcesar').hide();
      $('#btnCompletar').hide();
    });
}); // Cierra document ready