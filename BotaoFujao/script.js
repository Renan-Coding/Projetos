function fuja(){
    var botaonao = document.getElementById('nao')

    var largurajanela = window.innerWidth;
    var alturajanela = window.innerHeight;

    var maxX = largurajanela - botaonao.offsetWidth
    var maxY = alturajanela - botaonao.offsetHeight

    var aleatorioX = Math.floor(Math.random() * maxX)
    var aleatorioY = Math.floor(Math.random() * maxY)

    botaonao.style.left = aleatorioX + "px";
    botaonao.style.top = aleatorioY + "px";
}
