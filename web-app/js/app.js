(function () {
  "use strict";

  var state = { data: null, filter: "", activeSession: null };

  var els = {
    sidebar: document.getElementById("sidebar"),
    tree: document.getElementById("sidebarTree"),
    content: document.getElementById("content"),
    search: document.getElementById("searchInput"),
    drawerToggle: document.getElementById("drawerToggle"),
    scrim: document.getElementById("scrim"),
  };

  var TYPE_LABEL = {
    teaching: "Session",
    assignment: "Assignment",
    "class-test": "Class test",
    seminar: "Seminar",
    discussion: "Discussion",
    note: "Note",
  };

  fetch("data/sessions.json")
    .then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    })
    .then(function (data) {
      state.data = data;
      buildTree();
      route();
      window.addEventListener("hashchange", route);
    })
    .catch(function (err) {
      els.content.innerHTML =
        '<div class="session-note">Could not load session data (' +
        escapeHtml(String(err.message || err)) +
        "). Check that data/sessions.json exists next to index.html.</div>";
    });

  // ---------------------------------------------------------------
  // Sidebar tree
  // ---------------------------------------------------------------
  function buildTree() {
    var frag = document.createDocumentFragment();
    var q = state.filter.trim().toLowerCase();

    state.data.units.forEach(function (unit) {
      var sessionsInUnit = [];
      for (var n = unit.start; n <= unit.end; n++) {
        var s = state.data.sessions[String(n)];
        if (!s) continue;
        if (q && !sessionMatches(s, q)) continue;
        sessionsInUnit.push(s);
      }
      if (q && sessionsInUnit.length === 0) return;

      var block = document.createElement("div");
      block.className = "unit-block";
      if (q || (state.activeSession && state.activeSession >= unit.start && state.activeSession <= unit.end)) {
        block.classList.add("open");
      }

      var head = document.createElement("button");
      head.className = "unit-head";
      head.innerHTML =
        '<span class="num">Unit ' + unit.number + "</span>" +
        '<span class="title">' + escapeHtml(unit.title) + "</span>" +
        '<span class="chev">\u25B8</span>';
      head.addEventListener("click", function () {
        block.classList.toggle("open");
      });
      block.appendChild(head);

      var list = document.createElement("div");
      list.className = "session-list";

      (q ? sessionsInUnit : allSessionsInRange(unit.start, unit.end)).forEach(function (s) {
        var item = document.createElement("button");
        item.className = "session-item";
        if (state.activeSession === s.number) item.classList.add("active");
        item.dataset.session = s.number;
        var label = sessionLabel(s);
        item.innerHTML =
          '<span class="n">' + String(s.number).padStart(2, "0") + "</span>" +
          '<span class="type-dot ' + s.type + '"></span>' +
          '<span class="label">' + escapeHtml(label) + "</span>";
        item.addEventListener("click", function () {
          location.hash = "#session-" + s.number;
          closeDrawer();
        });
        list.appendChild(item);
      });

      block.appendChild(list);
      frag.appendChild(block);
    });

    els.tree.innerHTML = "";
    if (frag.childNodes.length === 0) {
      var empty = document.createElement("div");
      empty.className = "no-results";
      empty.textContent = "No sessions match your search.";
      els.tree.appendChild(empty);
    } else {
      els.tree.appendChild(frag);
    }
  }

  function allSessionsInRange(start, end) {
    var out = [];
    for (var n = start; n <= end; n++) {
      var s = state.data.sessions[String(n)];
      if (s) out.push(s);
    }
    return out;
  }

  function sessionLabel(s) {
    if (s.programs.length === 0) return TYPE_LABEL[s.type] || "Session";
    if (s.type === "assignment") return "Assignment";
    if (s.type === "class-test") return "Class test";
    return s.programs.length + (s.programs.length === 1 ? " program" : " programs");
  }

  function sessionMatches(s, q) {
    if (("session " + s.number).indexOf(q) !== -1) return true;
    if (String(s.number) === q) return true;
    if (s.note && s.note.toLowerCase().indexOf(q) !== -1) return true;
    return s.programs.some(function (p) {
      return (
        (p.title && p.title.toLowerCase().indexOf(q) !== -1) ||
        (p.description && p.description.toLowerCase().indexOf(q) !== -1) ||
        (p.code && p.code.toLowerCase().indexOf(q) !== -1)
      );
    });
  }

  var searchDebounce;
  els.search.addEventListener("input", function () {
    clearTimeout(searchDebounce);
    var v = els.search.value;
    searchDebounce = setTimeout(function () {
      state.filter = v;
      buildTree();
    }, 120);
  });

  // ---------------------------------------------------------------
  // Routing
  // ---------------------------------------------------------------
  function route() {
    var m = /^#session-(\d+)$/.exec(location.hash);
    if (m && state.data.sessions[m[1]]) {
      renderSession(parseInt(m[1], 10));
    } else {
      renderIntro();
    }
  }

  // ---------------------------------------------------------------
  // Intro / landing view
  // ---------------------------------------------------------------
  function renderIntro() {
    state.activeSession = null;
    markActiveInTree();
    var c = state.data.course;
    var totalPrograms = Object.keys(state.data.sessions).reduce(function (acc, k) {
      return acc + state.data.sessions[k].programs.length;
    }, 0);

    var html = '<div class="intro">';
    html += '<div class="kicker">' + escapeHtml(c.code) + "</div>";
    html += "<h1>" + escapeHtml(c.title) + "</h1>";
    html +=
      "<p>" +
      escapeHtml(c.section) +
      ", " +
      escapeHtml(c.institution) +
      ". Seventy-five one-hour sessions, " +
      totalPrograms +
      " runnable programs — pick a session from the list to read the code, the description, and the documented sample output.</p>";
    html += '<div class="unit-cards">';
    state.data.units.forEach(function (u) {
      html +=
        '<button class="unit-card" data-unit="' + u.number + '">' +
        '<div class="u-num">Unit ' + u.number + "</div>" +
        '<div class="u-title">' + escapeHtml(u.title) + "</div>" +
        '<div class="u-range">Sessions ' + u.start + "\u2013" + u.end + "</div>" +
        "</button>";
    });
    html += "</div></div>";

    els.content.innerHTML = html;

    els.content.querySelectorAll(".unit-card").forEach(function (card) {
      card.addEventListener("click", function () {
        var num = card.dataset.unit;
        var unitBlocks = els.tree.querySelectorAll(".unit-block");
        unitBlocks.forEach(function (b) {
          var head = b.querySelector(".unit-head .num");
          if (head && head.textContent === "Unit " + num) {
            b.classList.add("open");
            b.scrollIntoView({ block: "nearest" });
          }
        });
        openDrawer();
      });
    });
  }

  // ---------------------------------------------------------------
  // Session view
  // ---------------------------------------------------------------
  function renderSession(num) {
    state.activeSession = num;
    markActiveInTree();

    var s = state.data.sessions[String(num)];
    var unit = state.data.units.filter(function (u) {
      return u.number === s.unit;
    })[0];

    var html = '<div class="session-header">';
    html += '<div class="big-num">' + String(num).padStart(2, "0") + "</div>";
    html += '<div class="heading-block">';
    html +=
      '<div class="unit-crumb">Unit ' +
      (unit ? unit.number + " \u00B7 " + escapeHtml(unit.title) : "") +
      "</div>";
    html += "<h1>Session " + num + "</h1>";
    html +=
      '<div class="session-type-tag"><span class="type-dot ' +
      s.type +
      '"></span>' +
      (TYPE_LABEL[s.type] || "Session") +
      "</div>";
    html += "</div></div>";

    if (s.programs.length === 0) {
      html += '<div class="session-note">' + formatNote(s.note || "No programs for this session.") + "</div>";
    } else {
      s.programs.forEach(function (p, i) {
        html += '<div class="program">';
        html += '<div class="program-head">';
        html += '<span class="program-num">' + (i + 1) + "</span>";
        html += '<h2 class="program-title">' + escapeHtml(p.title) + "</h2>";
        html += "</div>";
        if (p.description) {
          html += '<p class="program-desc">' + escapeHtml(p.description) + "</p>";
        }
        html += '<div class="code-block">';
        html += '<div class="code-bar"><span>' + escapeHtml(p.file) + '</span><button class="copy-btn" type="button">Copy</button></div>';
        html += '<pre><code class="language-python">' + escapeHtml(p.code) + "</code></pre>";
        html += "</div>";
        if (p.sample_output) {
          html +=
            '<div class="output-block"><div class="output-label">Sample Output</div><pre>' +
            escapeHtml(p.sample_output) +
            "</pre></div>";
        }
        if (p.try_also) {
          html +=
            '<div class="try-also"><span class="tag">Try also</span>' +
            escapeHtml(p.try_also) +
            "</div>";
        }
        html += "</div>";
      });
    }

    html += buildPrevNext(num);

    els.content.innerHTML = html;
    els.content.scrollTop = 0;
    window.scrollTo(0, 0);

    els.content.querySelectorAll("pre code").forEach(function (block) {
      if (window.hljs) window.hljs.highlightElement(block);
    });

    els.content.querySelectorAll(".copy-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var code = btn.closest(".code-block").querySelector("code").textContent;
        navigator.clipboard.writeText(code).then(function () {
          var original = btn.textContent;
          btn.textContent = "Copied";
          setTimeout(function () {
            btn.textContent = original;
          }, 1400);
        });
      });
    });
  }

  function buildPrevNext(num) {
    var prev = findAdjacent(num, -1);
    var next = findAdjacent(num, 1);
    var html = '<div class="prev-next">';
    html += prev
      ? '<a href="#session-' + prev.number + '"><span class="dir">\u2190 Previous</span>Session ' + prev.number + "</a>"
      : "<span></span>";
    html += next
      ? '<a class="next" href="#session-' + next.number + '"><span class="dir">Next \u2192</span>Session ' + next.number + "</a>"
      : "<span></span>";
    html += "</div>";
    return html;
  }

  function findAdjacent(num, dir) {
    var n = num + dir;
    while (n >= 1 && n <= 75) {
      var s = state.data.sessions[String(n)];
      if (s) return s;
      n += dir;
    }
    return null;
  }

  function markActiveInTree() {
    els.tree.querySelectorAll(".session-item").forEach(function (item) {
      item.classList.toggle("active", parseInt(item.dataset.session, 10) === state.activeSession);
    });
  }

  // ---------------------------------------------------------------
  // Mobile drawer
  // ---------------------------------------------------------------
  function openDrawer() {
    els.sidebar.classList.add("open");
    els.scrim.classList.add("open");
    els.drawerToggle.setAttribute("aria-expanded", "true");
  }
  function closeDrawer() {
    if (window.innerWidth > 860) return;
    els.sidebar.classList.remove("open");
    els.scrim.classList.remove("open");
    els.drawerToggle.setAttribute("aria-expanded", "false");
  }
  els.drawerToggle.addEventListener("click", function () {
    if (els.sidebar.classList.contains("open")) closeDrawer();
    else openDrawer();
  });
  els.scrim.addEventListener("click", closeDrawer);

  // ---------------------------------------------------------------
  // Utils
  // ---------------------------------------------------------------
  function formatNote(str) {
    // Note text is our own generated content (from README.md files in the
    // repo, not user input), so a light, non-recursive markdown pass for
    // **bold** and `code` spans on the already-escaped string is safe.
    var escaped = escapeHtml(str);
    escaped = escaped.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    escaped = escaped.replace(/`([^`]+?)`/g, "<code>$1</code>");
    return escaped;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }
})();
