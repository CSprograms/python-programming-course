(function () {
  "use strict";

  var state = {
    data: null,
    qb: null,          // question bank data (loaded after the sessions)
    qbError: null,
    qbFilter: { unit: "all", part: "all", repeated: false },
    view: "intro",     // "intro" | "session" | "qb"
    filter: "",
    activeSession: null,
  };

  var els = {
    sidebar: document.getElementById("sidebar"),
    tree: document.getElementById("sidebarTree"),
    content: document.getElementById("content"),
    search: document.getElementById("searchInput"),
    drawerToggle: document.getElementById("drawerToggle"),
    scrim: document.getElementById("scrim"),
    navSessions: document.getElementById("navSessions"),
    navQB: document.getElementById("navQB"),
  };

  var TYPE_LABEL = {
    teaching: "Session",
    assignment: "Assignment",
    "class-test": "Class test",
    seminar: "Seminar",
    discussion: "Discussion",
    note: "Note",
  };

  fetch("data/sessions.json", { cache: "no-cache" })
    .then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    })
    .then(function (data) {
      state.data = data;
      buildTree();
      route();
      window.addEventListener("hashchange", route);
      loadQuestionBank();
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
      if (state.view === "qb") renderQBResults();
    }, 120);
  });

  // ---------------------------------------------------------------
  // Routing
  // ---------------------------------------------------------------
  function route() {
    var m = /^#session-(\d+)$/.exec(location.hash);
    if (location.hash === "#qb") {
      renderQB();
    } else if (m && state.data.sessions[m[1]]) {
      renderSession(parseInt(m[1], 10));
    } else {
      renderIntro();
    }
    setNav();
  }

  function setNav() {
    els.navSessions.classList.toggle("active", state.view !== "qb");
    els.navQB.classList.toggle("active", state.view === "qb");
    if (state.view === "qb") els.navQB.setAttribute("aria-current", "page");
    else els.navQB.removeAttribute("aria-current");
  }

  // ---------------------------------------------------------------
  // Intro / landing view
  // ---------------------------------------------------------------
  function renderIntro() {
    state.view = "intro";
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
    html += "</div>";
    html +=
      '<a class="intro-qb" href="#qb"><span class="t">Previous-year Question Bank \u2192</span>' +
      '<span class="d">End-semester questions (Nov 2023 \u2013 Nov 2025) that match the current syllabus, sorted by unit.</span></a>';
    html += "</div>";

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
    state.view = "session";
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
        copyText(code).then(
          function () { flashButton(btn, "Copied"); },
          function () { flashButton(btn, "Copy failed"); }
        );
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
    var activeItem = null;
    els.tree.querySelectorAll(".session-item").forEach(function (item) {
      var isActive = parseInt(item.dataset.session, 10) === state.activeSession;
      item.classList.toggle("active", isActive);
      if (isActive) activeItem = item;
    });
    // Expand the unit that holds the current session (e.g. after using
    // Previous/Next across a unit boundary or opening a #session-N link)
    // and keep the highlighted item visible in the sidebar.
    if (activeItem) {
      var block = activeItem.closest(".unit-block");
      if (block) block.classList.add("open");
      activeItem.scrollIntoView({ block: "nearest" });
    }
  }

  // ---------------------------------------------------------------
  // Question Bank view  (#qb)
  // ---------------------------------------------------------------
  function loadQuestionBank() {
    fetch("data/question_bank.json", { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (qb) {
        state.qb = qb;
        if (state.view === "qb") renderQB();
      })
      .catch(function (err) {
        state.qbError = String(err.message || err);
        if (state.view === "qb") renderQB();
      });
  }

  function renderQB() {
    state.view = "qb";
    state.activeSession = null;
    markActiveInTree();
    window.scrollTo(0, 0);

    if (!state.qb) {
      els.content.innerHTML = state.qbError
        ? '<div class="session-note">Could not load the question bank (' + escapeHtml(state.qbError) +
          "). Check that data/question_bank.json exists.</div>"
        : '<div class="qb-empty">Loading question bank\u2026</div>';
      return;
    }

    var qb = state.qb;
    var exams = qb.exams || [];
    var html = '<div class="qb-head">';
    html += '<div class="kicker">' + escapeHtml(state.data.course.code) + " \u00B7 Previous-year questions</div>";
    html += "<h1>Question Bank</h1>";
    html +=
      "<p>" + qb.questions.length + " questions from the end-semester papers" +
      (exams.length ? " of " + escapeHtml(exams[0]) + " to " + escapeHtml(exams[exams.length - 1]) : "") +
      ", grouped by unit. " + escapeHtml(qb.excluded || "") + "</p>";
    html += "</div>";

    html += '<div class="qb-filters" id="qbFilters"></div>';
    html += '<div class="qb-summary" id="qbSummary" aria-live="polite"></div>';
    html += '<div id="qbResults"></div>';
    els.content.innerHTML = html;

    renderQBFilters();
    renderQBResults();
  }

  function qbMatches(q, f, text) {
    if (f.unit !== "all" && q.units.indexOf(f.unit) === -1) return false;
    if (f.part !== "all" && q.part !== f.part) return false;
    if (f.repeated && q.asked.length < 2) return false;
    if (text) {
      var hay = (q.question + " " + q.co + " " + q.kl + " " + (q.note || "") + " " +
        q.asked.map(function (a) { return a.exam; }).join(" ")).toLowerCase();
      if (hay.indexOf(text) === -1) return false;
    }
    return true;
  }

  function renderQBFilters() {
    var f = state.qbFilter;
    var qs = state.qb.questions;
    function count(over) {
      var g = { unit: f.unit, part: f.part, repeated: f.repeated };
      for (var k in over) g[k] = over[k];
      return qs.filter(function (q) { return qbMatches(q, g, ""); }).length;
    }
    function chip(kind, value, label, on, n) {
      return '<button type="button" class="chip' + (on ? " on" : "") + '" data-kind="' + kind +
        '" data-value="' + value + '" aria-pressed="' + on + '">' + label +
        (n !== undefined ? '<span class="count">' + n + "</span>" : "") + "</button>";
    }

    var html = '<div class="qb-filter-group"><span class="label">Unit</span>';
    html += chip("unit", "all", "All", f.unit === "all", count({ unit: "all" }));
    state.data.units.forEach(function (u) {
      html += chip("unit", u.number, u.number, f.unit === u.number, count({ unit: u.number }));
    });
    html += '</div><div class="qb-filter-group"><span class="label">Part</span>';
    html += chip("part", "all", "All", f.part === "all", count({ part: "all" }));
    Object.keys(state.qb.parts).forEach(function (p) {
      html += chip("part", p, escapeHtml(p), f.part === p, count({ part: p }));
    });
    html += '</div><div class="qb-filter-group">';
    html += chip("repeated", "1", "Asked more than once", f.repeated, count({ repeated: true }));
    html += "</div>";

    var box = document.getElementById("qbFilters");
    box.innerHTML = html;
    box.querySelectorAll(".chip").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var kind = btn.dataset.kind;
        if (kind === "repeated") state.qbFilter.repeated = !state.qbFilter.repeated;
        else state.qbFilter[kind] = btn.dataset.value;
        renderQBFilters();
        renderQBResults();
      });
    });
  }

  function renderQBResults() {
    var box = document.getElementById("qbResults");
    if (!box || !state.qb) return;
    var f = state.qbFilter;
    var text = state.filter.trim().toLowerCase();
    var shown = state.qb.questions.filter(function (q) { return qbMatches(q, f, text); });

    var summary = shown.length + (shown.length === 1 ? " question" : " questions");
    if (text) summary += " matching \u201C" + state.filter.trim() + "\u201D";
    document.getElementById("qbSummary").textContent = summary;

    if (shown.length === 0) {
      box.innerHTML = '<div class="qb-empty">No questions match these filters.</div>';
      return;
    }

    var html = "";
    state.data.units.forEach(function (u) {
      // A question spanning two units (e.g. IV/V) is listed under its first
      // unit, or under the unit being filtered on.
      var inUnit = shown.filter(function (q) {
        return f.unit !== "all" ? q.units.indexOf(u.number) !== -1 : q.units[0] === u.number;
      });
      if (inUnit.length === 0) return;
      html += '<section class="qb-unit">';
      html += '<div class="qb-unit-head"><h2><span class="num">Unit ' + u.number + "</span>" +
        escapeHtml(u.title) + "</h2>" +
        '<a href="#session-' + u.start + '">Sessions ' + u.start + "\u2013" + u.end + " \u2192</a></div>";
      Object.keys(state.qb.parts).forEach(function (p) {
        var inPart = inUnit.filter(function (q) { return q.part === p; });
        if (inPart.length === 0) return;
        html += '<div class="qb-part-title">' + escapeHtml(state.qb.parts[p]) + " \u00B7 " +
          inPart.length + (inPart.length === 1 ? " question" : " questions") + "</div>";
        html += '<ol class="qb-list">';
        inPart.forEach(function (q) { html += qbItem(q); });
        html += "</ol>";
      });
      html += "</section>";
    });
    box.innerHTML = html;
  }

  function qbItem(q) {
    var html = '<li class="qb-q part-' + q.part + '">';
    html += '<div class="qb-q-text">' + escapeHtml(q.question) + "</div>";
    html += '<div class="qb-meta">';
    if (q.asked.length > 1) html += '<span class="qb-tag repeat">Asked ' + q.asked.length + "\u00D7</span>";
    html += '<span class="qb-tag" title="Knowledge level">' + escapeHtml(q.kl) + "</span>";
    html += '<span class="qb-tag" title="Course outcome">' + escapeHtml(q.co) + "</span>";
    if (q.units.length > 1) html += '<span class="qb-tag" title="Units">Units ' + escapeHtml(q.units.join(" & ")) + "</span>";
    html += '<span class="qb-asked">' + q.asked.map(function (a) {
      return escapeHtml(a.exam) + " \u00B7 Q" + escapeHtml(String(a.qno));
    }).join(", ") + "</span>";
    html += '<span title="Programme outcomes / programme-specific outcomes">' +
      escapeHtml([q.po, q.pso].filter(Boolean).join(" \u00B7 ")) + "</span>";
    html += "</div>";
    if (q.note) html += '<div class="qb-note">' + escapeHtml(q.note) + "</div>";
    html += "</li>";
    return html;
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
  // navigator.clipboard only exists on HTTPS / localhost. When the viewer is
  // opened over plain HTTP (e.g. a lab PC on the college LAN) fall back to a
  // hidden textarea + execCommand("copy").
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.top = "-1000px";
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      if (ok) resolve(); else reject(new Error("copy failed"));
    });
  }

  function flashButton(btn, label) {
    if (!btn.dataset.label) btn.dataset.label = btn.textContent;
    btn.textContent = label;
    clearTimeout(btn._flashTimer);
    btn._flashTimer = setTimeout(function () {
      btn.textContent = btn.dataset.label;
    }, 1400);
  }

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
