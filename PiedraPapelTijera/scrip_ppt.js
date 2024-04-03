let Estado_partida = 1; // 1 para el turno del jugador 1, 2 para el turno del jugador 2
let jugador1;
let jugador2;
let cuadro_ganador = document.getElementById("ganador");
let cuadro_reiniciar = document.getElementById("reiniciar")

function SeleccionarPiedra() {
  if (Estado_partida === 1) {
    jugador1 = "Piedra";
    Estado_partida = 2;
  } else {
    jugador2 = "Piedra";
    Resultado(jugador1, jugador2);
  }
}

function SeleccionarPapel() {
  if (Estado_partida === 1) {
    jugador1 = "Papel";
    Estado_partida = 2;
  } else {
    jugador2 = "Papel";
    Resultado(jugador1, jugador2);
  }
}

function SeleccionarTijera() {
  if (Estado_partida === 1) {
    jugador1 = "Tijera";
    Estado_partida = 2;
  } else {
    jugador2 = "Tijera";
    Resultado(jugador1, jugador2);
  }
}


function Resultado(jugador1, jugador2) {
  switch (jugador1) {
    case "Piedra":
      if (jugador2 == "Piedra") {
        cuadro_ganador.textContent = 'EMPATE';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      } else if (jugador2 == "Papel") {
        cuadro_ganador.textContent = 'Jugador 2 gana';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      } else if (jugador2 == "Tijera") {
        cuadro_ganador.textContent = 'Jugador 1 gana';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      }
      break;

      case "Papel":
      if (jugador2 == "Piedra") {
        cuadro_ganador.textContent = 'Jugador 1 gana';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      } else if (jugador2 == "Papel") {
        cuadro_ganador.textContent = 'EMPATE';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      } else if (jugador2 == "Tijera") {
        cuadro_ganador.textContent = 'Jugador 2 gana';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      }
      break;

      case "Tijera":
      if (jugador2 == "Piedra") {
        cuadro_ganador.textContent = 'Jugador 2 gana';
        cuadro_ganador.style.display = 'block'
        cuadro_reiniciar.style.display= 'block'
      } else if (jugador2 == "Papel") {
        cuadro_ganador.textContent = 'Jugador 1 gana';
        cuadro_ganador.style.display = 'block';
        cuadro_reiniciar.style.display= 'block';
      } else if (jugador2 == "Tijera") {
        cuadro_ganador.textContent = 'EMPATE';
        cuadro_ganador.style.display = 'block';
        cuadro_reiniciar.style.display= 'block';
      }
      break;
  }
}

function reiniciar() {
  Estado_partida = 1;
  cuadro_ganador.style.display = 'none';
  cuadro_reiniciar.style.display = 'none';
}