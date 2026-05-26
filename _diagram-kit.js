/* ===========================================================
   Marketplace SMC · Diagram Kit · v1.0
   Zoom + pan + click bloque → side panel + filtros canal + hover ruta
   Reusa el mismo kit en cualquier diagrama del banco
   =========================================================== */
(function () {
  window.SMCDiagram = window.SMCDiagram || {};

  /**
   * Inicializa un diagrama interactivo.
   * @param {object} cfg
   *   id           · id del .diagram-wrapper
   *   blocks       · { blockId: { type, title, sub, code, desc, stack, owner, channels, related } }
   *   connections  · [ { from, to, label?, channels? } ]   ← se usa para hover ruta
   */
  function init(cfg) {
    const root = document.getElementById(cfg.id);
    if (!root) return;

    const svg = root.querySelector('.diagram-svg');
    const canvas = root.querySelector('.diagram-canvas');
    const panel = root.querySelector('.diagram-panel');
    const panelBody = root.querySelector('.diagram-panel-body');
    const panelType = root.querySelector('.diagram-panel-type');
    const panelTitle = root.querySelector('.diagram-panel-title');
    const panelSub = root.querySelector('.diagram-panel-sub');
    const panelClose = root.querySelector('.diagram-panel-close');
    const zoomInd = root.querySelector('.diagram-zoom-indicator');

    let scale = 1, panX = 0, panY = 0;
    let isDragging = false, dragStartX = 0, dragStartY = 0, panStartX = 0, panStartY = 0;
    const activeFilters = new Set();
    const blocks = cfg.blocks || {};
    const connections = cfg.connections || [];

    // -----------------------------------------------------------
    // ZOOM + PAN
    // -----------------------------------------------------------
    function applyTransform() {
      svg.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
      if (zoomInd) zoomInd.textContent = `${Math.round(scale * 100)}%`;
    }

    function setZoom(newScale, cx, cy) {
      const rect = canvas.getBoundingClientRect();
      cx = cx != null ? cx : rect.width / 2;
      cy = cy != null ? cy : rect.height / 2;
      const ratio = newScale / scale;
      panX = cx - ratio * (cx - panX);
      panY = cy - ratio * (cy - panY);
      scale = newScale;
      applyTransform();
    }

    function fitToScreen() {
      scale = 1; panX = 0; panY = 0;
      applyTransform();
    }

    root.querySelectorAll('[data-zoom]').forEach(btn => {
      btn.addEventListener('click', () => {
        const action = btn.getAttribute('data-zoom');
        if (action === 'in')        setZoom(Math.min(scale * 1.2, 3));
        else if (action === 'out')  setZoom(Math.max(scale / 1.2, 0.4));
        else if (action === 'reset')fitToScreen();
        else if (action === 'fullscreen') root.classList.toggle('is-fullscreen');
      });
    });

    // wheel zoom
    canvas.addEventListener('wheel', (e) => {
      if (!e.ctrlKey && !e.metaKey) return;
      e.preventDefault();
      const rect = canvas.getBoundingClientRect();
      const cx = e.clientX - rect.left;
      const cy = e.clientY - rect.top;
      const delta = e.deltaY < 0 ? 1.1 : 1 / 1.1;
      setZoom(Math.max(0.4, Math.min(3, scale * delta)), cx, cy);
    }, { passive: false });

    // drag pan
    canvas.addEventListener('mousedown', (e) => {
      // si fue click en un bloque, no inicia drag (lo deja al click handler)
      if (e.target.closest('.block')) return;
      isDragging = true;
      canvas.classList.add('is-panning');
      dragStartX = e.clientX; dragStartY = e.clientY;
      panStartX = panX; panStartY = panY;
    });
    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      panX = panStartX + (e.clientX - dragStartX);
      panY = panStartY + (e.clientY - dragStartY);
      applyTransform();
    });
    window.addEventListener('mouseup', () => {
      if (isDragging) { isDragging = false; canvas.classList.remove('is-panning'); }
    });

    // -----------------------------------------------------------
    // SIDE PANEL
    // -----------------------------------------------------------
    function openPanel(blockId) {
      const data = blocks[blockId];
      if (!data) return;

      panelType.textContent = data.type || 'Bloque';
      panelTitle.textContent = data.title || blockId;
      panelSub.textContent = data.sub || '';

      let html = '';

      if (data.desc) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Descripción</div>
          <p>${data.desc}</p>
        </div>`;
      }
      if (data.stack && data.stack.length) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Stack</div>
          <div class="panel-chips">${data.stack.map(s => `<span class="panel-chip">${s}</span>`).join('')}</div>
        </div>`;
      }
      if (data.channels && data.channels.length) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Canales</div>
          <div class="panel-chips">${data.channels.map(c => `<span class="panel-chip is-channel-${c}">${c.toUpperCase()}</span>`).join('')}</div>
        </div>`;
      }
      if (data.owner) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Owner</div>
          <p>${data.owner}</p>
        </div>`;
      }
      if (data.endpoints && data.endpoints.length) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Endpoints</div>
          <ul>${data.endpoints.map(e => `<li><code>${e}</code></li>`).join('')}</ul>
        </div>`;
      }
      if (data.notes) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Notas</div>
          <p>${data.notes}</p>
        </div>`;
      }
      if (data.related && data.related.length) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Docs relacionados</div>
          <div class="panel-related">${data.related.map(r => `<a href="${r.href}">${r.title}<small>${r.sub || ''}</small></a>`).join('')}</div>
        </div>`;
      }
      panelBody.innerHTML = html;
      panel.classList.add('is-open');
      highlightConnections(blockId);
    }

    function closePanel() {
      panel.classList.remove('is-open');
      clearHighlight();
    }
    panelClose.addEventListener('click', closePanel);

    // click bloque
    svg.querySelectorAll('.block').forEach(el => {
      el.addEventListener('click', () => {
        const id = el.getAttribute('data-id');
        openPanel(id);
      });
    });

    // ESC cierra panel
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && panel.classList.contains('is-open')) closePanel();
    });

    // -----------------------------------------------------------
    // HOVER RUTA: cuando hover bloque · highlight conexiones que tocan ese bloque
    // -----------------------------------------------------------
    function highlightConnections(blockId) {
      const touchingConns = connections.filter(c => c.from === blockId || c.to === blockId);
      const touchingBlocks = new Set([blockId]);
      touchingConns.forEach(c => { touchingBlocks.add(c.from); touchingBlocks.add(c.to); });

      svg.querySelectorAll('.block').forEach(el => {
        const id = el.getAttribute('data-id');
        if (touchingBlocks.has(id)) {
          el.classList.add('is-highlight');
          el.classList.remove('is-dimmed');
        } else {
          el.classList.add('is-dimmed');
          el.classList.remove('is-highlight');
        }
      });

      svg.querySelectorAll('.conn').forEach(line => {
        const f = line.getAttribute('data-from');
        const t = line.getAttribute('data-to');
        if ((f === blockId) || (t === blockId)) {
          line.classList.add('is-highlight');
          line.classList.remove('is-dimmed');
        } else {
          line.classList.add('is-dimmed');
          line.classList.remove('is-highlight');
        }
      });
    }

    function clearHighlight() {
      svg.querySelectorAll('.block').forEach(el => {
        el.classList.remove('is-highlight', 'is-dimmed');
      });
      svg.querySelectorAll('.conn').forEach(line => {
        line.classList.remove('is-highlight', 'is-dimmed');
      });
      applyFilters();
    }

    svg.querySelectorAll('.block').forEach(el => {
      el.addEventListener('mouseenter', () => {
        if (panel.classList.contains('is-open')) return;
        const id = el.getAttribute('data-id');
        highlightConnections(id);
      });
      el.addEventListener('mouseleave', () => {
        if (panel.classList.contains('is-open')) return;
        clearHighlight();
      });
    });

    // -----------------------------------------------------------
    // FILTROS CANAL
    // -----------------------------------------------------------
    function applyFilters() {
      if (activeFilters.size === 0) {
        svg.querySelectorAll('.block').forEach(el => el.classList.remove('is-dimmed'));
        svg.querySelectorAll('.conn').forEach(el => el.classList.remove('is-dimmed'));
        return;
      }
      svg.querySelectorAll('.block').forEach(el => {
        const id = el.getAttribute('data-id');
        const data = blocks[id];
        const matches = data && data.channels && data.channels.some(c => activeFilters.has(c));
        const noChannel = !data || !data.channels || data.channels.length === 0;
        if (matches || noChannel) el.classList.remove('is-dimmed');
        else el.classList.add('is-dimmed');
      });
      svg.querySelectorAll('.conn').forEach(line => {
        const ch = (line.getAttribute('data-channels') || '').split(',').filter(Boolean);
        if (ch.length === 0) { line.classList.remove('is-dimmed'); return; }
        if (ch.some(c => activeFilters.has(c))) line.classList.remove('is-dimmed');
        else line.classList.add('is-dimmed');
      });
    }

    root.querySelectorAll('.diagram-filter').forEach(btn => {
      btn.addEventListener('click', () => {
        const ch = btn.getAttribute('data-channel');
        if (!ch) return;
        if (activeFilters.has(ch)) {
          activeFilters.delete(ch);
          btn.classList.remove('is-active');
        } else {
          activeFilters.add(ch);
          btn.classList.add('is-active');
        }
        applyFilters();
      });
    });

    // init
    applyTransform();
  }

  window.SMCDiagram.init = init;

  // ===========================================================
  // PIPELINE · selector de escenarios + etapas + INT boxes
  // ===========================================================

  /**
   * @param {object} cfg
   *   id          · id del .process-wrapper (vacío · se renderiza completo desde JS)
   *   scenarios   · { A: {letter, title, sub, tags, callout, stages:[{num,name,boxes:[{code,label,kind,stack,desc,notes,doc}]}]}, B:{...}, ... }
   *   default     · letra del escenario activo inicial
   */
  function initPipeline(cfg) {
    const root = document.getElementById(cfg.id);
    if (!root) return;

    const scenarios = cfg.scenarios || {};
    const letters = Object.keys(scenarios);
    let active = cfg.default || letters[0];

    function esc(s) {
      return (s == null ? '' : String(s))
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function renderScenarios() {
      return `<div class="scenario-grid">
        ${letters.map(L => {
          const s = scenarios[L];
          return `<div class="scenario-card ${L === active ? 'is-active' : ''}" data-letter="${L}">
            <div class="scenario-letter">${L}</div>
            <div class="scenario-title">${esc(s.title)}</div>
            <div class="scenario-sub">${esc(s.sub || '')}</div>
          </div>`;
        }).join('')}
      </div>`;
    }

    function renderDetail() {
      const s = scenarios[active];
      const total = (s.stages || []).reduce((acc, st) => acc + (st.boxes || []).length, 0);
      return `<div class="scenario-detail">
        <strong>Escenario activo: ${esc(s.title)} (${active})</strong> · ${esc(s.callout || s.sub || '')}
        ${s.tags ? `<br><span style="font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#475569;">${s.tags.join(' · ')} · ${s.stages.length} etapas · ${total} pasos</span>` : ''}
      </div>`;
    }

    function renderPipeline() {
      const s = scenarios[active];
      const stages = s.stages || [];
      const head = stages.map((st, i) => {
        const isLast = i === stages.length - 1;
        return `<div class="pipeline-stage-head ${isLast ? 'is-last' : ''}">
          <div class="pipeline-stage-num">Etapa ${st.num}</div>
          <h4 class="pipeline-stage-name">${esc(st.name)}</h4>
        </div>`;
      }).join('');
      const body = stages.map((st, i) => {
        const isLast = i === stages.length - 1;
        const boxes = (st.boxes || []).map((b, j) => `
          <div class="int-box kind-${b.kind || 'search'}" data-stage="${i}" data-box="${j}">
            <span class="int-code">${esc(b.code || '')}</span>
            <p class="int-label">${esc(b.label || '')}</p>
            ${b.stack ? `<span class="int-stack">${esc(b.stack)}</span>` : ''}
          </div>`).join('');
        return `<div class="pipeline-stage-col ${isLast ? 'is-last' : ''}">
          <div class="pipeline-stage-col-inner">${boxes}</div>
        </div>`;
      }).join('');
      return `<div class="pipeline-shell">
        <div class="pipeline-header">${head}</div>
        <div class="pipeline-body">${body}</div>
        <div class="pipeline-meta">
          <strong>${esc(s.title)}</strong> · ${esc(s.sub || '')}
          ${s.notes ? ' · ' + esc(s.notes) : ''}
        </div>
      </div>`;
    }

    function renderPanel() {
      return `<aside class="diagram-panel">
        <div class="diagram-panel-header">
          <button class="diagram-panel-close" aria-label="Cerrar">×</button>
          <div class="diagram-panel-type">Paso</div>
          <h3 class="diagram-panel-title">Detalle</h3>
          <p class="diagram-panel-sub"></p>
        </div>
        <div class="diagram-panel-body"></div>
      </aside>`;
    }

    function render() {
      root.innerHTML = renderScenarios() + renderDetail() + renderPipeline() + renderPanel();
      bind();
    }

    function openBoxPanel(stageIdx, boxIdx) {
      const s = scenarios[active];
      const st = s.stages[stageIdx];
      const b = st.boxes[boxIdx];
      const panel = root.querySelector('.diagram-panel');
      const panelType = root.querySelector('.diagram-panel-type');
      const panelTitle = root.querySelector('.diagram-panel-title');
      const panelSub = root.querySelector('.diagram-panel-sub');
      const panelBody = root.querySelector('.diagram-panel-body');

      panelType.textContent = `${b.code || ''} · Etapa ${st.num} · ${st.name}`;
      panelTitle.textContent = b.label || b.code || 'Paso';
      panelSub.textContent = `Escenario ${active} · ${s.title}`;

      let html = '';
      if (b.desc) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Descripción</div>
          <p>${esc(b.desc)}</p>
        </div>`;
      }
      if (b.stack) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Stack · tecnología</div>
          <p>${esc(b.stack)}</p>
        </div>`;
      }
      if (b.endpoints && b.endpoints.length) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Endpoints / referencia</div>
          <ul>${b.endpoints.map(e => `<li><code>${esc(e)}</code></li>`).join('')}</ul>
        </div>`;
      }
      if (b.payload) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Sample payload</div>
          <pre class="ascii" style="font-size:11px;background:#0F172A;color:#A7F3D0;padding:12px;border-radius:8px;overflow-x:auto;">${esc(b.payload)}</pre>
        </div>`;
      }
      if (b.errors && b.errors.length) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Errores comunes</div>
          <ul>${b.errors.map(e => `<li>${esc(e)}</li>`).join('')}</ul>
        </div>`;
      }
      if (b.notes) {
        html += `<div class="panel-section">
          <div class="panel-section-label">Notas</div>
          <p>${esc(b.notes)}</p>
        </div>`;
      }
      if (b.doc) {
        const docs = Array.isArray(b.doc) ? b.doc : [b.doc];
        html += `<div class="panel-section">
          <div class="panel-section-label">Docs relacionados</div>
          <div class="panel-related">${docs.map(d => `<a href="${esc(d.href)}">${esc(d.title)}<small>${esc(d.sub || '')}</small></a>`).join('')}</div>
        </div>`;
      }
      panelBody.innerHTML = html;

      root.querySelectorAll('.int-box').forEach(el => el.classList.remove('is-active'));
      root.querySelector(`.int-box[data-stage="${stageIdx}"][data-box="${boxIdx}"]`)?.classList.add('is-active');
      panel.classList.add('is-open');
    }

    function bind() {
      // scenario click
      root.querySelectorAll('.scenario-card').forEach(card => {
        card.addEventListener('click', () => {
          const L = card.getAttribute('data-letter');
          if (L === active) return;
          active = L;
          render();
        });
      });
      // INT box click
      root.querySelectorAll('.int-box').forEach(box => {
        box.addEventListener('click', () => {
          openBoxPanel(parseInt(box.getAttribute('data-stage')), parseInt(box.getAttribute('data-box')));
        });
      });
      // panel close
      root.querySelector('.diagram-panel-close')?.addEventListener('click', () => {
        root.querySelector('.diagram-panel').classList.remove('is-open');
        root.querySelectorAll('.int-box').forEach(el => el.classList.remove('is-active'));
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key !== 'Escape') return;
      const panel = root.querySelector('.diagram-panel');
      if (panel && panel.classList.contains('is-open')) {
        panel.classList.remove('is-open');
        root.querySelectorAll('.int-box').forEach(el => el.classList.remove('is-active'));
      }
    });

    render();
  }

  window.SMCDiagram.initPipeline = initPipeline;
})();
