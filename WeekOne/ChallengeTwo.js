function altura(inclinacao, comprimento) {
  return ((inclinacao * comprimento)/100);
}
function qtTelhas(fatorCorrecao, largura, comprimento, consumoMedio) {
  let area = largura * comprimento;
  let areaInclinada = area * fatorCorrecao;
  let qtTelhas = areaInclinada * consumoMedio;
  return (qtTelhas + (qtTelhas* 0.05));
}
function main() {
  
  let comprimento = parseFloat(document.getElementById('comprimento').value);
  let largura = parseFloat(document.getElementById('largura').value);
  let consumo = parseFloat(document.getElementById('consumo').value);
  let inclinacao = parseFloat(document.getElementById('inclinacao').value);
  let correcao = parseFloat(document.getElementById('correcao').value);

  let alt = altura(inclinacao, comprimento);
  let qt = qtTelhas(correcao, largura, comprimento, consumo);

  document.getElementById('altura').value = alt;
  document.getElementById('quantidade').value = parseInt(qt);

}