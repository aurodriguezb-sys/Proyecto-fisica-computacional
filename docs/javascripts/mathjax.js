// Configuración de MathJax 3 para MkDocs con pymdownx.arithmatex (generic: true).
// Arithmatex envuelve las fórmulas en \( ... \) y \[ ... \] dentro de elementos
// con la clase "arithmatex"; MathJax solo procesa esos elementos.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
