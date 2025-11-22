// Contador em tempo real para o campo whatsapp_boas_vindas no Admin
// Mostra tamanho bruto (trim) e tamanho codificado para URL (encodeURIComponent)
(function () {
  function updateCounter(textarea, counterEl) {
    var raw = textarea.value || "";
    var trimmed = raw.trim();
    var rawLen = trimmed.length;
    var encodedLen = encodeURIComponent(trimmed).length;
    var RAW_LIMIT = 255; // limite do CharField no modelo
    var ENCODED_LIMIT = 2000; // limite definido no ModelForm

    var warnings = [];
    if (rawLen > RAW_LIMIT) warnings.push("bruto > " + RAW_LIMIT);
    if (encodedLen > ENCODED_LIMIT) warnings.push("codificado > " + ENCODED_LIMIT);

    var text = "Bruto: " + rawLen + " | Codificado (URL): " + encodedLen;
    if (warnings.length) {
      text += " — Limite excedido: " + warnings.join(", ");
      counterEl.style.color = "#b91c1c"; // vermelho
    } else {
      counterEl.style.color = "#374151"; // cinza
    }
    counterEl.textContent = text;
  }

  function init() {
    var textarea = document.querySelector('textarea[name="whatsapp_boas_vindas"]');
    if (!textarea) return;

    var counter = document.createElement("div");
    counter.className = "help"; // usa estilo de help-text do Admin
    counter.style.marginTop = "4px";
    textarea.parentElement.appendChild(counter);

    var handler = function () { updateCounter(textarea, counter); };
    textarea.addEventListener("input", handler);
    textarea.addEventListener("change", handler);
    handler();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();