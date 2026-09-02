(function () {
  var indexEl = document.getElementById("site-search-index");
  var input = document.getElementById("site-search-input");
  var resultsEl = document.getElementById("site-search-results");
  var statusEl = document.getElementById("site-search-status");

  if (!indexEl || !input || !resultsEl || !statusEl) {
    return;
  }

  var index = [];
  try {
    index = JSON.parse(indexEl.textContent);
    // Older builds accidentally double-encoded the index as a JSON string.
    if (typeof index === "string") {
      index = JSON.parse(index);
    }
    if (!Array.isArray(index)) {
      throw new Error("Search index is not an array.");
    }
  } catch (error) {
    statusEl.textContent = "Search index could not be loaded.";
    return;
  }

  function normalize(value) {
    return (value || "").toLowerCase().replace(/\s+/g, " ").trim();
  }

  function scoreEntry(entry, query) {
    var title = normalize(entry.title);
    var text = normalize(entry.text);
    var section = normalize(entry.section);
    var haystack = title + " " + text + " " + section;
    if (!haystack.includes(query)) {
      return -1;
    }

    var score = 0;
    if (title.includes(query)) score += 4;
    if (title.startsWith(query)) score += 2;
    if (section.includes(query)) score += 1;
    if (text.includes(query)) score += 1;
    return score;
  }

  function renderResults(matches) {
    resultsEl.innerHTML = "";

    if (!matches.length) {
      statusEl.textContent = "No matches found.";
      return;
    }

    statusEl.textContent = matches.length + (matches.length === 1 ? " result" : " results");

    matches.forEach(function (entry) {
      var item = document.createElement("li");
      item.className = "site-search-result";

      var link = document.createElement("a");
      link.className = "site-search-result-link";
      link.href = entry.url;
      link.innerHTML = "<span class=\"site-search-result-title\">" + entry.title + "</span>"
        + "<span class=\"site-search-result-section\">" + entry.section + "</span>";

      item.appendChild(link);
      resultsEl.appendChild(item);
    });
  }

  function runSearch() {
    var query = normalize(input.value);
    if (query.length < 2) {
      resultsEl.innerHTML = "";
      statusEl.textContent = query.length ? "Type at least 2 characters." : "Start typing to search this site.";
      return;
    }

    var matches = index
      .map(function (entry) {
        return { entry: entry, score: scoreEntry(entry, query) };
      })
      .filter(function (item) {
        return item.score >= 0;
      })
      .sort(function (a, b) {
        return b.score - a.score || a.entry.title.localeCompare(b.entry.title);
      })
      .slice(0, 12)
      .map(function (item) {
        return item.entry;
      });

    renderResults(matches);
  }

  input.addEventListener("input", runSearch);

  var params = new URLSearchParams(window.location.search);
  var initialQuery = params.get("q");
  if (initialQuery) {
    input.value = initialQuery;
  }

  runSearch();
})();
