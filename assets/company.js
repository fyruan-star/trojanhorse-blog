// Company stats pages: the Season type and Per mode menus pick which of the
// four prebuilt tables shows. Without scripts the page shows fiscal-year totals.
(function () {
  var season = document.getElementById("cp-season"), mode = document.getElementById("cp-mode");
  if (!season || !mode) return;
  season.closest(".cp-filters").hidden = false;
  function show() {
    var want = season.value + "-" + mode.value;
    document.querySelectorAll(".cp-tbl").forEach(function (t) { t.hidden = t.getAttribute("data-k") !== want; });
  }
  season.addEventListener("change", show);
  mode.addEventListener("change", show);
  show();
})();
